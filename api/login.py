from http.server import BaseHTTPRequestHandler
class handler(BaseHTTPRequestHandler):
 
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')# mata data
    self.end_headers()
    mas='welcome to pyton'
    self.wfile.write(mas.encode())# encode its kind of scurity 
    #  fas => function as server 
    return