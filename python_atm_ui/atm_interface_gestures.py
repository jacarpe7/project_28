# -*- coding: utf-8 -*-
"""
This generates a basic ATM interface for use in 
proximity sensor gesture recognition.
Created on Jan 27 2021
@author: Josh Carpenter, Michael Frederic
"""
import os
from tkinter import Tk, Frame, Button, Text, SUNKEN, DISABLED, NORMAL, END, PhotoImage
from pynput import keyboard
from rx.subject import AsyncSubject
from rx.core import Observable
from rx.subject import Subject

#DEBUG MODE - Set true to have debug comments in console.
debug = False

# GUI constants
B_PAD = 15
B_WIDTH = 8
B_HT = 4
BUTTON_X = 12
BUTTON_Y = 8

# boolean values for menu navigation and button enable/disable
initial_screen = True
pin_entry_screen = False
cancel_prompt = False
pin_valid = False
menu_present = False
withdrawal_prompt = False
deposit_prompt = False
deposit_options_prompt = False
another_trans_prompt = False
acct_balance_displayed = False
insufficient_funds = False
invalid_pin_msg = False

# variables related to gestures
HOVER = 0
LEFT_SWIPE = 1
RIGHT_SWIPE = 2
UP_SWIPE = 3

# pin values for gestures
global current, previous, after
current = 0
previous = 9
after = 1

# Gesture menu selection constants
main_menu_selection = None
DEPOSIT = 0
CHECK_BAL = 1
WITHDRAWAL = 2

deposit_menu_selection = None
CASH = 0
CHECK = 1

another_trans_selection = None
TRANS_YES = 0
TRANS_NO = 1

cancel_selection = None
CANCEL_NO = 0
CANCEL_YES = 1

# variables for capturing input & storing account balance
deposit_type = ""
pin_code = ""
correct_pin = "1234"
amount_entered = ""
acct_balance = 280
transaction_message = None

#gesture listener 
def on_press(key):
    try:
        keyListener.on_next(key)
        if debug:
            print('alphanumeric key {0} pressed'.format(
                key.char))
    except AttributeError:
        if debug:
            print('special key {0} pressed'.format(
                key))

def on_release(key):
    if debug:
        print('{0} released'.format(
            key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False
 
#observable declaration, SEE IMPLEMENTATION IN PIN MENU FOR EXAMPLE
keyListener = Subject()

#pynumpt keyboard listening subscription, this is monitoring key strokes
#Will need to remove when back-end data is ready.
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)

def gestureListener(observable: AsyncSubject){
    # obsevable.subscribe(lambda: x:)
}
#observable 

class Atm:
    """
    Constructor of the ATM class that creates all the GUI elements and layout:
        -- main LCD screen
        -- Clear and Cancel buttons
        -- sizing, padding, and display configurations
        -- initializes the listener
    """
    def __init__(self, root):
        self.root = root    
        root.title("ASU Capstone ATM Simulator")
        root.geometry("650x525")
      
        # ASU logo image
        base_folder = os.path.dirname(__file__)
        image_path = os.path.join(base_folder, 'asu_pitchfork.png')
        global asuLogo
        asuLogo = PhotoImage(file=image_path)


        # Create the main frames for the various sections on the UI
        center_frame = Frame(root, width=400, height=500, relief=SUNKEN)
        button_frame = Frame(root, width=800, height=250)
        
        # Grid layouts for the main window
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)
        
        center_frame.grid(row=0)
        button_frame.grid(row=1)
        
        # Create main LCD panel and add text
        root.main_lcd = Text(center_frame, height=23, width=70, \
            background="black", foreground="green")
        
        # Create config tags for main_lcd
        root.main_lcd.tag_configure("center", \
            justify='center', font="fixedsys 20", foreground = "green")
        root.main_lcd.tag_configure("left", \
            justify='left', font="fixedsys 20", foreground = "green")
        root.main_lcd.tag_configure("right", \
            justify='right', font="fixedsys 20", foreground = "green")
        root.main_lcd.tag_configure("left_selected", \
            justify='left', font="fixedsys 20", foreground = "blue")
        root.main_lcd.tag_configure("right_selected", \
            justify='right', font="fixedsys 20", foreground = "blue")
        root.main_lcd.tag_configure("center_selected", \
            justify='center', font="fixedsys 20", foreground = "blue")
        
        root.main_lcd.image_create("1.0", image=asuLogo)
        root.main_lcd.insert("2.0", "\nWelcome to the ASU ATM System\n")
        root.main_lcd.insert(END, "\n\nHover to begin")
        root.main_lcd.tag_add("center", "1.0", "end")
        root.main_lcd.grid(row=0, column=0, padx=5, pady=(25, 5))
        root.main_lcd.config(state=DISABLED)
        
        # Create buttons for num pad and add to center frame grid
        button_clear = Button(button_frame,text = "Clear", \
            width=B_WIDTH, height=B_HT, bg='yellow', command=clear)
        button_cancel = Button(button_frame,text = "Cancel", \
            width=B_WIDTH, height=B_HT, bg='red', command=cancel)
        button_clear.grid(row=0,column=0, padx=BUTTON_X,pady=BUTTON_Y)
        button_cancel.grid(row=0,column=1, padx=BUTTON_X,pady=BUTTON_Y)
        
        listener.start()
        if debug:  
            keyListener.subscribe(
                lambda x:print(navigation_gestures(x))) 
        else:
            keyListener.subscribe(
                lambda x:navigation_gestures(x))


# Define funtion for gesture navigation
def navigation_gestures(swipe):
    """
    Backbone of the program that is executed each time input is detected
    from the listener.  All the logic is contained here such that when
    listener input is detected it checks which screen the application is
    currently on based on the boolean gates and from there based on which
    input was detected the corresponding action will be executed.
    """
    global pin_entry_screen, menu_present, main_menu_selection, \
        deposit_menu_selection, acct_balance, deposit_options_prompt, \
        deposit_prompt, deposit_type, withdrawal_prompt, amount_entered, \
        acct_balance_displayed, another_trans_prompt, another_trans_selection, \
        transaction_message, pin_valid, pin_code, current, previous, after, \
        invalid_pin_msg, cancel_prompt, cancel_selection

    # Cancel prompt
    if cancel_prompt:
        if swipe is LEFT_SWIPE and cancel_selection == CANCEL_NO:
            cancel_selection = CANCEL_YES
            display_cancel_prompt()
        if swipe is RIGHT_SWIPE and cancel_selection == CANCEL_YES:
            cancel_selection = CANCEL_NO
            display_cancel_prompt()
        if swipe is HOVER:
            if cancel_selection == CANCEL_YES:
                cancel()
            if cancel_selection == CANCEL_NO:
                if menu_present:
                    display_main_menu()
                if pin_entry_screen:
                    gesture_pin_menu()
                if withdrawal_prompt:
                    display_gesture_withdrawal_prompt()
                if deposit_options_prompt:
                    display_deposit_options()
                if deposit_prompt:
                    display_gesture_deposit_prompt()
                if acct_balance_displayed:
                    display_gesture_deposit_prompt()
        return swipe
    # Initial screen menu
    if initial_screen:
        if swipe is HOVER:
            gesture_pin_menu()
        return swipe
    # PIN entry screen
    if pin_entry_screen:
        if swipe is RIGHT_SWIPE:
            current +=1
            after +=1
            previous +=1
            if current == 10:
                current = 0
            elif after == 10:
                after = 0
            elif previous == 10:
                previous = 0
            gesture_pin_menu()
        elif swipe is LEFT_SWIPE:
            current -=1
            after -=1
            previous -=1
            if current == -1:
                current = 9
            elif after == -1:
                after = 9
            elif previous == -1:
                previous = 9
            gesture_pin_menu()
        elif swipe is HOVER:
            if len(pin_code) < 4:
                pin_code = pin_code + str(current)
                gesture_pin_menu()
            if pin_code == correct_pin:
                pin_valid = True
                main_menu_selection = CHECK_BAL
                display_main_menu()
            elif len(pin_code) == 4:
                pin_code = ""
                current = 0
                previous = 9
                after = 1
                display_invalid_pin_msg()
        elif swipe is UP_SWIPE:
            cancel_selection = CANCEL_NO
            display_cancel_prompt()
        return swipe
    # Main menu
    if menu_present:
        if swipe is RIGHT_SWIPE:
            if main_menu_selection == DEPOSIT or main_menu_selection == CHECK_BAL:
                main_menu_selection = main_menu_selection + 1
                display_main_menu()
        if swipe is LEFT_SWIPE:
            if main_menu_selection == CHECK_BAL or main_menu_selection == WITHDRAWAL:
                main_menu_selection = main_menu_selection - 1
                display_main_menu()
        if swipe is HOVER:
            if main_menu_selection == DEPOSIT:
                deposit_menu_selection = CASH
                display_deposit_options()
            if main_menu_selection == WITHDRAWAL:
                display_gesture_withdrawal_prompt()
            if main_menu_selection == CHECK_BAL:
                display_acct_balance()
            main_menu_selection = CHECK_BAL
        if swipe is UP_SWIPE:
            cancel_selection = CANCEL_NO
            display_cancel_prompt()
        return swipe
    # Deposit Options menu
    if deposit_options_prompt:
        if swipe is RIGHT_SWIPE and deposit_menu_selection == CASH:
            deposit_menu_selection = deposit_menu_selection + 1
            display_deposit_options()
        if swipe is LEFT_SWIPE and deposit_menu_selection == CHECK:
            deposit_menu_selection = deposit_menu_selection - 1
            display_deposit_options()
        if swipe is HOVER:
            if deposit_menu_selection == CASH:
                deposit_type = "cash"
                display_gesture_deposit_prompt()
            if deposit_menu_selection == CHECK:
                deposit_type = "check"
                display_gesture_deposit_prompt()
        if swipe is UP_SWIPE:
            cancel_selection = CANCEL_NO
            display_cancel_prompt()
        return swipe
    # Deposit Menu
    if deposit_prompt:
        increment_value = 20
        if amount_entered == '' or None:
            amount_entered = '0'
        if swipe is RIGHT_SWIPE:
            if amount_entered == '300':
                if debug:
                    print(amount_entered) 
            else:
                amount_entered = str(int(amount_entered) + increment_value)
                if debug:
                    print(amount_entered + ' incrementing')
                display_gesture_deposit_prompt()
        if swipe is LEFT_SWIPE:
            if amount_entered == '0' or None:
                if debug:
                    print(amount_entered) 
            else:
                amount_entered = str(int(amount_entered) - increment_value)
                if debug:
                    print(amount_entered + ' decrementing')
                display_gesture_deposit_prompt()
        if swipe is HOVER:
            acct_balance = acct_balance + int(amount_entered)
            transaction_message = "Deposit successful"
            amount_entered = ""
            another_trans_selection = TRANS_NO
            display_another_trans_prompt()
        if swipe is UP_SWIPE:
            cancel_selection = CANCEL_NO
            display_cancel_prompt()
        return swipe
    # Withdrawal Menu
    if withdrawal_prompt:
        increment_value = 20
        if amount_entered == '' or None:
            amount_entered = '0'
        if swipe is RIGHT_SWIPE:
            if amount_entered == '300':
                if debug:
                    print(amount_entered)
                return 
            else:
                amount_entered = str(int(amount_entered) + increment_value)
                if debug:
                    print(amount_entered + ' incrementing')
                display_gesture_withdrawal_prompt()
        if swipe is LEFT_SWIPE:
            if amount_entered == '0' or None:
                if debug:
                    print(amount_entered)
                return 
            else:
                amount_entered = str(int(amount_entered) - increment_value)
                if debug:
                    print(amount_entered + ' decrementing')
                
                display_gesture_withdrawal_prompt()
        if swipe is HOVER:
            if int(amount_entered) <= int(acct_balance):
                acct_balance = acct_balance - int(amount_entered)
                transaction_message = "Please take your cash"
                amount_entered = ""
                another_trans_selection = TRANS_NO
                display_another_trans_prompt()
                return
            else:
                amount_entered = ""
                display_insufficient_funds()
        if swipe is UP_SWIPE:
            cancel_selection = CANCEL_NO
            display_cancel_prompt()
        return swipe
    #Check Balance screen
    if acct_balance_displayed:
        if swipe is LEFT_SWIPE:
            display_main_menu()
        if swipe is UP_SWIPE:
            cancel_selection = CANCEL_NO
            display_cancel_prompt()
        return swipe
    #Another transaction prompt
    if another_trans_prompt:
        if swipe is LEFT_SWIPE and another_trans_selection == TRANS_NO:
            another_trans_selection = TRANS_YES
            display_another_trans_prompt()
        if swipe is RIGHT_SWIPE and another_trans_selection == TRANS_YES:
            another_trans_selection = TRANS_NO
            display_another_trans_prompt()
        if swipe is HOVER:
            if another_trans_selection == TRANS_NO:
                pin_valid = False
                pin_code = ""
                amount_entered = ""
                current = 0
                previous = 9
                after = 1
                display_initial_screen()
            if another_trans_selection == TRANS_YES:
                display_main_menu()
        return swipe
    # Insufficient Funds screen
    if insufficient_funds:
        if swipe is LEFT_SWIPE:
            display_main_menu()
        return swipe
    # Invalid PIN Screen
    if invalid_pin_msg:
        if swipe is LEFT_SWIPE:
            gesture_pin_menu()
        return swipe
            

# Define method for pin entry screen.
def gesture_pin_menu():
    """
    Flips boolean gates used for navigation and displays the PIN carousel.
    """
    global menu_present, withdrawal_prompt, another_trans_prompt, \
        initial_screen, deposit_options_prompt, deposit_prompt, \
        acct_balance_displayed, current, previous, after, \
        pin_entry_screen, invalid_pin_msg, cancel_prompt
    pin_entry_screen = True
    initial_screen = False
    invalid_pin_msg = False
    menu_present = False
    withdrawal_prompt = False
    deposit_prompt = False
    another_trans_prompt = False
    deposit_options_prompt = False
    acct_balance_displayed = False
    cancel_prompt = False
    root.main_lcd.config(state=NORMAL)
    clear_tags()
    root.main_lcd.delete("1.0", END)
    root.main_lcd.insert("end", "\n\n{}\n".format(current))
    root.main_lcd.insert("1.0", "\n↓ Hover to select a # ↓\n\n\n\t\t  {}\t\t\t\t{}\n".format(previous, after))
    root.main_lcd.insert("end", "\n" + pin_code + "\n\n← Swipe left or right →")
    
    root.main_lcd.tag_add("center", "1.0", "3.0")
    root.main_lcd.tag_add("left", "4.0", "end-3l")
    root.main_lcd.tag_add("center_selected", "end-5l", "end-3l")
    root.main_lcd.tag_add("center", "end-3l", END) 


# Defines function to back to initial screen for PIN entry
def display_initial_screen():
    """
    Flips boolean gates used for navigation and displays initial screen of the
    application at launch.
    """
    global menu_present, withdrawal_prompt, another_trans_prompt, \
        initial_screen, deposit_options_prompt, deposit_prompt, \
        acct_balance_displayed, cancel_prompt, pin_entry_screen
    initial_screen = True
    pin_entry_screen = False
    menu_present = False
    withdrawal_prompt = False
    deposit_prompt = False
    another_trans_prompt = False
    deposit_options_prompt = False
    acct_balance_displayed = False
    cancel_prompt = False
    root.main_lcd.config(state=NORMAL)
    root.main_lcd.delete("1.0", END)
    root.main_lcd.image_create("1.0", image=asuLogo)
    root.main_lcd.insert("2.0", "\nWelcome to the ASU ATM System\n")
    root.main_lcd.insert(END, "\n\nHover to begin")
    root.main_lcd.tag_add("center", "1.0", "end")
    root.main_lcd.config(state=DISABLED)


# Defines function to show the main menu
def display_main_menu():
    """
    Flips boolean gates used for navigation and displays the
    main menu of the ATM.
    """
    global menu_present, withdrawal_prompt, another_trans_prompt, \
        initial_screen, deposit_options_prompt, deposit_prompt, \
        acct_balance_displayed, main_menu_selection, pin_entry_screen, \
        cancel_prompt
    initial_screen = False
    pin_entry_screen = False
    menu_present = True
    withdrawal_prompt = False
    deposit_prompt = False
    another_trans_prompt = False
    deposit_options_prompt = False
    acct_balance_displayed = False
    cancel_prompt = False
    root.main_lcd.config(state=NORMAL)
    root.main_lcd.delete("1.0", END)
    clear_tags()
    root.main_lcd.insert("1.0", "\n\n\n\n Deposit\t\t\t\t\t\tWithdrawal\n")
    root.main_lcd.insert("end", "\n\nCheck Balance\n")
    root.main_lcd.insert("end", "\n\n← Swipe left or right →")

    if main_menu_selection == DEPOSIT:
        root.main_lcd.tag_add("left_selected", "1.0", "1.0+12c")
        root.main_lcd.tag_add("left", "1.0+13c", "1.0+28c")
        root.main_lcd.tag_add("center", "1.0", END)

    if main_menu_selection == CHECK_BAL:
        root.main_lcd.tag_add("left", "1.0", "end-1l")
        root.main_lcd.tag_add("center_selected", "end-4l", "end-1l")
        root.main_lcd.tag_add("center", "end-1l", END) 

    if main_menu_selection == WITHDRAWAL:
        root.main_lcd.tag_add("left", "1.0", "1.0+12c")
        root.main_lcd.tag_add("left_selected", "1.0+13c", "1.0+28c")
        root.main_lcd.tag_add("center", "1.0", END)
    
    root.main_lcd.config(state=DISABLED)


# Defines function for deposit options
def display_deposit_options():
    """
    Flips boolean gates used for navigation after the user has selected option
    to 'Deposit' and then displays the corresponding menu to select deposit 
    type.
    """
    global menu_present, deposit_options_prompt, deposit_prompt, \
        deposit_menu_selection, cancel_prompt
    menu_present = False
    deposit_prompt = False
    deposit_options_prompt = True
    cancel_prompt = False
    root.main_lcd.config(state=NORMAL)
    root.main_lcd.delete("1.0", END)
    clear_tags()
    root.main_lcd.insert("1.0", "\n\n\n\nSelect Deposit Type:\n\n\n\t\tCash\t\t\tCheck")
    if deposit_menu_selection == CASH:
        root.main_lcd.tag_add("center", "1.0", "end")
        root.main_lcd.tag_add("left_selected", "7.0", "7.0+7c")
        root.main_lcd.tag_add("left", "end-5c", "end")
    if deposit_menu_selection == CHECK:
        root.main_lcd.tag_add("center", "1.0", "end")
        root.main_lcd.tag_add("left", "7.0", "7.0+7c")
        root.main_lcd.tag_add("left_selected", "end-6c", "end")
    root.main_lcd.config(state=DISABLED)


# Gesture withdrawal prompt
def display_gesture_withdrawal_prompt():
    """
    Flips boolean gates used for navigation after the user has selected option
    to 'Withdrawal' and then displays the corresponding menu to enter
    withdrawal amount.
    """
    global menu_present, withdrawal_prompt, amount_entered, cancel_prompt
    menu_present = False
    withdrawal_prompt = True
    cancel_prompt = False
    root.main_lcd.config(state=NORMAL)
    root.main_lcd.delete('1.0', END)
    root.main_lcd.insert('1.0', '\n\nEnter Amount to Withdrawal:\n')
    root.main_lcd.insert('4.0', "\n← Swipe Left/Right →\n\n ")
    root.main_lcd.insert('7.0', "\n$ {}" .format(amount_entered))
    root.main_lcd.tag_add("center", "1.0", "end")
    root.main_lcd.config(state=DISABLED)

# Gesture deposit prompt 
def display_gesture_deposit_prompt():
    """
    Flips boolean gates used for navigation after the user has selected 
    deposit type, and then displays the corresponding menu to enter the
    deposit amount.
    """
    global menu_present, deposit_prompt, amount_entered, \
        deposit_options_prompt, cancel_prompt
    menu_present = False
    deposit_options_prompt = False
    deposit_prompt = True
    cancel_prompt = False
    root.main_lcd.config(state=NORMAL)
    root.main_lcd.delete('1.0', END)
    root.main_lcd.insert('1.0', '\n\nEnter Amount to Deposit:\n')
    root.main_lcd.insert('4.0', "\n← Swipe Left/Right →\n\n ")
    root.main_lcd.insert('7.0', "\n$ {}" .format(amount_entered))
    root.main_lcd.tag_add("center", "1.0", "end")
    root.main_lcd.config(state=DISABLED)


# Define function to display current account balance
def display_acct_balance():
    """
    Flips boolean gates used for navigation after the user has selected option
    to show 'Account Balance', and then displays the current balance of the
    user's account.  Also includes an option to swipe left to go back to the 
    main screen.
    """
    global menu_present, acct_balance_displayed, acct_balance, cancel_prompt
    acct_balance_displayed = True
    menu_present = False
    cancel_prompt = False
    root.main_lcd.config(state=NORMAL)
    root.main_lcd.delete("1.0", END)
    root.main_lcd.insert("1.0", "\n\n\nYour account balance is:\n")
    root.main_lcd.insert("end", "\n$ " + str(acct_balance) + "\n\n\n\n\n← Swipe left to go back")
    root.main_lcd.tag_add("center", "1.0", END)
    root.main_lcd.config(state=DISABLED)


# Define funtion to display 'Another Transaction' prompt
def display_another_trans_prompt():
    """
    Flips boolean gates used for navigation after the user has completed
    a transaction, and displays to the user an option to do another
    transaction, or to exit and logout.  Also includes an option to swipe left
    to go back to the main screen.
    """
    global another_trans_prompt, deposit_prompt, withdrawal_prompt, \
        transaction_message, another_trans_selection
    another_trans_prompt = True
    deposit_prompt = False
    withdrawal_prompt = False 
    root.main_lcd.config(state=NORMAL)
    root.main_lcd.delete("1.0", END)
    root.main_lcd.insert("1.0", "\n\n\n" + transaction_message + "\n\n\nAnother transaction?\n\n\t\t\tYes\t\tNo")
    if another_trans_selection == TRANS_YES:
        root.main_lcd.tag_add("center", "1.0", "end-1l")
        root.main_lcd.tag_add("left_selected", "8.0", "8.0+7c")
        root.main_lcd.tag_add("left", "end-3c", "end")
    if another_trans_selection == TRANS_NO:
        root.main_lcd.tag_add("center", "1.0", "end-1l")
        root.main_lcd.tag_add("left", "8.0", "8.0+7c")
        root.main_lcd.tag_add("left_selected", "end-3c", "end")
    root.main_lcd.config(state=DISABLED)


# Define function to display message that there are insufficient funds
def display_insufficient_funds():
    """
    Flips boolean gates used for navigation after the user has attempted to
    withdrawal more fund than the user has in his/her account, and displays
    and message containing the same.  Also includes an option to swipe left
    to go back to the main screen.
    """
    global insufficient_funds, withdrawal_prompt
    insufficient_funds = True
    withdrawal_prompt = False
    root.main_lcd.config(state=NORMAL)
    root.main_lcd.delete("1.0", END)
    root.main_lcd.insert("1.0", "\n\n\n\n\nInsufficient Funds!\n")
    root.main_lcd.insert("end", "\n\n\n\n← Swipe left to go back")
    root.main_lcd.tag_add("center", "1.0", END)
    root.main_lcd.config(state=DISABLED)


# Define function to display a message when the PIN entered is incorrect
def display_invalid_pin_msg():
    """
    Flips boolean gates used for navigation after the user has entered an
    invalid PIN code, and displays a message containing the same.  Also
    includes an option to swipe left to go back to the pin entry screen
    to try again.
    """
    global invalid_pin_msg, pin_entry_screen
    invalid_pin_msg = True 
    pin_entry_screen = False
    root.main_lcd.config(state=NORMAL)
    root.main_lcd.delete("1.0", END)
    root.main_lcd.insert("1.0", "\n\n\n\n\nIncorrect PIN!\n")
    root.main_lcd.insert("end", "\n\n\n\n← Swipe left to try again")
    root.main_lcd.tag_add("center", "1.0", END)
    root.main_lcd.config(state=DISABLED)


# Define function to display cancel prompt after up swipe
def display_cancel_prompt():
    """
    Flips boolean gates used for navigation after the user has swiped up
    to cancel the current transaction, and displays a message containing
    confirmation yes/no prompt
    """
    global cancel_prompt, cancel_selection
    cancel_prompt = True
    root.main_lcd.config(state=NORMAL)
    root.main_lcd.delete("1.0", END)
    root.main_lcd.insert("1.0", "\n\n\nCancel Transaction\n\n\nAre you sure?\n\n\t\t\tYes\t\tNo")
    if cancel_selection == CANCEL_YES:
        root.main_lcd.tag_add("center", "1.0", "end-1l")
        root.main_lcd.tag_add("left_selected", "8.0", "8.0+7c")
        root.main_lcd.tag_add("left", "end-3c", "end")
    if cancel_selection == CANCEL_NO:
        root.main_lcd.tag_add("center", "1.0", "end-1l")
        root.main_lcd.tag_add("left", "8.0", "8.0+7c")
        root.main_lcd.tag_add("left_selected", "end-3c", "end")
    root.main_lcd.config(state=DISABLED)


# Define function for 'Cancel' button
def cancel():
    """
    Implementation for the 'Cancel' GUI button which logs the user out and
    returns back to the initial screen of the program.  This was added as
    a failsafe in case the gestures were misbehaving so that a user could
    still exit out of their account safely.
    """
    global pin_code, pin_valid, amount_entered, current, previous, after
    pin_valid = False
    pin_code = ""
    amount_entered = ""
    current = 0
    previous = 9
    after = 1
    display_initial_screen()
    

# Defines a function to remove all tags from the main_lcd
def clear_tags():
    """
    Clears all the tags from the main LCD screen that are initialized during
    the ATM constructor's execution.  Used in cases where it was necessary
    to get the following screen to render properly.
    """
    root.main_lcd.tag_remove("left", "1.0", "end")
    root.main_lcd.tag_remove("right", "1.0", "end")
    root.main_lcd.tag_remove("center", "1.0", "end")
    root.main_lcd.tag_remove("left_selected", "1.0", "end")
    root.main_lcd.tag_remove("right_selected", "1.0", "end")
    root.main_lcd.tag_remove("center_selected", "1.0", "end")


# Define function for the 'Clear' button (to clear PIN for now)
def clear():
    """
    Implementation for the 'Clear' GUI button which only works on the PIN 
    entry screen and clears any digits already entered by the user so they
    can start over.
    """
    global pin_code
    if pin_entry_screen:
        pin_code = ""
        gesture_pin_menu()

def main():
    root = Tk()
    gui = Atm(root)
    root.mainloop()

# Entry point to initiate the program for execution    
if __name__ == '__main__':
    main()