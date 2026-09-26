#!/usr/bin/env python3
"""Render the site icons and the link-preview card.

macOS only: it draws SVG and lets WebKit rasterise it through qlmanage, then
trims the square thumbnail back to the aspect ratio we asked for. The PNGs are
committed, so a build on any other machine just uses what is already in docs/.

Run:  python3 tools/make_icons.py
"""
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(HERE, "docs", "assets")

INK = "#e8eef4"
DIM = "#8fa3b5"
BG = "#0e1319"
ACCENT = "#5fc0ad"
BRASS = "#d6a445"
SANS = "'Helvetica Neue',Helvetica,Arial,sans-serif"


def icon_svg(size):
    """A rounded slab with GA set in condensed caps over a roofline."""
    r = size * 0.22
    return """<svg xmlns="http://www.w3.org/2000/svg" width="%(s)d" height="%(s)d" viewBox="0 0 512 512">
<rect width="512" height="512" rx="%(r).0f" fill="%(bg)s"/>
<rect x="18" y="18" width="476" height="476" rx="%(r2).0f" fill="none" stroke="%(ac)s" stroke-width="10" opacity=".35"/>
<path d="M256 96 L432 236 L400 236 L400 404 L112 404 L112 236 L80 236 Z"
      fill="none" stroke="%(ac)s" stroke-width="22" stroke-linejoin="round"/>
<text x="256" y="344" text-anchor="middle" font-family=%(f)s font-size="150"
      font-weight="700" letter-spacing="6" fill="%(ac)s">GA</text>
</svg>""" % {"s": size, "r": r, "r2": r * 0.85, "bg": BG, "ac": ACCENT, "f": '"%s"' % SANS}


def og_svg(questions, terms):
    # Drawn on a 1200x1200 square with the card centred in it: qlmanage always
    # renders to a square thumbnail, so letterbox here and crop the band back
    # out afterwards rather than fighting its scaling.
    return """<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="1200" viewBox="0 0 1200 1200">
<rect width="1200" height="1200" fill="%(bg)s"/>
<g transform="translate(0,285)">
<rect x="0" y="0" width="1200" height="8" fill="%(ac)s"/>
<g transform="translate(88,104) scale(.215)">
  <path d="M256 96 L432 236 L400 236 L400 404 L112 404 L112 236 L80 236 Z"
        fill="none" stroke="%(ac)s" stroke-width="30" stroke-linejoin="round"/>
</g>
<text x="212" y="186" font-family=%(f)s font-size="34" font-weight="700"
      letter-spacing="8" fill="%(dim)s">GEORGIA REAL ESTATE</text>
<text x="92" y="318" font-family=%(f)s font-size="94" font-weight="700"
      letter-spacing="-1" fill="%(ink)s">Pass the salesperson</text>
<text x="92" y="418" font-family=%(f)s font-size="94" font-weight="700"
      letter-spacing="-1" fill="%(ac)s">exam. Free.</text>
<rect x="92" y="470" width="1016" height="1" fill="%(dim)s" opacity=".3"/>
<text x="92" y="534" font-family=%(f)s font-size="34" font-weight="500"
      fill="%(dim)s">%(q)s practice questions  &#183;  %(t)s defined terms  &#183;  worked math  &#183;  no signup</text>
<text x="92" y="586" font-family=%(f)s font-size="27" font-weight="600"
      letter-spacing="2" fill="%(br)s">imoveflow3.github.io/ga-realestate-prep</text>
</g>
</svg>""" % {"bg": BG, "ac": ACCENT, "ink": INK, "dim": DIM, "br": BRASS,
             "f": '"%s"' % SANS, "q": questions, "t": terms}


def render(svg, path, width, height):
    """Rasterise one SVG. qlmanage pads to a square, so crop back afterwards."""
    box = max(width, height)   # what qlmanage will actually produce
    tmp = tempfile.mkdtemp()
    try:
        src = os.path.join(tmp, "card.svg")
        with open(src, "w") as f:
            f.write(svg)
        subprocess.check_call(["qlmanage", "-t", "-s", str(box), "-o", tmp, src],
                              stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        made = os.path.join(tmp, "card.svg.png")
        if not os.path.exists(made):
            raise SystemExit("qlmanage did not rasterise %s" % path)
        if (width, height) != (box, box):
            subprocess.check_call(["sips", "-c", str(height), str(width), made],
                                  stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        shutil.move(made, path)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    got = subprocess.check_output(["sips", "-g", "pixelWidth", "-g", "pixelHeight", path])
    print("  %-22s %s" % (os.path.basename(path),
                          b" ".join(got.split()[-3:]).decode().replace("pixelHeight:", "x")))


def main():
    if sys.platform != "darwin":
        raise SystemExit("this renderer needs macOS (qlmanage + sips); "
                         "the PNGs it makes are committed, so just use those")
    if not os.path.isdir(OUT):
        os.makedirs(OUT)
    import json
    study = json.load(open(os.path.join(HERE, "greprep", "banks", "study.json")))
    terms = sum(len(t["vocab"]) for t in study["topics"].values())
    written = 0
    for name in ("national", "georgia", "comprehensive"):
        written += len(json.load(open(os.path.join(HERE, "greprep", "banks",
                                                   name + ".json"))))
    print("rendering into docs/assets")
    for size in (192, 512, 180):
        render(icon_svg(size), os.path.join(OUT, "icon-%d.png" % size), size, size)
    render(og_svg(written, terms), os.path.join(OUT, "card.png"), 1200, 630)


if __name__ == "__main__":
    main()
