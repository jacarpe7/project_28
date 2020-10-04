## Exporting data via File Logger in Atmel Studio:
Note: It appears this method only allows for exporting the data from one sensor at a time.
*	Connect your data source and get the Data Visualizer responsive to activity with the QT7 Xplained. 
*	Make sure Serial Port Control Panel is open and shows as connected.
*	Open up Configuration by clicking the arrow/expander (left side of screen) to display Data Visualizer Modules.
*	Open the Utilities branch and double click on File Logger.
*	Provide a filename in the File field to save as.
*	Select a data type
	*	Options are RAW, CSV, BIN, ASCII, HEX
*	Click and drag a headphone jack icon from the Data Stream Control Panel and drop onto the Sink icon in Log to File (underneath the word Type).
	*	In our initial setup, the relevant options are Delta0 through Delta4.
*	Click Start to start logging data and click Stop when done.