import http.server
import socketserver
import os

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/reportcode':
            self.path = '/pylint_report.txt'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Generate the pylint report
os.system("pylint --rcfile=/app/.pylintrc /app/app.py > /app/pylint_report.txt || true")

# Serve the pylint report
PORT = 5000
with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print("Serving HTTP on port", PORT)
    httpd.serve_forever()

