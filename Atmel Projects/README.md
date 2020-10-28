## Modified configurations for varying gain amounts

Differing levels of gain affect the sensitivity and precision of the device sensors. We will need to determine ideal gain levels for the sensors to process non-touch gestures through machine learning.

For purposes of designing uniform custom builds, this is the process used for developing these builds:
* Go to Atmel START and choose Browse Examples
* Search for "QT7" and select the AVRDA-Curiosity-Nano-QT7-XPRO-Touch_project
* Click Open Selected Example
* Click the box for QTouch_Library and click QTouch Configurator
* To adjust gain, click Parameters and scroll down to find the Gain column in the table of sensors
* Return to the Dashboard (top icon on the left side)
* Click USART and check the box for Printf support.
* Export Project, specify file name, and Download Pack
* Load the project in Atmel Studio and navigate to the files/folders that are generated.
* Replace the file /qtouch/datastreamer/datastreamer_UART_avr.c with one that prints delta values as output
	* Example location of modified datastreamer_UART_avr.c:  qt7-ascii-out project (the goal is to keep the up-to-date configuration directly in develop, not in Atmel Projects)