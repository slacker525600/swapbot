import MySQLdb
from MySQLdb.constants import FIELD_TYPE
import json

def fetch(db):
  #Generally speaking, putting passwords in your code is not such a good idea:
  #db=_mysql.connect(host="outhouse",db="thangs",read_default_file="~/.my.cnf")                       
  db.query("""SELECT * FROM itemtype """)
  r = db.store_result()
  rResult = r.fetch_row()
  sToReturn = ''
  while len(rResult) >0:
    sToReturn += json.dumps(rResult)
    rResult = r.fetch_row()
  return sToReturn

