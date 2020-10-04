## Exporting data via QTouch Data Visualizer in Atmel Studio:
Note: This document uses configuration from the qt7-proj1 solution file Bob provided us.

*	Open Atmel Studio and ensure your hardware (AVR128DA48, QT7 Xplained Pro, QTouch PTC) is connected via USB and has the qt7-proj1 solution loaded.
*	Open the Data Visualizer from the Tools menu.
*	Navigate to the Serial Port Control Panel.
	*	If not already open, it is in Configuration > External Connection > Serial Port.
*	These boxes should be checked: DTR, Autodetect protocols, Show Config search path.
*	The Config search path needs to be set to the datastreamer folder located in the qt7-proj1 folder: qt7-proj1 > qt7-proj1 > qtouch > datastreamer
	*	The datastreamer folder will contain useful information to understand how this data is handled to generate the output from this process.
*	Connect to the Serial Port and wait for connection to activate. 
*	A few new windows should display. Open up the QTouch Data Visualizer window.
*	Scroll to the bottom of the window and you should see a "Start" button.
*	Click Start and select a location to save the output CSV.
*	Once you've selected your filename and location, the output data is being recorded. Perform any actions you'd like recorded on the QT7 board.
*	Click Stop when done. You can then review your CSV in Excel.