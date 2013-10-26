import jsonify_db_result

def fetch(db, path):
  sUserID = '' 
  #id from path
  db.query("""SELECT * FROM  """)
  r = db.store_result()
  return jsonify_db_result.proc(r)
