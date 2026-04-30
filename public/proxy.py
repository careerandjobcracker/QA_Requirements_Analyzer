#!/usr/bin/env python3
"""
QA Analyzer — Local Proxy Server
Forwards streaming requests to api.anthropic.com, adding CORS headers
so the HTML widgets can call it from the browser.

Usage:
  python3 proxy.py --key sk-ant-YOUR_KEY_HERE
  python3 proxy.py --key sk-ant-YOUR_KEY_HERE --port 8787

Then open any widget HTML file in your browser.
The widget will automatically send requests to http://localhost:8787/proxy
"""

import argparse
import http.server
import json
import urllib.request
import urllib.error
import sys

PORT = 8787
ANTHROPIC_URL = "https://api.anthropic.com/v1/messages"
ANTHROPIC_VERSION = "2023-06-01"

class ProxyHandler(http.server.BaseHTTPRequestHandler):

    def log_message(self, fmt, *args):
        # Suppress default server log spam; print our own cleaner version
        pass

    def send_cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers",
                         "Content-Type, x-api-key, anthropic-version")

    # ── Handle preflight (OPTIONS) ────────────────────────────────────────
    def do_OPTIONS(self):
        self.send_response(204)
        self.send_cors()
        self.end_headers()

    # ── Health-check (GET) ────────────────────────────────────────────────
    def do_GET(self):
        if self.path in ("/", "/health"):
            body = json.dumps({"status": "ok", "proxy": "QA Analyzer proxy"}).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_cors()
            self.end_headers()
            self.wfile.write(body)
        else:
            self.send_response(404)
            self.end_headers()

    # ── Main proxy (POST) ─────────────────────────────────────────────────
    def do_POST(self):
        if self.path != "/proxy":
            self.send_response(404)
            self.end_headers()
            return

        # Read request body
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length)

        # Forward to Anthropic with streaming
        req = urllib.request.Request(
            ANTHROPIC_URL,
            data=body,
            headers={
                "Content-Type": "application/json",
                "x-api-key": API_KEY,
                "anthropic-version": ANTHROPIC_VERSION,
            },
            method="POST",
        )

        try:
            with urllib.request.urlopen(req) as upstream:
                self.send_response(200)
                self.send_header("Content-Type", "text/event-stream")
                self.send_header("Cache-Control", "no-cache")
                self.send_header("Transfer-Encoding", "chunked")
                self.send_cors()
                self.end_headers()

                # Stream chunks straight through to the browser
                while True:
                    chunk = upstream.read(1024)
                    if not chunk:
                        break
                    try:
                        self.wfile.write(chunk)
                        self.wfile.flush()
                    except BrokenPipeError:
                        break

        except urllib.error.HTTPError as e:
            err_body = e.read()
            self.send_response(e.code)
            self.send_header("Content-Type", "application/json")
            self.send_cors()
            self.end_headers()
            self.wfile.write(err_body)
            print(f"  [proxy] Anthropic error {e.code}: {err_body[:200]}")

        except urllib.error.URLError as e:
            msg = json.dumps({"error": {"message": str(e)}}).encode()
            self.send_response(502)
            self.send_header("Content-Type", "application/json")
            self.send_cors()
            self.end_headers()
            self.wfile.write(msg)
            print(f"  [proxy] Network error: {e}")


def main():
    global API_KEY

    parser = argparse.ArgumentParser(description="QA Analyzer local proxy")
    parser.add_argument("--key", required=True,
                        help="Your Anthropic API key (sk-ant-...)")
    parser.add_argument("--port", type=int, default=PORT,
                        help=f"Port to listen on (default: {PORT})")
    args = parser.parse_args()

    API_KEY = args.key

    if not API_KEY.startswith("sk-"):
        print("ERROR: API key should start with 'sk-'. Check your key and try again.")
        sys.exit(1)

    server = http.server.HTTPServer(("127.0.0.1", args.port), ProxyHandler)
    print(f"\n  QA Analyzer proxy running on http://127.0.0.1:{args.port}")
    print(f"  API key: {API_KEY[:12]}{'*' * 8}  (masked)")
    print(f"\n  Now open any widget HTML file in your browser.")
    print(f"  Press Ctrl+C to stop.\n")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n  Proxy stopped.")


if __name__ == "__main__":
    main()
