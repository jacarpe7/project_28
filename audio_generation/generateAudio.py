import serial

import pydub
from pydub import AudioSegment
from pydub.generators import *
from pydub.playback import play
# import ffmpeg

# Need to define port according to your setup. Typical port name - Windows: 'COM3'  Mac: '/dev/tty.usbmodem12345'
serialPort = serial.Serial(port='/dev/tty.usbmodem14702',baudrate=38400,bytesize=8,timeout=2,stopbits=serial.STOPBITS_ONE)

# define sample object to hold data
class Row:
    def __init__(row, time, delta0, delta1, delta2, delta3, delta4):
        row.time = time
        row.delta0 = delta0
        row.delta1 = delta1
        row.delta2 = delta2
        row.delta3 = delta3
        row.delta4 = delta4

# array to hold objects
list = []

# setup filewriting to CSV
filename = "stream.csv"
f = open(filename, "w")
headers = "time,delta0,delta1,delta2,delta3,delta4\n"
f.write(headers)

# Create an empty AudioSegment
result = AudioSegment.silent(duration=0)
sound1 = AudioSegment.from_wav("1.wav")
sound2 = AudioSegment.from_wav("2.wav")
sound3 = AudioSegment.from_wav("3.wav")
sound4 = AudioSegment.from_wav("4.wav")
sound5 = AudioSegment.from_wav("5.wav")

# discard first line
serialPort.readline()

# read in data from serial, set to 1000 lines - start at 100 for first use
for x in range(1000):
    # parse readline() into array, can be easily placed into other objects if wanted
    parseLine = serialPort.readline().decode('utf-8').split(",")
    # time component is discarded and replaced with x variable increment; time output is 8-bit and resets after 255
    list.append(Row(x,parseLine[1],parseLine[2],parseLine[3],parseLine[4],parseLine[5]))
    for n in range(1,6):
    	if (int(parseLine[n]) > 50):
            if (n == 1):
                sine = sound1.apply_gain(-2).fade_in(150).fade_out(150)
            elif n == 2:
                sine = sound2.apply_gain(-2).fade_in(150).fade_out(150)
                #sine = gen.to_audio_segment(duration=150).apply_gain(-2).fade_in(150).fade_out(150)
            elif n == 3:
                sine = sound3.apply_gain(-2).fade_in(150).fade_out(150)
                #sine = gen.to_audio_segment(duration=150).apply_gain(-2).fade_in(50).fade_out(150)
            elif n == 4:
                sine = sound4.apply_gain(-2).fade_in(150).fade_out(150)
                #sine = gen.to_audio_segment(duration=100).apply_gain(-2).fade_in(100).fade_out(50)
            elif n == 5:
                sine = sound5.apply_gain(-2).fade_in(150).fade_out(150)
                #sine = gen.to_audio_segment(duration=100).apply_gain(-2).fade_in(100).fade_out(100)
    		
            # Append the sine to our result
            result += sine

# write to CSV
for obj in list:
    f.write(str(obj.time) + "," + str(obj.delta0) + "," + str(obj.delta1) + "," + str(obj.delta2) + "," + str(obj.delta3) + "," + str(obj.delta4) + ",\n")

f.close()
serialPort.close()

# Play the result
play(result)
result.export("qt7.mp3", format="mp3")

