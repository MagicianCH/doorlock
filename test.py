import serial
import time
import MySQLdb


def dbQuerry(_id):
    conn = MySQLdb.connect('localhost', user='root', passwd='chao', db='doorlock')
    cur = conn.cursor()
    queryStr = 'select id from memberinfo where id=' + "\'" + _id + "\'"
    queryname = 'select name from memberinfo where id=' + "\'" + _id + "\'"
    flag = cur.execute(queryStr)
    if flag != 0:
        cur.execute(queryname)
        name = cur.fetchone()
        print "name: %s" % name
        return 1
    else:
        return 0

def dbWrite(_id):
    conn = MySQLdb.connect('localhost',user='root',passwd='chao',db='doorlock')
    cur = conn.cursor()
    queryname = 'select name from memberinfo where id=' + "\'" + _id + "\'"
    cur.execute(queryname)
    name = "%s" % cur.fetchone()
    writestr = "insert into checktime values('%s','%s',now())" % (_id,name)
    print writestr
    cur.execute(writestr)
    cur.close()
    conn.commit()
    conn.close()


if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 115200)
    print ser.portstr

    while True:
        data = ser.read(20)
        result = dbQuerry(data)

        if result == 1:
            ser.write('\x01')
            print "id: " + data
            dbWrite(data)
            result = 0
        else:
            ser.write('\x02')
            print 'no'
            result = 0
        ser.flush()
        time.sleep(1)
