import SocketServer 
import CGIHTTPServer 
import urllib2

import shutil
import datetime

from json_handler import json_handler

PORT = 8080

class Proxy(CGIHTTPServer.CGIHTTPRequestHandler):
  def do_GET(self):
    #think I just need this below
    if 'json' in self.path:
      #handle json request here 
      handler = json_handler() 
      self.wfile.write( handler.handle_json(self.path) )
    else:
      fFileToServe = open(self.path[1:] ,'r') #urllib removed front / urllib 2 gives it thus starting at 1
      self.copyfile(fFileToServe, self.wfile)
      fFileToServe.close()
    return
  def do_POST(self):
    self.wFile.write("posting")


httpd = SocketServer.ForkingTCPServer(('', PORT), Proxy)
print "serving at port", PORT
httpd.serve_forever()

