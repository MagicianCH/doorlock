import MySQLdb

db = MySQLdb.connect('localhost',user = 'root',passwd = 'chao',db = 'doorlock')
cur = db.cursor()

idcolum = 'A2 C3 8D 98 00 CC 00'
qurry = "select id from doorlock where id="+"\'"+idcolum+"\'"

#print(qurry)

if cur.execute(qurry) == 0:
   print "querry OK"
else:
   print "NOT FOUND"
