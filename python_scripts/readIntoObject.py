import serial

# This script uses the hardware build in folder qt7-ascii-out-dylan

# Asks if the user would like to change the threshold
print("Would you like to change the delta threshold from the default value? Y or N")
answer = input()
if (answer == "Y"):
    print("What would you like the delta to be?")
    customThresh = int(input())
else:
    customThresh = 40

print("Do you want to change the length of the recording from the default value? Y or N");
answer = input()
if (answer == "Y"):
    print("How long would you like the length to be (default is 50)?")
    customLength = int(input())
else:
    customThresh = 50

# Asks user how many recordings to make
print("How many gesture records would you like to make? ")
amount = int(input())

# Asks what the file should be called
print("What would you like the files to be called?")
fname = str(input())
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

for index in range(amount):
    # setup filewriting to CSV
    filename = fname + "%s.csv" % index
    f = open(filename, "w")
    headers = "time,delta0,delta1,delta2,delta3,delta4\n"
    f.write(headers)
    
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
    while val0 < customThresh and val1 < customThresh and val2 < customThresh and val3 < customThresh and val4 < customThresh :
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
    
    # write to CSV
    for obj in list:
        f.write(str(obj.time) + "," + str(obj.delta0) + "," + str(obj.delta1) + "," + str(obj.delta2) + "," + str(obj.delta3) + "," + str(obj.delta4) + ",\n")
        
    print("Gesture #", str(index), " recorded and written.")
f.close()
serialPort.close()
print("All gestures recorded.  Program complete.")