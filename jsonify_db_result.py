import json

def proc(r):
  rResult = r.fetch_row()
  arResults = []
  while len(rResult) > 0:
    arResults.append(rResult)
    rResult = r.fetch_row()
  return json.dumps(arResults)
