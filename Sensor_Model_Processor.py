import os
import serial
import platform
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras


# import model and display model summary
model = tf.keras.models.load_model('lstm_model')
# model.summary()

# Need to define port according to your setup. Typical port name - Windows: 'COM3'  Mac: '/dev/tty.usbmodem12345'
platform.system()
if platform.system() == 'Windows':
    port = 'COM3'
else:
    port = '/dev/tty.usbmodem12345'

serialPort = serial.Serial(port=port,baudrate=115200,bytesize=8,timeout=2,stopbits=serial.STOPBITS_ONE)

# discard first line
serialPort.readline()

while (1):
    queue = []
    parseLine = serialPort.readline().decode('utf-8').split(",")[:9]
    parseLine = [int(i) for i in parseLine] 
    indices = [0]
    pl = np.array(parseLine)
    mask = np.zeros(pl.size, dtype=bool)
    mask[indices] = True
    m = np.ma.array(pl, mask=mask)
    maxx = np.max(m)
    #print(parseLine)
    
    # Read in first 15 lines
    for _ in range(15):
        queue.append((parseLine))
        parseLine = serialPort.readline().decode('utf-8').split(",")[:9]
        parseLine = [int(i) for i in parseLine]
     
    # Loop until a line contains a value greater than or equal to 20
    while maxx < 20:
        #print(maxx)
        parseLine = serialPort.readline().decode('utf-8').split(",")[:9]
        parseLine = [int(i) for i in parseLine]
        queue.append((parseLine))
        queue.pop(0)
        #use mask to get accurate max value
        pl = np.array(parseLine)
        mask = np.zeros(pl.size, dtype=bool)
        mask[indices] = True
        m = np.ma.array(pl, mask=mask)
        maxx = np.max(m)

    # Append next 40 lines
    for x in range(40):
        parseLine = serialPort.readline().decode('utf-8').split(",")[:9]
        parseLine = [int(i) for i in parseLine]
        queue.append((parseLine))
    
    # Convert values to a vertical array
    #print(parseLine)
    #print(max(parseLine))
    from numpy import array
    #array needs to be in this 3d form in order to conform
    #to the model
    arr = array(np.vstack(queue))
    arr = arr.reshape(1, 55, 9)
    #print(arr)
    prediction = model.predict_classes(arr)
    
    # Test for what result of prediction was
    """ switch (prediction[0]) {
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
    """
    #print(arr)
    print(prediction[0])
           
serialPort.close()
