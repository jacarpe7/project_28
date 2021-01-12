import serial

# This script uses the hardware build in folder qt7-ascii-out-dylan

# Need to define port according to your setup. Typical port name - Windows: 'COM3'  Mac: '/dev/tty.usbmodem12345'
serialPort = serial.Serial(port='COM3',baudrate=38400,bytesize=8,timeout=2,stopbits=serial.STOPBITS_ONE)

# define sample object to hold data
class Row:
    def __init__(row, time, delta0, delta1, delta2, delta3, delta4):
        row.time = time
        row.delta0 = delta0
        row.delta1 = delta1
        row.delta2 = delta2
        row.delta3 = delta3
        row.delta4 = delta4

# array to hold objects
list = []
bigList = []
index  = 0
while(1):
    
    # discard first line
    serialPort.readline()
    
    print("Ready to record gesture.")
    # values to be compared, once one hits 40, recording will start
    val0 = 0
    val1 = 0
    val2 = 0
    val3 = 0
    val4 = 0
    i = 0
    
    #read in data from serial, set to 50 lines
    while val0 < 40 and val1 < 40 and val2 < 40 and val3 < 40 and val4 < 40 :
        parseLine = serialPort.readline().decode('utf-8').split(",")
        list.append(Row(i,parseLine[1],parseLine[2],parseLine[3],parseLine[4],parseLine[5]))
        i = i + 1
        for obj in list:
            val0 = int(obj.delta0)
            val1 = int(obj.delta1)
            val2 = int(obj.delta2)
            val3 = int(obj.delta3)
            val4 = int(obj.delta4)
        
    list.clear()
    for x in range(50):
        # parse readline() into array, can be easily placed into other objects if wanted
        parseLine = serialPort.readline().decode('utf-8').split(",")
        # time component is discarded and replaced with x variable increment; time output is 8-bit and resets after 255
        list.append(Row(x,parseLine[1],parseLine[2],parseLine[3],parseLine[4],parseLine[5]))
        
    index = index + 1
    print("Gesture #", str(index), " recorded and written.")
    bigList.append(list)

serialPort.close()
print("All gestures recorded.  Program complete.")