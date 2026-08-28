#!/usr/bin/env bash
# Start the Georgia real estate study app. Open http://localhost:8778 when it prints.
cd "$(dirname "$0")" && exec python3 server.py
