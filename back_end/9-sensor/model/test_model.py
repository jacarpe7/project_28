import os
import serial
import platform
import pandas as pd
import numpy as np
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

serialPort = serial.Serial(port=port,baudrate=115200,bytesize=8,timeout=2,stopbits=serial.STOPBITS_ONE)

# discard first line
serialPort.readline()

while (1):
    queue = []
    parseLine = serialPort.readline().decode('utf-8').split(",")
    
    # Read in first 15 lines
    for _ in range(15):
        queue.append(list(int(parseLine)))
        parseLine = serialPort.readline().decode('utf-8').split(",")
     
    # Loop until a line contains a value greater than or equal to 20
    while max(list(int(parseLine))) < 20:
        parseLine = serialPort.readline().decode('utf-8').split(",")
        queue.append(list(int(parseLine)))
        queue.pop(0)

    # Append next 40 lines
    for x in range(40):
        parseLine = serialPort.readline().decode('utf-8').split(",")
        queue.append(list(int(parseLine)))
    
    # Convert values to a vertical array
    arr = np.vstack(queue)
    prediction = model.predict_classes(arr)

    # Test for what result of prediction was
    switch (prediction[0]) {
        case 1: print('swipe left');
            break;
        case 2: print('swipe right');
            break;
        case 3: print('swipe up');
            break;
        case 4: print('select');
            break;
        default: print('unknown selection {}'.format(prediction[0]));
            break;
    }
           
serialPort.close()