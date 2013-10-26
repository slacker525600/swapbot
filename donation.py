import 
# what does a donation need to do?
# new donation, add items, user date 

def insert_donation(db, dJS):
  {user_email, locationid, dropoffdate, itemids:{ {itemtypeid, qty, size} ,... }}
  dJSONDonation # needs to have, blah blah blah 
  sUserEmail = dJS.get('user_email')
  if sUserEmail == None:
    sUserEmail = 'default@gmail.com'
 
  rResult = db.query('select id from person where email = "' + dJS.get('user_email') + '";')
  rRow = rResult.fetch_row()
  if len(rRow) != 0:
    rRow.val() # this is the user id to use for insert 
  else: 
    rResult = db.query('select max(id) + 1 from person')
    rRow = rResult.fetch_row()

    sQuery = 'insert into person (id, name, phone, email, password, loc_id, is_activated) values (' 
    sQuery += str(rRow.val) 
    sQuery += ', "annon'
    sQuery += str(rRow.val)
    sQuery += '" , NULL ,' 
    sQuery += str(dJS.get('user_email')) 
    sQuery += ',"abc123" , ' 
    sQuery += dJS.get('location_id') == None ? 1: dJS.get('location_id') 
    sQuery += ', 1);'
    rResult = db.query(sQuery)
    #check state of db here. 
      
    db.query('insert into donor values(' + str(rRow.val()) + ')')
  #now we know we have a user ... nRow.val is user id
  for dSet in dJS.get(itemids):
    nQty = 0
    while nQty < dSet.get('qty'):
      sInsertItemQuery = 'INSERT INTO `swapbot`.`donation` (`id`, `item_id`, `size`, `donor_id`, `state`) VALUES (NULL, '
      sInsertItemQuery += dSet.get('itemtypeid') 
      sInsertItemQuery += ', "' 
      sInsertItemQuery += dSet.get('size') 
      sInsertItemQuery += '", "'
      sInsertItemQuery += rRow.val() + '", "open");'     
      db.query(sInsertItemQuery)
      nQty += 1
    
  return ''
