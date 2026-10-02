# -*- coding: utf-8 -*-
"""The handful of real-world facts the build cannot work out for itself.

Everything here is something only the owner of the site knows: where it
lives, who answers the support mail, what it costs. They used to be spelled
out in three different files, each with its own placeholder, which is how a
site ends up shipping with support@example.com in its footer.

Edit this file, or set the matching environment variable, and run the build.
Anything still left at a placeholder is reported loudly by check(), and the
build refuses to produce a public page with a fake address in it unless you
ask for a draft on purpose.
"""

import os

# Where the paid site is served from. A Cloudflare Worker is published at
# <name>.<subdomain>.workers.dev until a real domain is pointed at it, so this
# stays a placeholder until the first deploy tells us the truth.
PAID_SITE = os.environ.get("GA_PAID_SITE", "").strip()

# The free, public study tool on GitHub Pages. This one is already real.
FREE_SITE = os.environ.get(
    "GA_FREE_SITE", "https://imoveflow3.github.io/ga-realestate-prep/").strip()

# The address a buyer writes to when something goes wrong. It appears in the
# footer of every page, in the terms, and in the privacy policy as the way to
# have an account deleted -- so it has to be an address somebody reads.
SUPPORT_EMAIL = os.environ.get("GA_SUPPORT_EMAIL", "").strip()

# One payment, in cents.
PRICE_CENTS = int(os.environ.get("GA_PRICE_CENTS", "1900"))

# The legal entity behind the site, as it should appear in the terms. A sole
# trader can put their own name here.
OPERATOR = os.environ.get("GA_OPERATOR", "").strip()


PLACEHOLDER = "— not set —"


def _missing():
    out = []
    if not PAID_SITE:
        out.append(("GA_PAID_SITE", "the address the paid site is served from",
                    "https://ga-prep.<your-subdomain>.workers.dev/"))
    if not SUPPORT_EMAIL:
        out.append(("GA_SUPPORT_EMAIL", "the address support mail goes to",
                    "help@yourdomain.com"))
    if not OPERATOR:
        out.append(("GA_OPERATOR", "who is legally behind the site",
                    "Your Name"))
    return out


def check(strict=False):
    """Report anything still unset. With strict, refuse to build.

    The build is allowed to run unconfigured on purpose: it is how the site
    gets looked at before it is bought a domain. What it may not do is run
    unconfigured *quietly*.
    """
    missing = _missing()
    if not missing:
        return True
    print("")
    print("  NOT READY TO PUBLISH — %d thing%s still unset:"
          % (len(missing), "" if len(missing) == 1 else "s"))
    for var, what, example in missing:
        print("    %-18s %s" % (var, what))
        print("    %-18s e.g. %s" % ("", example))
    print("")
    print("  Set them in tools/siteconfig.py, or for one build:")
    print("    %s python3 tools/build_paid.py"
          % " ".join("%s='%s'" % (v, e) for v, _, e in missing))
    print("")
    if strict:
        raise SystemExit("refusing to build a public site with placeholders in it")
    print("  Building anyway, with placeholders. Do not publish this.")
    print("")
    return False


def support_email():
    """What to print where a support address belongs."""
    return SUPPORT_EMAIL or PLACEHOLDER


def paid_site():
    """Always ends in a slash, so joining a path is never a guess."""
    s = PAID_SITE or "https://example.invalid/"
    return s if s.endswith("/") else s + "/"


def operator():
    return OPERATOR or PLACEHOLDER


def configured():
    return not _missing()
