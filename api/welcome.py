from http.server import BaseHTTPRequestHandler

 
class handler(BaseHTTPRequestHandler):
 
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    message = "Welcome to Python course"
    self.wfile.write(message.encode())
    return