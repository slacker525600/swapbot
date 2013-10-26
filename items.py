import MySQLdb
from MySQLdb.constants import FIELD_TYPE
import json

def fetch():
  my_conv = { FIELD_TYPE.LONG: int }
  db = MySQLdb.connect(host="localhost", # your host, usually localhost
                       user="swapbot", # your username
                       passwd="swappass", # your password
                       db="swapbot",
                       conv=my_conv) # name of the data base
  #Generally speaking, putting passwords in your code is not such a good idea:
  #db=_mysql.connect(host="outhouse",db="thangs",read_default_file="~/.my.cnf")                       
  db.query("""SELECT * FROM items """)
  r = db.store_result()
  rResult = r.fetch_row()
  sToReturn = ''
  while rResult != Null:
    sToReturn += json.dump(rResult)
  return sToReturn

