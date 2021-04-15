import os
import threading
import time
import serial
import platform
import pandas as pd
import numpy as np
from numpy import dstack
import tensorflow as tf
from tensorflow import keras
from rx.core import Observable
from rx.subject import Subject

LSTM_P = os.path.abspath('lstm')

def main():
    #DB_PATH = os.path.abspath('bank_db')
    # import model and display model summary
    model = tf.keras.models.load_model(LSTM_P)
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

    # create Subject
    subject = Subject()

    def loopChecker():
        deltaMax = 0
        print("Ready for gesture testing.\n")
        while (1):
            
            queue = [[],[],[],[],[],[],[],[],[]]

            for _ in range(15):
                parseLine = serialPort.readline().decode('utf-8').split(",")
                for a in range(9):
                    queue[a].append(int(parseLine[a+1]))

            while deltaMax < 20:
                parseLine = serialPort.readline().decode('utf-8').split(",")
                # for maximum delta monitoring, omit time and newline values from parseLine
                deltas = [parseLine[1], parseLine[2], parseLine[3], parseLine[4], parseLine[5], parseLine[6], parseLine[7], parseLine[8], parseLine[9]]
                deltaMax = max(map(int, deltas))
                for a in range(9):
                    queue[a].pop(0)
                    queue[a].append(int(parseLine[a+1]))

            # reset deltaMax value
            deltaMax = 0
            for x in range(40):
                parseLine = serialPort.readline().decode('utf-8').split(",")
                for a in range(9):
                    queue[a].append(int(parseLine[a+1]))
            
            testArr = list()
            for a in range(9):
                testArr.append(queue[a])

            testArr = dstack(testArr)

            prediction = model.predict_classes(testArr)
            print("Gesture prediction: " + str(prediction))

            subject.on_next(prediction)

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

    t1 = threading.Thread(target=loopChecker)
    t1.daemon = True
    t1.start()
    print("returning subject")
    return subject