fFile = open('salvation_army_item_types.csv', 'r')
asLines = fFile.readlines()
fFile.close()

fOut = open('item_sql.sql', 'w')
nRowOn = 1

for sLine in asLines:
  # mens/womens/childrens, type, min, max, include
  asFields = sLine.split(',')
  if asFields[-1] != '0':
    #id item mwc imagepath estimated price 
    fOut.write('insert into itemtype values (' + str(nRowOn) + ',"' + asFields[1] +'","' + asFields[0][0]+'","image/'+asFields[1] +
       '.jpg",' + str((float(asFields[2][1:]) + float(asFields[3][1:])) / 2)  + ');\n')
    nRowOn += 1

fOut.close()
