from http.server import BaseHTTPRequestHandler, HTTPServer
import json

f = open('data.json')
data = json.load(f)


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        content = data
        self.wfile.write(bytes(json.dumps(content), "utf8"))


with HTTPServer(('', 8000), handler) as server:
    server.serve_forever()

