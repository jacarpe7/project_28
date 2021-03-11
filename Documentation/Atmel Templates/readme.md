About Atmel builds:

To load an Atmel build, such as AVRDA-Gain8AllSensors:
* Connect the AVR (microcontroller device) to your computer.
* Open Atmel Studio
* Click File -> Open -> Project/Solution
* Navigate to the build folder and select the .atsln file
* After this loads, Build will show as a menu bar heading; click it and select Build Solution
* After the solution has built, click either the blue play/pause or the green play button. This will write the build to the microcontroller. Click Stop and you can exit out.

To modify the gain amount:
* Within the primary folder, go to qtouch -> touch.h
* Scroll down about a third of the way where NODE_X_PARAMS are defined and modify a number in the NODE_GAIN section.

To modify the microcontroller output:
* Within the primary folder, go to qtouch -> datastreamer -> datastreamer_UART_avr.c
* The main section for the output is about halfway down where you find sprintf and send_string statements
