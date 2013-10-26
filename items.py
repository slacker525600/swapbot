import jsonify_db_result

def fetch(db):
  db.query("""SELECT * FROM itemtype """)
  r = db.store_result()
  return jsonify_db_result.proc(r)


