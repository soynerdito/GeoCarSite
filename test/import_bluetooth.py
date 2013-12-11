import serial
import Queue
import threading
import urllib2
import sys
import struct

from time import sleep
from serial import Serial, EIGHTBITS,SEVENBITS, STOPBITS_ONE, PARITY_NONE

def whatisthis(s):
    if isinstance(s, str):
        print "ordinary string"
    elif isinstance(s, unicode):
        print "unicode string"
    else:
        print "not a string"
        
        
        
#define a worker function
def read_serial(queue, ser):
    queue_full = True
    ser.write('B');    
    while queue_full:
        #get your data off the queue, and do some work            
        #add to queue
        data = ser.read( ser.inWaiting()  )
        if len(data) > 0 :
            #whatisthis(data)            
            queue.put(data)
        #if data :                
        #    queue.put(data)        


port = "COM6"
#ser = Serial(port, baudrate=9600, 
#            bytesize=EIGHTBITS, parity=PARITY_NONE, stopbits=STOPBITS_ONE,xonxoff=0, timeout=4)
ser = serial.Serial(port,
                   baudrate=9600,
                   bytesize=serial.EIGHTBITS,
                   parity=serial.PARITY_NONE,
                   stopbits=serial.STOPBITS_ONE,
                   timeout=4,
                   xonxoff=False,
                   rtscts=False,
                   writeTimeout=None,
                   dsrdtr=False,
                   interCharTimeout=None)
                   
#ser = serial.Serial(port, 9600, timeout=0)

#load up a queue with your data, this will handle locking
q = Queue.Queue()

#create as many threads as you want
thread_count = 5
#start thread for reading COM Port
t = threading.Thread(target=read_serial, args = (q,ser))
t.start()

f = open('GPS.txt','w')
while True:
    try:
        #get your data off the queue, and do some work
        data = q.get(False)
        if len(data)>1:
            f.write(data.replace('\0', ''))            
            sys.stdout.write(data.replace('\0', ''))
            f.flush();
    except Queue.Empty:
        continue
        #queue_full = False
f.close()
#while True:
#    data = ser.read(size=100)
#    if len(data) > 0:
#        print data
#ser.close()
