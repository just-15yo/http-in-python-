from http.server import HTTPServer, BaseHTTPRequestHandler

host = '192.168.8.87'     
port = 8000             

class KhaledHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write('<html><body><h2>that is the sign khaled</h2></body></html>'.encode('utf-8'))

server = HTTPServer((host, port), KhaledHandler)
print('khaled server is running')
try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
server.server_close()
print('server is closed')
print('khaled2011__omhkK')