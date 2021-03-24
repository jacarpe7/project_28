import os
import serial
import platform
import pandas as pd
import numpy as np
from numpy import dstack
import tensorflow as tf
from tensorflow import keras

# import model and display model summary
model = tf.keras.models.load_model("lstm")
# model.summary()

# Need to define port according to your setup. Typical port name - Windows: 'COM3'  Mac: '/dev/tty.usbmodem12345'
platform.system()
if platform.system() == 'Windows':
    port = 'COM3'
else:
    port = '/dev/tty.usbmodem2202'

serialPort = serial.Serial(port=port,baudrate=38400,bytesize=8,timeout=2,stopbits=serial.STOPBITS_ONE)

# discard first line
serialPort.readline()

deltaMax = 0;

print("Ready for gesture testing.\n")

while (1):
    
    queue = [[],[],[],[],[]]

    # for repeat iterations, checks for maximum delta level before processing
    parseLine = serialPort.readline().decode('utf-8').split(",")
    # for maximum delta monitoring, omit time and newline values from parseLine
    deltas = [parseLine[1], parseLine[2], parseLine[3], parseLine[4], parseLine[5]]
    deltaMax = max(map(int, deltas))

    # holding loop until all sensors are below 20
    while deltaMax > 20:
        parseLine = serialPort.readline().decode('utf-8').split(",")
        # for maximum delta monitoring, omit time and newline values from parseLine
        deltas = [parseLine[1], parseLine[2], parseLine[3], parseLine[4], parseLine[5]]
        deltaMax = max(map(int, deltas))

    # populates queue
    for _ in range(20):
        parseLine = serialPort.readline().decode('utf-8').split(",")
        for a in range(5):
            # a+1 as the first output, a[0], is a counter
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
    
    testArr = list()
    for a in range(5):
        testArr.append(queue[a])

    testArr = dstack(testArr)

    prediction = model.predict_classes(testArr)
    print("Gesture prediction: " + str(prediction))

    # # Test for what result of prediction was
    # switch (prediction[0]) {
    #     case 1: print('swipe left');
    #         break;
    #     case 2: print('swipe right');
    #         break;
    #     case 3: print('swipe up');
    #         break;
    #     case 4: print('select');
    #         break;
    #     default: print('unknown selection {}'.format(prediction[0]));
    #         break;
    # }
           
serialPort.close()