import serial

# This script uses the hardware build in folder qt7-ascii-out-dylan

# Need to define port according to your setup. Typical port name - Windows: 'COM3'  Mac: '/dev/tty.usbmodem12345'
serialPort = serial.Serial(port='/dev/COM3',baudrate=115200,bytesize=8,timeout=2,stopbits=serial.STOPBITS_ONE)

class Row:
    def __init__(row, delta0, delta1, delta2, delta3, delta4, delta5, delta6, delta7, delta8):
        row.delta0 = delta0
        row.delta1 = delta1
        row.delta2 = delta2
        row.delta3 = delta3
        row.delta4 = delta4
        row.delta5 = delta5
        row.delta6 = delta6
        row.delta7 = delta7
        row.delta8 = delta8
        
    
# discard first line
serialPort.readline()

i = 0
q = 0
count = 0
queue = []
baseline = []

while (1):
     parseLine = serialPort.readline().decode('utf-8').split(",")
     
     if count == 0 or count % 30 == 0:
         baseline = [int(parseLine[1]), int(parseLine[2]), int(parseLine[3]), int(parseLine[4]), int(parseLine[5]), int(parseLine[6]), int(parseLine[7]), int(parseLine[8]), int(parseLine[9])]
     
     # isolate deltas for activity recognition
     deltas = [str(int(parseLine[1]-baseline[0])), str(int(parseLine[2]-baseline[1])), str(int(parseLine[3]-baseline[2])), str(int(parseLine[4]-baseline[3])), str(int(parseLine[5]-baseline[4])), str(int(parseLine[6]-baseline[5])), str(int(parseLine[7]-baseline[6])), str(int(parseLine[8]-baseline[7])), str(int(parseLine[9]-baseline[8]))]
     if q < 15:
         queue.append(Row(str(parseLine[1]), str(parseLine[2]), str(parseLine[3]), str(parseLine[4]), str(parseLine[5]), str(parseLine[6]), str(parseLine[7]), str(parseLine[8]), str(parseLine[9])))
     else:
         queue.pop(0)
         queue.append(Row(str(parseLine[1]), str(parseLine[2]), str(parseLine[3]), str(parseLine[4]), str(parseLine[5]), str(parseLine[6]), str(parseLine[7]), str(parseLine[8]), str(parseLine[9])))

     q += 1 
     # convert string array to int array
     map(int, deltas)

     # grab max delta value
     max_value = max(deltas)

     # if max delta value exceeds threshold, read in data to get gesture 'data signature'
     if int(max_value) >= 20:
        filename = "stream_" + str(i) + ".csv"
        f = open(filename, "w")
        # for debugging
        # headers = "ch1,sig1,ref1,delta1,ch2,sig2,ref2,delta2,ch3,sig3,ref3,delta3,ch4,sig4,ref4,delta4\n"
        # deltas only
        headers = "delta1,delta2,delta3,delta4,delta5,delta6,delta7,delta8,delta9\n"
        f.write(headers)
        for obj in queue:
            f.write(obj.delta0 + "," + obj.delta1 + "," + obj.delta2 + "," + obj.delta3 + "," + obj.delta4 + "," + obj.delta5 + "," + obj.delta6 + "," + obj.delta7 + "," + obj.delta8 + "\n")
        for x in range(40):
            parseLine = serialPort.readline().decode('utf-8').split(",")
            
            # delta values only
            f.write(str(str(parseLine[1]) + "," + str(parseLine[2]) + "," + str(parseLine[3]) + "," + str(parseLine[4]) + "," + str(parseLine[5]) + "," + str(parseLine[6]) + "," + str(parseLine[7]) + "," + str(parseLine[8]) + "," + str(parseLine[9]) + "\n"))

            # for debugging, includes all data output
            # f.write(str(parseLine[0]) + "," + str(parseLine[1]) + "," + str(parseLine[2]) + "," + str(parseLine[3]) + "," + str(parseLine[4]) + "," + str(parseLine[5]) + "," + str(parseLine[6]) + "," + str(parseLine[7]) + "," + str(parseLine[8]) + "," + str(parseLine[9]) + "," + str(parseLine[10]) + "," + str(parseLine[11]) + "," + str(parseLine[12]) + "," + str(parseLine[13]) + "," + str(parseLine[14]) + "," + str(parseLine[15]) + "\n")   
        i += 1
        f.close()
        print("Gesture " + str(i) + " written to file")

serialPort.close()