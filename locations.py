import jsonify_db_result

def fetch(db, path):
  db.query("""SELECT * FROM location inner join open_hors on location.id = open_hors.loc_id """)
  r = db.store_result()
  return jsonify_db_result.proc(r)
