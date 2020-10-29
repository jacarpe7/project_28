<h1>Atmel Project Creation Steps </h1>

<h3>10/18/2020</h3>

<h4>Pre-requisites:</h4>

- Read: _Atmel Start Project Creation Guide.md_

Resources:

- [Atmel Studio Official Documentation](https://onlinedocs.microchip.com/pr/GUID-ECD8A826-B1DA-44FC-BE0B-5A53418A47BD-en-US-4.1.1/index.html?GUID-00257F02-E33C-40C3-B324-83DBCC05EC30)
- [QTouch Library Documentation](https://microchipdeveloper.com/touch:generate-qtouch-configurator-touch-project)

**Part 1**. Important Components (main view):

1. File Tree: this is our file navigation browser that will be used to access and edit code that is intended to be built on the hardware.
2. Debugger: debugger menu that can be used to launch, debug, and step through the software.
3. Hardware related tools: this menu can be used to build (deploy the software -> hardware), access the hardware configuration,and monitor; hardware memory, registers, processor, and I/O.

![](https://i.imgur.com/6UeLRco.jpg)

**Part 2**. Accessing the Data Visualizer:

1. *tools->Data Visualizer*

![](https://i.imgur.com/2NLMbv0.jpg)

2. Connect to your device (COM port reliant).

![](https://i.imgur.com/p3Bknur.jpg)

3. Depending the device the display will be different, for us it should look something like this:
    - *tabs at the top indicate the various viewports: Basic (current), Graph, Advanced, All*

![](https://i.imgur.com/zWvBMCU.jpg)

4. Take a look at the Graph tab, it will display the data visually.

![](https://i.imgur.com/RgJinDI.jpg)

5.The advanced data tab displays an extended versions of the basic data tab.

![](https://i.imgur.com/oyYFs1Q.jpg)

6. The all data tab condenses the advanced data and graph tabs into one viewport.

7. From here you will want to reference [Exporting data via QTouch Data Visualizer in Atmel Studio](Atmel_Start_Project_Creation_Guide.md) for further information on how to export the data.

**Part 3**. Project Re-configuration:

1. *Project -> Re-configure Atmel Start Project*

![](https://i.imgur.com/H7a86GU.jpg)

2. This will take you to *Atmel Start* where you can make changes to your project skeleton. See *Atmel Start Project Creation Guide.md*


**Part 4**. Usefull Customization Options:

1. *Tools -> Customize*: choose what components you want to display in the view port.

![](https://i.imgur.com/O2yeWr3.jpg)

2. *Tools -> Options*: featurs a ton of customizable options for the developer environment along with a few notable sections like *Projects* which houses project configurations and *Live Watch* which is the configuration for logged data output.

![](https://i.imgur.com/To08mUU.jpg)

3. *Tools -> Import and Export Settings*: Gives the ability to export/import your current settings in Atmel. Also features the ability to *reset* the settings back to the factory default for Atmel.

![](https://i.imgur.com/bis59p4.jpg)
