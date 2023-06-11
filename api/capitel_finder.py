from http.server import BaseHTTPRequestHandler
import requests
from urllib import parse



class handler(BaseHTTPRequestHandler):
 
  def do_GET(self):
     
    #  fas => function as server 
    s = self.path
    url_components = parse.urlsplit(s)
    query_strings_list = parse.parse_qsl(url_components.query)
    dic = dict(query_strings_list)
    country = dic.get("country")
    capital = dic.get("capital")

    if capital:
      url ="https://restcountries.com/v3.1/capital/"
      res = requests.get(url+capital)
      data = res.json()
      res = data[0]["name"]["common"]
      res2 = f"{capital} is the capital of {res}.."
    elif country:
      url ="https://restcountries.com/v3.1/name/"
      res = requests.get(url+country)
      data = res.json()
      res = data[0]["capital"][0]
      res2 = f"The capital of {country} is {res}"


    self.send_response(200)
    self.send_header('Content-type', 'text/plain')# mata data
    self.end_headers()
    self.wfile.write(res2.encode())# encode its kind of scurity 
    return