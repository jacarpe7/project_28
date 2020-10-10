## Reading the serial port from Python:

### Before you start:
* Must have Python installed on your computer
* Install pySerial via command line: pip install pyserial
* Make sure you don't have the serial port connected in Atmel Studio
* If you need to figure out your port information, you can look in Atmel Studio when you connect the serial port.

### Python code:
```
import serial
serialPort = serial.Serial(port='COM3',baudrate=38400,bytesize=8,timeout=2,stopbits=serial.STOPBITS_ONE)
print(serialPort.readline())
serialPort.close()
```