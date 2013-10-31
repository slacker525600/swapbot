import jsonify_db_result
import json

class item(object):
  id = ''
  item = ''
  mwc = ''
  imagePath = ''
  estimatedPrice = 0
  def set_fields(sJSON):
    dJSONDict = json.loads(sJSON)
    self.id = dJSONDict.get('id')
    self.item = dJSONDict.get('item')
    self.mwc = dJSONDict.get('mwc')
    self.imagePath = dJSONDict.get('imagePath')
    self.estimatedPrice = dJSONDict.get('estimatedPrice')
    return self
  
  #item = json.load(string param)

  
def fetch(db):
  db.query("""SELECT * FROM itemtype """)
  r = db.store_result()
  return jsonify_db_result.proc(r)


