import serial
import time

ser = serial.Serial('/dev/ttyUSB0','115200')

while True:
    data = ser.read(20)
    print data
    ser.flush()
    time.sleep(1)
