import serial

# Need to define port according to your setup. Typical port name - Windows: 'COM3'  Mac: '/dev/tty.usbmodem12345'
serialPort = serial.Serial(port='/dev/tty.usbmodem2202',baudrate=38400,bytesize=8,timeout=2,stopbits=serial.STOPBITS_ONE)

class Row:
    def __init__(row, delta0, delta1, delta2, delta3):
        row.delta0 = delta0
        row.delta1 = delta1
        row.delta2 = delta2
        row.delta3 = delta3

# discard first line
serialPort.readline()

#list for each sensor
list0 = list()
list1 = list()
list2 = list()
list3 = list()

i = 0
q = 0
queue = []

while (1):
    parseLine = serialPort.readline().decode('utf-8').split(",")
    deltas = [parseLine[2], parseLine[3], parseLine[4], parseLine[5]]
     
    if q < 15:
        queue.append(Row(parseLine[2], parseLine[3], parseLine[4], parseLine[5]))
        q += 1 
     
    else:
        queue.pop(0)
        queue.append(Row(parseLine[2], parseLine[3], parseLine[4], parseLine[5]))
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

            for x in range(40):
                parseLine = serialPort.readline().decode('utf-8').split(",")
                list0.append(int(parseLine[2]))
                list1.append(int(parseLine[3]))
                list2.append(int(parseLine[4]))
                list3.append(int(parseLine[5]))

            i += 1
            
            filename = "stream_" + str(i) + ".txt"
            f = open(filename, "w")
            for item in list0:
                f.write(str(item) + " ")

            list0.clear()
            f.write("\n")
            for item in list1:
                f.write(str(item) + " ")

            list1.clear()
            f.write("\n")
            for item in list2:
                f.write(str(item) + " ")

            list2.clear()
            f.write("\n")
            for item in list3:
                f.write(str(item) + " ")

            list3.clear()
            f.close()
            q = 0
            deltas.clear()
            queue.clear()
            print("Gesture " + str(i) + " written to file")

        else:
            q += 1 

serialPort.close()