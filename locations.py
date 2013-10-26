import jsonify_db_result

def fetch(db, path):
  db.query("""SELECT * FROM locations """)
  r = db.store_result()
  return jsonify_db_result.proc(r)
