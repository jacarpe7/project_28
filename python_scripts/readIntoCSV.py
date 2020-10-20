import serial

# This script uses the hardware build in folder qt7-ascii-out-dylan

# Need to define port according to your setup, output is readable at 38400 baudrate
serialPort = serial.Serial(port='COM3',baudrate=38400,bytesize=8,timeout=2,stopbits=serial.STOPBITS_ONE)

# setup filewriting to CSV
filename = "stream.csv"
f = open(filename, "w")
headers = "time,time-8bit,delta0,delta1,delta2,delta3,delta4\n"
f.write(headers)

# discard first line
serialPort.readline()

# change range value to collect more/less data points
for x in range(500):
	# timer. TODO: get rid of one time component
	f.write(x + ",")
	# read in from device
    f.write(serialPort.readline().decode('utf-8'))

serialPort.close()
f.close()