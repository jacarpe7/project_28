# SER 401 Capstone Project 2020-2021
### Project 28 - Proximity Sensing in a Post-COVID World

# The Project
## Table of Contents  
I. [The Team](#team)  
II. [The Idea](#headers)  
III. [What Didn't Work](#emphasis)  
IV. [What Did Work](#worked)  
V. [Final Product](#notworked)  
VI. [The Future](#nexttime)  
VII. [Requirements](#requirements)  
VIII. [Setup and Run](#setup)  
IX. [References](#ref)  

<a name="team"/>
<p align="right">

## The Team

Bob Martin</br>
Dylan Johnson</br>
Joshua Carpenter</br>
Kelly Petrone</br>
Michael Frederic</br>
Russell Smith</br>
</p>


<a name="headers"/>

## The Idea
<p align="center"><img src="media/ASU-Logo.gif" width="200"><img src="media/Microchip-Logo.png" width="200"></p>
  2020 was a huge year for humanity. Overnight there were unlimited problems being faced on a day to day basis. Whether it be social distancing, mask wearing, or quarentine. Our project had the goal to help solve one of these problems with a focus on software being developed by students at ASU, and the hardware being built and provided by Microchip.


  With this goal in mind, we knew a large problem people faced in a time where it wasn't known how long COVID survived on physical surfaces was to help avoid touching surfaces while operating through a daily routine. The goal was to develop a sensor, and using machine learning process data from the sensor to eliminate the need for a user to physically touch surfaces that other people would also be touching.


  The team bounced around with several ideas. But one that really stuck out to us was the need for people to touch an ATM. The ATM, originally designed in 1967 hasn't seen any updates in years. Still requiring a user to use a pin pad, touching a surface that many other people could have touched. We decided that this was going to be the focus of our project. 

<a name="emphasis"/>

## What Didn't Work
  The first step of our design process involved using the QT-7 sensor pictured below. We used this to get an idea of what the data looked like coming off of the sensor. We originally though the QT-7 had the chance of being a proximity sensor for a real world application. Through thurough testing we quickly disocvered that we were unable to get accurate and consistent results. This took us back to the drawing board.

  // PICTURE OF QT-7

  After the QT-7, Bob tipped us off to a friend's company of his that designs paint that is electronically conductive and could potentially detect proximity of a user's hand. Once we realized this; the next iteration of design is the proximity sensor pictured below.

  // PICTURE OF ORIGINAL PROXIMITY PAINT SENSOR

  When we started testing and applying Machine Learning to the data being produced from the sensor above. We quickly once again realized that the data was not accurately able to detect what direction a users hand was coming from. As the paint sensors were too close to eachother. We reached out to Bob and collectively put up a series of designs for potential sensors. Below are the results of those design mockups.

  // ALL MOCK UP IMAGES

  After talking through several of these designs and their upsides we landed on the one below. After testing we were quickly able to apply our machine learning algorithm to the resulting sensor and able to detect hand motions at a very high accuracy. We will discuss this further later on.
  
<p align="center"><img src="media/final_sensor.jpg" width="200">

  In developing a machine learning model that works best for our application there were several choices of model types. Below is a list of models that we tested prior to landing on a LSTM (Long Term Short Memory Network) model.

  - Linear Regression.
  - Logistic Regression.
  - Decision Tree.
  - SVM.
  - Naive Bayes.
  - kNN.
  - K-Means.
  - Random Forest.
  - LSTM.

  In testing, below is a chart of the models compared to eachother with their accuracy rates:

  // IMAGE OF GRAPHS

  We eventually decided on using an LSTM model due to the overall advantage in accuracy rates. Below is a more detailed explanation of what exactly a Long Term Short Memory Network is as stated by on a great breakdown by [Christopher Olah](https://colah.github.io/posts/2015-08-Understanding-LSTMs/):

  > Long Short Term Memory networks – usually just called “LSTMs” – are a special kind of RNN, capable of learning long-term dependencies. They were introduced by Hochreiter & Schmidhuber (1997), and were refined and popularized by many people in following work.1 They work tremendously well on a large variety of problems, and are now widely used. LSTMs are explicitly designed to avoid the long-term dependency problem. Remembering information for long periods of time is practically their default behavior, not something they struggle to learn!

<a name="worked"/>

## What Did Work

### Back End
As stated above, after thorough testing and application; we landed on using an LSTM model. 

### Front End Interface
Now to discuss the front end portion of the project. To our surprise in our initial research after landing on an ATM for our final project. ATM interfaces designed today are almost identical to those that were designed decades ago. This has a lot to do with the fact that ATMs are typically coded in low level langauges like C and C++, which are easier to run on cheaper hardware due to it being more lightweight. To make our project as portable as possible, we negated bringing in a larger interface library and landed on using a built-in Python library. This allowed us to have less dependencies, create an equally lightweight project, while still upgrading from the original C and C++ ATM designs. 

<a name="notworked"/>

## Final Product
<p align="center"><img src="media/final_project_gif.gif">

<a name="nexttime"/>

## The Future

/POTENTIAL USES OF THE SENSOR AND MODEL BUILDING

<a name="Requirements"/>

## Requirements

<a name="setup"/>

## Setup and Run

<a name="ref"/>

## References


