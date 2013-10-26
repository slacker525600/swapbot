import MySQLdb

import items


class json_handler():
  #perform db query / validation here 
  def handle_json(self, path):
    if 'items' in path:
      return items.fetch()
      
    return "hello world"
    db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="swapbot", # your username
                      passwd="swappass", # your password
                      db="swapbot") # name of the data base
    
    return 

