import MySQLdb
from MySQLdb.constants import FIELD_TYPE
import json

def fetch(db):
  db.query("""SELECT * FROM itemtype """)
  r = db.store_result()
  rResult = r.fetch_row()
  arResults = []
  while len(rResult) >0:
    arResults.append(rResult)
    rResult = r.fetch_row()
  return json.dumps(arResults)


