# Python ATM Interface
### Revision 3/18/2021

**General Usage and Notes**</br>
- The program is written in Python and rendered in a text component of the TKinter framework.
- As of this revision the ATM interface no longer contains buttons, except for 'Cancel' and 'Clear'.  The numpad, side buttons, and 'Enter' have been removed.
- The gesture listener is currently mocked with a keyboard listener; enter key represents a hover gesture, and left/right arrows represent corresponding swipes.
- When executing the program on launch you will see the main welcome screen.  To advance to the main menu simply hover (press enter).

**PIN Entry**</br>
The User is presented with a carousel of numbers from 0-9 and can rotate between then from left to right (Figure 2).  It will go from 0 to 9 or vice versa in a continuous circular loop.  Stop on a number and hover (press enter) to enter a PIN digit.  The number will appear near the bottom.  Currently if you enter an incorrect number you must press the 'Clear' button to start over currently (this is the only functionality of that button).  The current correct PIN is **1234**.  If an invalid PIN is entered a message will be shown to the user and they can swipe left to try again.

**Main Menu Options**</br>
After proceeding past the welcome screen the user is presented with the main menu options which include deposit, withdrawal, and check balance.

**Withdrawal**</br>
After selecting withdrawal from the main menu screen the user will be presented with a screen to input a withdrawal amount ranging from $0 to $300.  This is presented as a text entry where left/right swipes will increment or decrement by $20. If you are at $0 or $300 dollars it will no longer decrement or increment, respectively.  If the user tries to withdrawal more money that is in the account an 'Insufficient Funds' message will be shown and the user must swipe left to go back to the main menu.  After withdrawaling a message will show stating that the withdrawal was successful and to take the cash.  It will prompt the user if they want another transaction.  Selecting 'Yes' will take them back to the main menu and selecting 'No' will log the user out and take them back to the welcome screen. 

**Deposit**</br>
After selecting deposit from the main menu screen the user will first be asked what kind of deposit, cash or check.  simply arrow/gesture left or right to select the correct option and hover. From there the same exact input screen for withdrawal is shown for entering in the dollar amount.  Also after selecting the amount to deposit the workflow is the same as withdrawal; the user will be asked if they want another transaction and can respond accordingly.

**Check Balance**</br>
The 'Check Balance' menu option does just that - it displays the current account balance to the user along with a message to swipe left to go back to the main menu.  The balance reflects all transactions completed during the current runtime execution of the program and will be reset to $280 if the program is terminated and executed again.

**Cancel button**</br>
The 'Cancel' button purpose is in case the user is having issues with gesture entry it can provide the ability to completely exit the system, logout, and terminate any current transaction in progress (This type of behavior is not currently modeled by gestures)