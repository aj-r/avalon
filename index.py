import os
from socketserver import ThreadingMixIn
from http.server import HTTPServer, BaseHTTPRequestHandler
from threading import Thread

class Handler(BaseHTTPRequestHandler):
    def do_GET(s):
        s.send_response(200)
        s.send_header("Content-type", "text/plain")
        s.end_headers()
        s.wfile.write(bytes("Hello World!", "UTF-8"))

class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True

def serve_on_port(port):
    server = ThreadingHTTPServer(("", int(port)), Handler)
    server.serve_forever()

port = os.getenv("PORT") if os.getenv("PORT") is not None else 80

Thread(target=serve_on_port, args=[port]).start()

exec(open("dreamlord.py").read())