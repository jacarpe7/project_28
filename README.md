# SER 401 Capstone Project 2020-2021
### Project 28 - Proximity Sensing in a Post-COVID World

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jacarpe7/project_28/HEAD?filepath=python_scripts%2Fml_model_generation.ipynb)

**Required Software & Tools**</br>
[AtmelStudio7](https://www.microchip.com/images/default-source/avr-support/atmel-studio-7/atmelstudio7__google_291x202-min.jpg?sfvrsn=c1ad339d_1)</br>
[Atmel Start](https://start.atmel.com/)</br>
[Anaconda Toolkit](https://www.anaconda.com/products/individual)</br>
[Python](https://www.python.org/downloads/)</br>
</br>

**Required Hardware in Use**</br>
Curiousity Nano Touch Adapter</br>
AVR128DA48 Microcontroller</br>
QT7 Xplained Pro extension board</br>
</br>

# The Project
## Table of Contents  
[The Idea](#headers)  
[What Didn't Work](#emphasis)  
[What Did Work](#worked)  
[Final Product](#notworked)  
[The Future](#nexttime)  

<a name="headers"/>

## Headers

<a name="emphasis"/>

## Headers

<a name="worked"/>

## Headers

<a name="notworked"/>

## Headers

<a name="nexttime"/>

## Headers

**Initial Setup**</br>
1. Download and install Atmel Studio</br>
2. Import 'qt7-ascii-out.atsln' onto device using Atmel Studio following instructions in the video below</br>
[![](http://img.youtube.com/vi/wmxJ9FIv4wA/0.jpg)](http://www.youtube.com/watch?v=wmxJ9FIv4wA "Atmel Install Video")</br>
  * QT7 ASCII project turns the QT7 into a proximity sensor. Converting that data into ASCII to save locally to a CSV file
3. Now that software is loaded onto the device, ensure you have the latest version of python installed</br>
4. Run the following command in terminal;
```terminal
python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose pyserial
```
5. If using Mac, find serial port below. If on windows, keep python code set to port 3. 
```Mac port for AVR128DA48
ls /dev/tty.*
screen /dev/tty.[yourSerialPortName] [yourBaudRate]
screen /dev/tty.usbserial-A6004byf 9600
```
6. Run program depending on where you'd like data to be saved. 
```
python_scripts -> readIntoCSV.py
  * Saves data into a local CSV
python_scripts -> readIntoObject.py
  * Saves data into a python object
```

**Video Links**</br>
[Artifact Review 1](https://youtu.be/0COBPH9X2WI)

**Team Members**</br>
Dylan Johnson</br>
Joshua Carpenter</br>
Kelly Petrone</br>
Michael Frederic</br>
Russell Smith</br>

**Resources**</br>
https://realpython.com/linear-regression-in-python/
</br>
