#import MySQLdb

import items
import location_swaps
import locations
import users


class json_handler():
  #perform db query / validation here 
  def handle_json(self, path):
    my_conv = { FIELD_TYPE.LONG: int }
    db = MySQLdb.connect(host="localhost", # your host, usually localhost
                       user="swapbot", # your username
                       passwd="swappass", # your password
                       db="swapbot",
                       conv=my_conv) # name of the data base    #could handle db connection here as opposed to opening it in each subclass.
    #passwords in code not a good idea:
    #db=_mysql.connect(read_default_file="~/.my.cnf") but whatever.
    if 'items' in path:
      return items.fetch(db)
    elif 'location_swaps' in path:
      return location_swaps.fetch(db,path) #need to pass location to handle
    elif 'locations' in path:
      return locations.fetch(db,path) #return locations relevant to the logged in user
    elif 'user_info' in path:
      #user page? show donations that have been matched and received and distributed, current status of all
      return users.fetch(db, path)
    elif '?' == Null:
      #what other cases do we need to handle?
      return Null
    return "hello world"
    
    return 

