import serial
import time
import MySQLdb

ser = serial.Serial('/dev/ttyUSB0',115200)
'''
n = ser.write('hello world')
print ser.portstr
'''
while True:
#    ser.write('hello')
#    time.sleep(3)
    data = ser.read(20)
    print data
    if data[0] == 'A':
        ser.write('yes')
    else:
        print 'world'
    ser.flush()
    time.sleep(1)
