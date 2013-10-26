import MySQLdb
# what does a donation need to do?
# new donation, add items, user date 

def insert_donation(db, dJS):
  #{user_email, locationid, dropoffdate, itemids:{ {itemtypeid, qty, size} ,... }}
  #dJSONDonation # needs to have, blah blah blah 
  sUserEmail = dJS.get('user_email')
  if sUserEmail == None:
    sUserEmail = 'default@gmail.com'
 
  db.query('select id from person where email = "' + dJS.get('user_email') + '";')
  rResult = db.store_result()
  rRow = rResult.fetch_row()
  nID = -1
  if len(rRow) != 0:
    nID = rRow[0][0] # this is the user id to use for insert 
    print('found user')
  else: 
    rResult = db.query('select max(id) + 1 from person')
    rRow = rResult.fetch_row()
    nID = rRow[0][0]

    sQuery = 'insert into person (id, name, phone, email, password, loc_id, is_activated) values (' 
    sQuery += str(nID) 
    sQuery += ', "annon'
    sQuery += str(niD)
    sQuery += '" , NULL ,' 
    sQuery += str(dJS.get('user_email')) 
    sQuery += ',"abc123" , ' 
    if dJS.get('location_id') == None:
      sQuery += 1 
    else:
      sQuery += dJS.get('location_id') 
    sQuery += ', 1);'
    print('inserting person')
    rResult = db.query(sQuery)
    #check state of db here. 
      
    db.query('insert into donor values(' + str(rRow.val()) + ')')
  #now we know we have a user ... nRow.val is user id
  for dSet in dJS.get('itemids'):
    print('got into add items')
    nQty = 0
    while nQty < dSet.get('qty'):
      print('made into generate insert')
      sInsertItemQuery = 'INSERT INTO `swapbot`.`donation` (`id`, `item_id`, `size`, `donor_id`, `state`) VALUES (NULL, '
      sInsertItemQuery += str(dSet.get('itemtypeid')) 
      sInsertItemQuery += ', "' 
      sInsertItemQuery += str(dSet.get('size')) 
      sInsertItemQuery += '", "'
      sInsertItemQuery += str(rRow[0][0]) + '", "open");'     
      db.query(sInsertItemQuery)
      nQty += 1
  # items are in the donation table. 
  # ... location match? 
  db.commit()
  return ''
