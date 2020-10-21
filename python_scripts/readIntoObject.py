import serial

# This script uses the hardware build in folder qt7-ascii-out-dylan

# Need to define port according to your setup
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

# discard first line
serialPort.readline()

# read in data from serial
for x in range(50):
    parseLine = serialPort.readline().decode('utf-8').split(",")
    # time component is discarded and replaced with x variable increment
    list.append(Row(x,parseLine[1],parseLine[2],parseLine[3],parseLine[4],parseLine[5]))

# print out to verify success
for obj in list:
    print(obj.time, obj.delta0, obj.delta1, obj.delta2, obj.delta3, obj.delta4, sep = ",")

serialPort.close()