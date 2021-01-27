import serial

# This script uses the hardware build in folder qt7-ascii-out-dylan

# Need to define port according to your setup. Typical port name - Windows: 'COM3'  Mac: '/dev/tty.usbmodem12345'
serialPort = serial.Serial(port='/dev/tty.usbmodem14702',baudrate=38400,bytesize=8,timeout=2,stopbits=serial.STOPBITS_ONE)

# discard first line
serialPort.readline()

i = 0

while i < 50:
     parseLine = serialPort.readline().decode('utf-8').split(",")

     # isolate deltas for activity recognition
     deltas = [str(parseLine[3]), str(parseLine[7]), str(parseLine[11]), str(parseLine[15])]

     # convert string array to int array
     map(int, deltas)

     # grab max delta value
     max_value = max(deltas)

     # if max delta value exceeds threshold, read in data to get gesture 'data signature'
     if int(max_value) > 30:
        filename = "stream_" + str(i) + ".csv"
        f = open(filename, "w")
        # for debugging
        # headers = "ch1,sig1,ref1,delta1,ch2,sig2,ref2,delta2,ch3,sig3,ref3,delta3,ch4,sig4,ref4,delta4\n"
        # deltas only
        headers = "delta1,delta2,delta3,delta4\n"
        f.write(headers)
        for x in range(40):
            parseLine = serialPort.readline().decode('utf-8').split(",")
            
            # delta values only
            f.write(str(parseLine[3]) + "," + str(parseLine[7]) + "," + str(parseLine[11]) + "," + str(parseLine[15]) + "\n")

            # for debugging, includes all data output
            # f.write(str(parseLine[0]) + "," + str(parseLine[1]) + "," + str(parseLine[2]) + "," + str(parseLine[3]) + "," + str(parseLine[4]) + "," + str(parseLine[5]) + "," + str(parseLine[6]) + "," + str(parseLine[7]) + "," + str(parseLine[8]) + "," + str(parseLine[9]) + "," + str(parseLine[10]) + "," + str(parseLine[11]) + "," + str(parseLine[12]) + "," + str(parseLine[13]) + "," + str(parseLine[14]) + "," + str(parseLine[15]) + "\n")
            
        i += 1
        f.close()

serialPort.close()