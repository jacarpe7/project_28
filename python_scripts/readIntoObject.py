import serial

# This script uses the hardware build in folder qt7-ascii-out-dylan

# Need to define port according to your setup. Typical port name - Windows: 'COM3'  Mac: '/dev/tty.usbmodem12345'
serialPort = serial.Serial(port='/dev/tty.usbmodem14702',baudrate=38400,bytesize=8,timeout=2,stopbits=serial.STOPBITS_ONE)

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

# setup filewriting to CSV
filename = "stream.csv"
f = open(filename, "w")
headers = "time,delta0,delta1,delta2,delta3,delta4\n"
f.write(headers)

# discard first line
serialPort.readline()

# read in data from serial, set to 1000 lines
for x in range(1000):
    # parse readline() into array, can be easily placed into other objects if wanted
    parseLine = serialPort.readline().decode('utf-8').split(",")
    # time component is discarded and replaced with x variable increment; time output is 8-bit and resets after 255
    list.append(Row(x,parseLine[1],parseLine[2],parseLine[3],parseLine[4],parseLine[5]))

# write to CSV
for obj in list:
    f.write(str(obj.time) + "," + str(obj.delta0) + "," + str(obj.delta1) + "," + str(obj.delta2) + "," + str(obj.delta3) + "," + str(obj.delta4) + ",\n")

f.close()
serialPort.close()