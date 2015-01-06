import MySQLdb
import serial

def dbWrite(_id):
    conn = MySQLdb.connect('localhost',user='root',passwd='chao',db='doorlock')
    cur = conn.cursor()
    queryname = 'select name from memberinfo where id=' + "\'" + _id + "\'"
    cur.execute(queryname)
    name = "%s" % cur.fetchone()
    print name
    ll = "%s,%s" % (_id,name)
    print ll
    writestr = "insert into checktime values('%s','%s',now())" % (_id,name)
    print writestr
    cur.execute(writestr)
    cur.close()
    conn.commit()
    conn.close()

if __name__ == '__main__':
    id = 'A2 EA E5 1F 00 BE 00'
    dbWrite(id)
