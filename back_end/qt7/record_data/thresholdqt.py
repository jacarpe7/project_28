import serial
import numpy as np

# Need to define port according to your setup. Typical port name - Windows: 'COM3'  Mac: '/dev/tty.usbmodem12345'
serialPort = serial.Serial(port='/dev/tty.usbmodem2202',baudrate=38400,bytesize=8,timeout=2,stopbits=serial.STOPBITS_ONE)       

# discard first line, partial data
serialPort.readline()

deltaMax = 0
writeCounter = 1

while (1):
    queue = [[],[],[],[],[]]
    parseLine = serialPort.readline().decode('utf-8').split(",")
    # for maximum delta monitoring, omit time and newline values from parseLine
    deltas = [parseLine[1], parseLine[2], parseLine[3], parseLine[4], parseLine[5]]
    deltaMax = max(map(int, deltas))

    while deltaMax > 20:
        parseLine = serialPort.readline().decode('utf-8').split(",")
        # for maximum delta monitoring, omit time and newline values from parseLine
        deltas = [parseLine[1], parseLine[2], parseLine[3], parseLine[4], parseLine[5]]
        deltaMax = max(map(int, deltas))

    for _ in range(20):
        parseLine = serialPort.readline().decode('utf-8').split(",")
        for a in range(5):
            queue[a].append(int(parseLine[a+1]))
    
    while deltaMax < 20:
        parseLine = serialPort.readline().decode('utf-8').split(",")
        # for maximum delta monitoring, omit time and newline values from parseLine
        deltas = [parseLine[1], parseLine[2], parseLine[3], parseLine[4], parseLine[5]]
        deltaMax = max(map(int, deltas))
        for a in range(5):
            queue[a].pop(0)
            queue[a].append(int(parseLine[a+1]))

    # reset deltaMax value
    deltaMax = 0
    for x in range(30):
        parseLine = serialPort.readline().decode('utf-8').split(",")
        for a in range(5):
            queue[a].append(int(parseLine[a+1]))
    
    # Convert values to a vertical array
    arr = np.vstack(queue)

    # save to file
    filename = "stream_" + str(writeCounter) + ".txt"
    f = open(filename, "w")
    for a in range(5):
        for b in range(50):
            f.write(str(queue[a][b]) + " ")

        f.write("\n")

    f.close()
    print("stream_" + str(writeCounter) + ".txt written to file")
    writeCounter += 1


serialPort.close()