# Developer Environment Setup - Atmel Studio 7

![AtmelStudio7](https://www.microchip.com/images/default-source/avr-support/atmel-studio-7/atmelstudio7__google_291x202-min.jpg?sfvrsn=c1ad339d_1)

Atmel Studio 7 is an integrated development platform for developing and debugging all AVR(R) and SAM microcontroller applications.  It will be used to code and debug the AVR128DA48 microcontroller and Qt7 Xplained extension board for the length of the project.

### Prerequisites

  - Curiousity Nano Touch Adapter 
  - AVR128DA48 Microcontroller
  - QT7 Xplained Pro extension board
  - Standard-A to Micro-B USB cable
  - Computer or emulator with Windows 10 (x86/x64) installation
  - GitHub project is cloned to the computer </br></br>

### Atmel Studio 7 Installation Steps

 1.  Navigate to the Atmel Studio [download link](https://www.microchip.com/mplab/avr-support/atmel-studio-7) and download the software
 2.  Double click the file to start the installation
 3.  When prompted, select ONLY the "AVR 8-bit MCU" architecture option (uncheck the others)
 4.  When prompted, UNCHECK the "Atmel Software Framework and Example Projects" extension option
 5.  Follow all other standard installation prompts as needed (folder location, etc.) </br></br>
 
### AVR128 DA Device Pack

After installation on the first run of the software the specific device package needs to be installed.

1. Launch Atmel Studio 7
2. Navigate to Tools -> Device Pack Manager
3. In the search bar in the upper right corner enter "128DA"
4. The AVR-Dx_DFP device pack will show in the search results, select "Install"
5. Restart Atmel Studio </br></br>

### Hardware Assembly

Assemble the hardware components to match Figure 1 below and connect the USB cable from the microcontroller directly to your computer.  Connectivity issues can arise from using a USB hub so ensure it is connected directly to a USB port on the physical machine.</br></br>

![hardware-config](https://i.ibb.co/SnqR5Fy/board-config1.jpg) </br>
*Figure 1 - hardware configuration* </br></br>

### Running the software with the hardware now connected

After completing all previous steps you should see the device start page in Atmel (see Figure 2 below):</br></br>

![atmel-start](https://i.ibb.co/THy7908/atmel-start.jpg) </br>
*Figure 2 - device start page* 

Click the link in the bottom-left of the left pane to "update board database" </br></br>

### Running & Debugging a Basic Project (The "Hello World" of Atmel)

1.  Go to File -> Open Project/Solution
2.  Navigate to the cloned repo folder on drive and open the *AVR128-rawblink* Solution file
3.  Once the project is open, select Build -> Build Solution.  
4.  The build will succeed with zero errors.
5.  Now setup the debugger:
    1.  Right-click the solution name in the Solution Explorer and go to *Properties*
    2.  Select the debugger/programmer as seen below (there should be only one option) in Figure 3.
    3.  Save the project
6.  Click the "Start Debugging and Break" icon on the far-left of the toolbar (looks like a blue play/pause button).  This pushes the compiled/linked code to the onboard debugger on the hardware.
7.  Click the "Continue" icon on the far-left side of the toolbar (looks like a green play button).  This will actually start execution and debugging of the code on the hardware.  If the far right 2 LED's on the QT7 board are blinking in sequence, you have successfully completed setup. </br></br>

![debug-setup](https://i.ibb.co/WDZn091/debug-setup.jpg)</br>
*Figure 3 - Setting up Debugger*
 



