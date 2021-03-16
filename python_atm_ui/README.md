# Python ATM Interface
### Revision 3/18/2021

![welcome](https://ibb.co/J5Dtq6Z)</br>
*Figure 1 - ATM Welcome Screen* </br></br>

**General Usage and Notes**</br>
- The program is written in Python and rendered in a text component of the TKinter framework.
- As of this revision the ATM interface no longer contains buttons, except for 'Cancel' and 'Clear' (Figure 1).  The numpad, side buttons, and 'Enter' have been removed.
- The gesture listener is currently mocked with a keyboard listener; enter key represents a hover gesture, and left/right arrows represent corresponding swipes.
- When executing the program on launch you will see the main welcome screen.  To advance to the main menu simply hover (press enter).

**PIN Entry**</br>
The User is presented with a carousel of numbers from 0-9 and can rotate between then from left to right (Figure 2).  It will go from 0 to 9 or vice versa in a continuous circular loop.  Stop on a number and hover (press enter) to enter a PIN digit.  The number will appear near the bottom.  Currently if you enter an incorrect number you must press the 'Clear' button to start over currently (this is the only functionality of that button).  The current correct PIN is **1234**.  If an invalid PIN is entered a message will be shown to the user and they can swipe left to try again (Figure 3).

![pin_iterator](https://ibb.co/yd5SDqm)</br>
*Figure 2 - PIN Iterator* </br></br>

![invalid_pin](https://ibb.co/4m77fTY)</br>
*Figure 3 - Invalid PIN message* </br></br>

**Main Menu Options**</br>
After proceeding past the welcome screen the user is presented with the main menu options which include deposit, withdrawal, and check balance (Figure 4):

![main_menu](https://ibb.co/ctDffq8)</br>
*Figure 4 - Main Menu* </br></br>
