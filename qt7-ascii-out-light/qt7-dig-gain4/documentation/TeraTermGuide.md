## Tera Term Guide
1. Download and install Tera Term: https://ttssh2.osdn.jp/index.html.en
2. Have your hardware plugged into the computer and know what serial port the data is coming in through. This example is using Bob's qt7-ascii-out solution loaded onto the hardware.
3. Open Tera Term and wait for the New Connection menu to pop up.
4. Click Cancel. You must modify settings for the data from the serial port to read correctly.
5. Click Setup and then Serial port...
6. Ensure the correct port is selected and change the speed to 38400.
7. Click New open.
8. Data should start feeding to the screen and it should be readable.
    * Hint: If no data is streaming in, it's possible your serial port is being accessed by another program. Check Atmel Studio
9. To log the data into a text file, click File, Log... and choose a name/location for the log file.
10. Perform any activity over the sensors you would like recorded.
11. When you're ready to stop logging the data stream, click File and Stop Logging or close the window that popped up when you began logging the data.