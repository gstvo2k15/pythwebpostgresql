import http.server
import socketserver
import os

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/reportcode':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            with open("/app/pylint_report.txt", "r") as file:
                self.wfile.write(file.read().encode())
        else:
            self.send_response(404)
            self.end_headers()

# Generate the pylint report
os.system("autopep8 --in-place --aggressive --aggressive /app/app.py")
os.system("pylint --rcfile=/app/.pylintrc /app/app.py > /app/pylint_report.txt || true")

# Serve the pylint report
PORT = 5000
with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print("Serving HTTP on port", PORT)
    httpd.serve_forever()
