import requests
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        print('Hello, world!')
        response = requests.get('https://intagpt.onrender.com/')
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(response.text.encode('utf-8'))
        return
