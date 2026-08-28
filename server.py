#!/usr/bin/env python3
"""Georgia real estate exam prep -- local web server.

Run:  python3 server.py        (then open http://localhost:8778)
No third-party packages required.
"""
import json
import mimetypes
import os
import posixpath
import random
import sys
import threading
import time
import uuid
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from greprep import mathgen, questions, scheduler, store, topics   # noqa: E402

WEB_DIR = os.path.join(HERE, "web")
PORT = int(os.environ.get("GAPREP_PORT", "8778"))
LOCK = threading.Lock()
SESSIONS = {}
SECONDS_PER_QUESTION = 75          # PSI pacing: ~4 hours for 152 questions


# --------------------------------------------------------------- helpers
def _public(q, index):
    """The question as the browser sees it -- no answer key."""
    return {"n": index, "id": q["id"], "topic": q["topic"],
            "topic_label": topics.label(q["topic"]),
            "portion": q.get("portion", "national"),
            "difficulty": q.get("difficulty", 1),
            "q": q["q"], "choices": q["choices"],
            "generator": q.get("generator")}


def _meta():
    return {
        "portions": topics.PORTIONS,
        "topics": topics.catalog(),
        "banks": questions.bank_summary(),
        "math_topics": [{"key": k, "label": v[0], "concept": v[1],
                         "closing": k in mathgen.CLOSING}
                        for k, v in mathgen.TOPICS.items()],
        "difficulties": questions.DIFFICULTIES,
        "seconds_per_question": SECONDS_PER_QUESTION,
    }


def _progress_payload(data):
    return {
        "profile": data.get("profile", {}),
        "portions": store.portion_stats(data),
        "topics": store.topic_report(data),
        "generators": store.generator_report(data),
        "trends": store.trend_series(data),
        "attempts": data["attempts"][-60:],
        "total_attempts": len(data["attempts"]),
    }


# --------------------------------------------------------------- handler
class Handler(BaseHTTPRequestHandler):
    server_version = "GAPrep/1.0"

    def log_message(self, fmt, *args):
        if os.environ.get("GAPREP_VERBOSE"):
            sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))

    def _send(self, code, body, ctype="application/json; charset=utf-8"):
        if not isinstance(body, (bytes, bytearray)):
            body = body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        try:
            self.wfile.write(body)
        except (BrokenPipeError, ConnectionResetError):
            pass

    def _json(self, obj, code=200):
        self._send(code, json.dumps(obj))

    def _body(self):
        try:
            n = int(self.headers.get("Content-Length") or 0)
        except ValueError:
            n = 0
        if not n:
            return {}
        try:
            return json.loads(self.rfile.read(n).decode("utf-8"))
        except ValueError:
            return {}

    # ------------------------------------------------------------- static
    def _static(self, path):
        rel = posixpath.normpath(path.lstrip("/")) or "index.html"
        if rel.startswith(".."):
            return self._send(403, "forbidden", "text/plain")
        full = os.path.join(WEB_DIR, rel)
        if os.path.isdir(full):
            full = os.path.join(full, "index.html")
        if not os.path.isfile(full):
            return self._send(404, "not found", "text/plain")
        ctype = mimetypes.guess_type(full)[0] or "application/octet-stream"
        with open(full, "rb") as f:
            self._send(200, f.read(), ctype)

    # ---------------------------------------------------------------- GET
    def do_GET(self):
        path = self.path.split("?", 1)[0]
        if path == "/api/meta":
            return self._json(_meta())
        if path == "/api/progress":
            with LOCK:
                return self._json(_progress_payload(store.load()))
        if path == "/api/plan":
            with LOCK:
                data = store.load()
            prof = data.get("profile", {})
            return self._json(scheduler.generate(
                data, prof.get("exam_date"), prof.get("mastery_date"),
                prof.get("declared_weak"), prof.get("hours_per_week", 8)))
        return self._static(path)

    # --------------------------------------------------------------- POST
    def do_POST(self):
        path = self.path.split("?", 1)[0]
        body = self._body()

        if path == "/api/profile":
            with LOCK:
                data = store.load()
                prof = data.setdefault("profile", {})
                for k in ("exam_date", "mastery_date", "hours_per_week", "declared_weak"):
                    if k in body:
                        prof[k] = body[k]
                store.save(data)
                return self._json({"profile": prof})

        if path == "/api/quiz/start":
            portion = body.get("portion", "national")
            count = max(1, min(200, int(body.get("count") or 20)))
            weak = bool(body.get("weak_spot"))
            topic = body.get("topic") or None
            diff = body.get("difficulty") or "harder"
            if diff not in questions.DIFFICULTIES:
                diff = "harder"
            with LOCK:
                data = store.load()
            if body.get("mode") == "exam":
                qs = questions.mock_exam(difficulty=diff)
                portion, count = "mixed", len(qs)
            else:
                qs = questions.select(portion, count, weak_spot=weak,
                                      progress=data, topic=topic, difficulty=diff)
            if not qs:
                return self._json({"error": "No questions matched."}, 400)
            sid = uuid.uuid4().hex[:12]
            limit = len(qs) * SECONDS_PER_QUESTION if body.get("timed", True) else 0
            with LOCK:
                SESSIONS[sid] = {
                    "questions": qs, "portion": portion, "weak_spot": weak,
                    "mode": body.get("mode") or ("topic" if topic else "quiz"),
                    "started": time.time(), "limit": limit,
                    "answers": [None] * len(qs), "topic": topic,
                }
            return self._json({
                "session": sid, "count": len(qs), "limit_seconds": limit,
                "portion": portion, "weak_spot": weak, "difficulty": diff,
                "questions": [_public(q, i) for i, q in enumerate(qs)],
            })

        if path == "/api/quiz/answer":
            sid = body.get("session")
            with LOCK:
                sess = SESSIONS.get(sid)
            if not sess:
                return self._json({"error": "That quiz session expired. Start a new quiz."}, 404)
            try:
                idx = int(body.get("index"))
                q = sess["questions"][idx]
            except (TypeError, ValueError, IndexError):
                return self._json({"error": "bad question index"}, 400)
            choice = body.get("choice")
            choice = int(choice) if choice is not None else None
            correct = (choice == q["answer"])
            with LOCK:
                sess["answers"][idx] = {
                    "qid": q["id"], "topic": q["topic"],
                    "generator": q.get("generator"),
                    "choice": choice, "correct": correct,
                    "seconds": float(body.get("seconds") or 0),
                }
            return self._json({
                "correct": correct,
                "answer": q["answer"],
                "answer_text": q["choices"][q["answer"]],
                "concept": q.get("concept", ""),
                "explain": q.get("explain", ""),
                "steps": q.get("steps") or [],
                "topic_label": topics.label(q["topic"]),
            })

        if path == "/api/quiz/finish":
            sid = body.get("session")
            with LOCK:
                sess = SESSIONS.pop(sid, None)
            if not sess:
                return self._json({"error": "session not found"}, 404)
            answered = [a for a in sess["answers"] if a]
            # unanswered questions count as wrong, same as the real exam
            for i, a in enumerate(sess["answers"]):
                if a is None:
                    q = sess["questions"][i]
                    answered.append({"qid": q["id"], "topic": q["topic"],
                                     "generator": q.get("generator"),
                                     "choice": None, "correct": False, "seconds": 0.0})
            elapsed = time.time() - sess["started"]
            with LOCK:
                data = store.load()
                attempt = store.record_attempt(
                    data, sess["portion"], sess["mode"], answered,
                    elapsed, weak_spot=sess["weak_spot"])
                store.save(data)
                payload = _progress_payload(data)
            return self._json({"attempt": attempt, "progress": payload})

        if path == "/api/reset":
            if body.get("confirm") != "DELETE":
                return self._json({"error": "confirmation required"}, 400)
            with LOCK:
                data = store.load()
                data["attempts"] = []
                data["topics"] = {}
                data["items"] = {}
                data["generators"] = {}
                store.save(data)
            return self._json({"ok": True})

        return self._json({"error": "unknown endpoint"}, 404)


def main():
    random.seed()
    srv = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    url = "http://localhost:%d" % PORT
    print("Georgia Real Estate Prep is running.")
    print("   Open:  %s" % url)
    print("   Stop:  Ctrl-C")
    if os.environ.get("GAPREP_OPEN"):
        threading.Timer(0.7, lambda: webbrowser.open(url)).start()
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped. Your progress is saved in data/progress.json")


if __name__ == "__main__":
    main()
