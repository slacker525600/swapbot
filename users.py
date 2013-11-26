import jsonify_db_result

class user(object):
  def __str__(self):
    return self


def fetch(db, path):
  sUserID = '' 
  #id from path
  db.query("""SELECT * FROM  """)
  r = db.store_result()
  return jsonify_db_result.proc(r)
