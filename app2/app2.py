from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        data = self.rfile.read(content_length)
        data = json.loads(data.decode("utf-8"))

        # Process the data received from App1
        print("App2 received data from App1:", data)

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        message = "Data received and processed by App2!"
        self.wfile.write(message.encode("utf-8"))

def run(server_class=HTTPServer, handler_class=SimpleRequestHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print("Starting App2 on port", port)
    httpd.serve_forever()

run()