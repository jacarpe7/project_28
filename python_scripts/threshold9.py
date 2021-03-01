import serial

# This script uses the hardware build in folder qt7-ascii-out-dylan

# Need to define port according to your setup. Typical port name - Windows: 'COM3'  Mac: '/dev/tty.usbmodem12345'
serialPort = serial.Serial(port='/dev/tty.usbmodem2202',baudrate=115200,bytesize=8,timeout=2,stopbits=serial.STOPBITS_ONE)

# discard first line
serialPort.readline()

i = 0

while i < 200:
     parseLine = serialPort.readline().decode('utf-8').split(",")
     # remove time value, alternatively we can reprogram the microcontroller to not output it
     parseLine.pop(0)
     # convert string array to int array
     map(int, parseLine)
     # grab max delta value
     max_value = max(parseLine)
     # if max delta value exceeds threshold, read in data to get gesture 'data signature'
     if int(max_value) > 25:
        filename = "stream_" + str(i) + ".csv"
        f = open(filename, "w")
        headers = "delta1,delta2,delta3,delta4,delta5,delta6,delta7,delta8,delta9\n"
        f.write(headers)
        for x in range(50):
            parseLine = serialPort.readline().decode('utf-8').split(",")
            f.write(str(parseLine[1]) + "," + str(parseLine[2]) + "," + str(parseLine[3]) + "," + str(parseLine[4]) + "," + str(parseLine[5]) + "," + str(parseLine[6]) + "," + str(parseLine[7]) + "," + str(parseLine[8]) + "," + str(parseLine[9]) + "\n" )
            
        i += 1
        f.close()

serialPort.close()