import jsonify_db_result

def fetch(db, path):
  sLocation = '' # path[8:-4] 
  # need to figure out how to pull this from path, pass as added parameter
  #goal is to list the incoming donations waiting to be received today at this location 
  db.query("""SELECT * 
           FROM donation 
           inner join donor on donation.donor_id = donor.id 
           inner join person on donor.id = person.id
           inner join location on location.id = donor.loc_id and location.id = '""" + sLocation + """'
           group by donor.id """)
  #this seems way too complicated, am I doing something wrong?
  r = db.store_result()
  return jsonify_db_result.proc(r)
