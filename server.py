#!/usr/bin/env python3
"""SyncPrompt local server with Notion API proxy."""

import json
import ssl
import urllib.request
import urllib.error
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse

# macOS Python 3.12 often lacks certificates — use unverified context
# This is safe here: we only proxy to api.notion.com on localhost
SSL_CTX = ssl.create_default_context()
SSL_CTX.check_hostname = False
SSL_CTX.verify_mode = ssl.CERT_NONE

PORT = 8080
NOTION_BASE = "https://api.notion.com/v1"


class SyncPromptHandler(SimpleHTTPRequestHandler):
    def do_OPTIONS(self):
        """Handle CORS preflight."""
        self.send_response(200)
        self._cors_headers()
        self.end_headers()

    def do_GET(self):
        if self.path.startswith("/api/notion/"):
            self._proxy_notion("GET")
        else:
            super().do_GET()

    def do_POST(self):
        if self.path.startswith("/api/notion/"):
            self._proxy_notion("POST")
        else:
            self.send_error(404)

    def _proxy_notion(self, method):
        notion_path = self.path[len("/api/notion/"):]
        url = f"{NOTION_BASE}/{notion_path}"

        # Read request body for POST
        body = None
        if method == "POST":
            length = int(self.headers.get("Content-Length", 0))
            if length > 0:
                body = self.rfile.read(length)

        # Forward relevant headers
        headers = {
            "Notion-Version": self.headers.get("Notion-Version", "2022-06-28"),
            "Content-Type": "application/json",
        }
        auth = self.headers.get("Authorization")
        if auth:
            headers["Authorization"] = auth

        req = urllib.request.Request(url, data=body, headers=headers, method=method)

        try:
            with urllib.request.urlopen(req, context=SSL_CTX) as resp:
                data = resp.read()
                self.send_response(resp.status)
                self._cors_headers()
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(data)
        except urllib.error.HTTPError as e:
            data = e.read()
            self.send_response(e.code)
            self._cors_headers()
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(data)

    def _cors_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Authorization, Content-Type, Notion-Version")

    def log_message(self, format, *args):
        # Only log API requests, not static files
        if "/api/" in (args[0] if args else ""):
            super().log_message(format, *args)


if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", PORT), SyncPromptHandler)
    print(f"SyncPrompt server running at http://localhost:{PORT}")
    print("Press Ctrl+C to stop\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        server.server_close()
