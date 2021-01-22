import serial

# This script uses the hardware build in folder qt7-ascii-out-dylan

# Need to define port according to your setup. Typical port name - Windows: 'COM3'  Mac: '/dev/tty.usbmodem12345'
serialPort = serial.Serial(port='/dev/tty.usbmodem14702',baudrate=38400,bytesize=8,timeout=2,stopbits=serial.STOPBITS_ONE)

# discard first line
serialPort.readline()

i = 0

while i < 10:
     parseLine = serialPort.readline().decode('utf-8').split(",")
     # remove time value, alternatively we can reprogram the microcontroller to not output it
     
     print(parseLine)

     deltas = [str(parseLine[3]), str(parseLine[7]), str(parseLine[11]), str(parseLine[15])]

     print(deltas)

     # convert string array to int array
     map(int, deltas)
     # grab max delta value
     max_value = max(deltas)
     # if max delta value exceeds threshold, read in data to get gesture 'data signature'
     if int(max_value) > 35:
        filename = "stream_" + str(i) + ".csv"
        f = open(filename, "w")
        headers = "ch1,sig1,ref1,delta1,ch2,sig2,ref2,delta2,ch3,sig3,ref3,delta3,ch4,sig4,ref4,delta4\n"
        f.write(headers)
        for x in range(50):
            parseLine = serialPort.readline().decode('utf-8').split(",")
            f.write(str(parseLine[0]) + "," + str(parseLine[1]) + "," + str(parseLine[2]) + "," + deltas[0] + "," + str(parseLine[4]) + "," + str(parseLine[5]) + "," + str(parseLine[6]) + "," + deltas[1] + "," + str(parseLine[8]) + "," + str(parseLine[9]) + "," + str(parseLine[10]) + "," + deltas[2] + "," + str(parseLine[12]) + "," + str(parseLine[13]) + "," + str(parseLine[14]) + "," + deltas[3] + "\n")
            # f.write(str(parseLine[0]) + "," + str(parseLine[1]) + "," + str(parseLine[2]) + "," + str(parseLine[3]) + "," + str(parseLine[4]) + "," + str(parseLine[5]) + "," + str(parseLine[6]) + "," + str(parseLine[7]) + "\n")
            
        i += 1
        f.close()

serialPort.close()