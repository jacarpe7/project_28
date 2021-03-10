import serial

# Need to define port according to your setup. Typical port name - Windows: 'COM3'  Mac: '/dev/tty.usbmodem12345'
serialPort = serial.Serial(port='/dev/tty.usbmodem2202',baudrate=115200,bytesize=8,timeout=2,stopbits=serial.STOPBITS_ONE)

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

#lists = [[]]

#list for each sensor
list0 = list()
list1 = list()
list2 = list()
list3 = list()
list4 = list()
list5 = list()
list6 = list()
list7 = list()
list8 = list()

i = 0
q = 0
queue = []

while (1):
    parseLine = serialPort.readline().decode('utf-8').split(",")
    deltas = [parseLine[1], parseLine[2], parseLine[3], parseLine[4], parseLine[5], parseLine[6], parseLine[7], parseLine[8], parseLine[9]]
     
    if q < 15:
        queue.append(Row(parseLine[1], parseLine[2], parseLine[3], parseLine[4], parseLine[5], parseLine[6], parseLine[7], parseLine[8], parseLine[9]))
     
    else:
        queue.pop(0)
        queue.append(Row(parseLine[1], parseLine[2], parseLine[3], parseLine[4], parseLine[5], parseLine[6], parseLine[7], parseLine[8], parseLine[9]))

    q += 1 
    # convert string array to int array
    map(int, deltas)

    # grab max delta value
    max_value = max(deltas)

    # if max delta value exceeds threshold, read in data to get gesture 'data signature'
    if int(max_value) >= 20:
        for obj in queue:
            list0.append(int(obj.delta0))
            list1.append(int(obj.delta1))
            list2.append(int(obj.delta2))
            list3.append(int(obj.delta3))
            list4.append(int(obj.delta4))
            list5.append(int(obj.delta5))
            list6.append(int(obj.delta6))
            list7.append(int(obj.delta7))
            list8.append(int(obj.delta8))

        for x in range(40):
            parseLine = serialPort.readline().decode('utf-8').split(",")
            list0.append(int(parseLine[1]))
            list1.append(int(parseLine[2]))
            list2.append(int(parseLine[3]))
            list3.append(int(parseLine[4]))
            list4.append(int(parseLine[5]))
            list5.append(int(parseLine[6]))
            list6.append(int(parseLine[7]))
            list7.append(int(parseLine[8]))
            list8.append(int(parseLine[9]))

        i += 1
        
        
        filename = "stream_" + str(i) + ".txt"
        f = open(filename, "w")
        for item in list0:
            f.write(str(item) + " ")

        f.write("\n")
        for item in list1:
            f.write(str(item) + " ")

        f.write("\n")
        for item in list2:
            f.write(str(item) + " ")

        f.write("\n")
        for item in list3:
            f.write(str(item) + " ")

        f.write("\n")
        for item in list4:
            f.write(str(item) + " ")

        f.write("\n")
        for item in list5:
            f.write(str(item) + " ")

        f.write("\n")
        for item in list6:
            f.write(str(item) + " ")

        f.write("\n")
        for item in list7:
            f.write(str(item) + " ")

        f.write("\n")
        for item in list8:
            f.write(str(item) + " ")

        f.close()
        print("Gesture " + str(i) + " written to file")


serialPort.close()