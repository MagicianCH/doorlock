import MySQLdb
import serial
import time
import string

def dbWrite(_id,name):
    conn = MySQLdb.connect('localhost',user='root',passwd='chao',db='doorlock')
    cur = conn.cursor()

#    queryname = 'select name from memberinfo where id=' + "\'" + _id + "\'"
#    cur.execute(queryname)
#    name = "%s" % cur.fetchone()
#    print name
#    ll = "%s,%s" % (_id,name)
#   print ll
    writestr = "insert into test values('%s','%s')" % (_id,name)
    print writestr
    cur.execute(writestr)
    cur.close()
    conn.commit()
    conn.close()

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0','115200')
    while True:
        length = ser.read(1)
        len = string.atoi(length)
        data = ser.read(20+len)
        print data
        id = data[0:20]
        name = data[21:(20+len)]
        print name
        dbWrite(id,name)

        ser.flushInput()
        time.sleep(1)

