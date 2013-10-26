import MySQLdb

def fetch():
  
  db = MySQLdb.connect(host="localhost", # your host, usually localhost
                       user="swapbot", # your username
                       passwd="swappass", # your password
                       db="swapbot") # name of the data base
  db.query("""SELECT * FROM items """)
  return 

