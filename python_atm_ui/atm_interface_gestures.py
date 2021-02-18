# -*- coding: utf-8 -*-
"""
This generates a basic ATM interface for use in 
proximity sensor gesture recognition.
Created on Oct 28 11:36:59 2020
@author: Josh Carpenter, Michael Frederic
"""

from tkinter import Tk, Frame, Button, Text, SUNKEN, DISABLED, NORMAL, END
from pynput import keyboard
from rx.subject import AsyncSubject
from rx.core import Observable
from rx.subject import Subject

#DEBUG MODE - Set true to have debug comments in console.
debug = True

# GUI constants
B_PAD = 15
B_WIDTH = 8
B_HT = 4
NUM_PAD_X = 12
NUM_PAD_Y = 8

# boolean values for menu navigation and button enable/disable
initial_screen = True
pin_entry_screen = False
cancel_pressed = False
pin_valid = False
menu_present = False
withdrawal_prompt = False
deposit_prompt = False
deposit_options_prompt = False
another_trans_prompt = False
acct_balance_displayed = False
insufficient_funds = False

# variables related to gestures
HOVER = 0
LEFT_SWIPE = 1
RIGHT_SWIPE = 2

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

# variables for capturing input & storing account balance
deposit_type = ""
pin_code = ""
correct_pin = "1234"
amount_entered = ""
acct_balance = 1000
transaction_message = None

#keyboard listener 
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

#pynumpt keyboard listening subscription, this is what is monitoring key strokes
#Will need to remove when back-end data is ready.
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)

class Atm:
    
    def __init__(self, root):
        self.root = root    
        root.title("ASU Capstone ATM Simulator")
        root.geometry("800x800")

        # Create the main frames for the various sections on the UI
        left_frame = Frame(root,width=150,height=500)
        center_frame = Frame(root, width=400,height=500,relief=SUNKEN)
        right_frame = Frame(root,width=150,height=500)
        numpad_frame = Frame(root,width=800,height=300)
        
        # Grid layouts for the main window
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)
        
        left_frame.grid(row=0,sticky="nw")
        center_frame.grid(row=0)
        right_frame.grid(row=0,sticky="ne")
        numpad_frame.grid(row=1)
        
        # Create buttons on left side of main LCD and add to grid
        button_1L = Button(left_frame,text = "L1",width=B_WIDTH,height=B_HT)
        button_2L = Button(left_frame,text = "L2",width=B_WIDTH,height=B_HT)
        button_3L = Button(left_frame,text = "L3",width=B_WIDTH,height=B_HT)
        button_4L = Button(left_frame,text = "L4",width=B_WIDTH,height=B_HT)
        
        button_1L.grid(row=0,column=0,padx=B_PAD,pady=B_PAD)
        button_2L.grid(row=1,column=0,padx=B_PAD,pady=B_PAD)
        button_3L.grid(row=2,column=0,padx=B_PAD,pady=B_PAD)
        button_4L.grid(row=3,column=0,padx=B_PAD,pady=B_PAD)
        
        # Create main LCD panel and add text
        root.main_lcd = Text(center_frame,height=23,width=70,background="black",foreground="green")
        
        # Create config tags for main_lcd
        root.main_lcd.tag_configure("center", justify='center', font="fixedsys 20", foreground = "green")
        root.main_lcd.tag_configure("left", justify='left', font="fixedsys 20", foreground = "green")
        root.main_lcd.tag_configure("right", justify='right', font="fixedsys 20", foreground = "green")
        root.main_lcd.tag_configure("left_selected", justify='left', font="fixedsys 20", foreground = "blue")
        root.main_lcd.tag_configure("right_selected", justify='right', font="fixedsys 20", foreground = "blue")
        root.main_lcd.tag_configure("center_selected", justify='center', font="fixedsys 20", foreground = "blue")
        
        root.main_lcd.insert("1.0", "\n\n\n\nWelcome to the ASU ATM System\n")
        root.main_lcd.insert(END, "\n\nHover to begin")
        root.main_lcd.tag_add("center", "1.0", "end")
        root.main_lcd.grid(row=0, column=0,padx=5,pady=5)
        root.main_lcd.config(state=DISABLED)
        
        # Create buttons on right side of main LCD and add to grid
        button_1R = Button(right_frame,text = "R1",width=B_WIDTH,height=B_HT)
        button_2R = Button(right_frame,text = "R2",width=B_WIDTH,height=B_HT)
        button_3R = Button(right_frame,text = "R3",width=B_WIDTH,height=B_HT)
        button_4R = Button(right_frame,text = "R4",width=B_WIDTH,height=B_HT)
        
        button_1R.grid(row=0,column=0,padx=B_PAD,pady=B_PAD)
        button_2R.grid(row=1,column=0,padx=B_PAD,pady=B_PAD)
        button_3R.grid(row=2,column=0,padx=B_PAD,pady=B_PAD)
        button_4R.grid(row=3,column=0,padx=B_PAD,pady=B_PAD)
        
        # Create buttons for num pad and add to center frame grid
        button_num_1 = Button(numpad_frame,text = "1",width=B_WIDTH,height=B_HT)
        button_num_2 = Button(numpad_frame,text = "2",width=B_WIDTH,height=B_HT)
        button_num_3 = Button(numpad_frame,text = "3",width=B_WIDTH,height=B_HT)
        button_num_4 = Button(numpad_frame,text = "4",width=B_WIDTH,height=B_HT)
        button_num_5 = Button(numpad_frame,text = "5",width=B_WIDTH,height=B_HT)
        button_num_6 = Button(numpad_frame,text = "6",width=B_WIDTH,height=B_HT)
        button_num_7 = Button(numpad_frame,text = "7",width=B_WIDTH,height=B_HT)
        button_num_8 = Button(numpad_frame,text = "8",width=B_WIDTH,height=B_HT)
        button_num_9 = Button(numpad_frame,text = "9",width=B_WIDTH,height=B_HT)
        button_num_0 = Button(numpad_frame,text = "0",width=B_WIDTH,height=B_HT)
        button_num_enter = Button(numpad_frame,text = "Enter",width=B_WIDTH,height=B_HT,bg='green')
        button_num_clear = Button(numpad_frame,text = "Clear",width=B_WIDTH,height=B_HT,bg='yellow',command=clear)
        button_num_cancel = Button(numpad_frame,text = "Cancel",width=B_WIDTH,height=B_HT,bg='red',command=cancel)
        
        button_num_1.grid(row=0,column=0, padx=NUM_PAD_X,pady=NUM_PAD_Y)
        button_num_2.grid(row=0,column=1, padx=NUM_PAD_X,pady=NUM_PAD_Y)
        button_num_3.grid(row=0,column=2, padx=NUM_PAD_X,pady=NUM_PAD_Y)
        button_num_4.grid(row=1,column=0, padx=NUM_PAD_X,pady=NUM_PAD_Y)
        button_num_5.grid(row=1,column=1, padx=NUM_PAD_X,pady=NUM_PAD_Y)
        button_num_6.grid(row=1,column=2, padx=NUM_PAD_X,pady=NUM_PAD_Y)
        button_num_7.grid(row=2,column=0, padx=NUM_PAD_X,pady=NUM_PAD_Y)
        button_num_8.grid(row=2,column=1, padx=NUM_PAD_X,pady=NUM_PAD_Y)
        button_num_9.grid(row=2,column=2, padx=NUM_PAD_X,pady=NUM_PAD_Y)
        button_num_0.grid(row=3,column=1, padx=NUM_PAD_X,pady=NUM_PAD_Y)
        button_num_enter.grid(row=0,column=3, padx=NUM_PAD_X,pady=NUM_PAD_Y)
        button_num_clear.grid(row=1,column=3, padx=NUM_PAD_X,pady=NUM_PAD_Y,)
        button_num_cancel.grid(row=2,column=3, padx=NUM_PAD_X,pady=NUM_PAD_Y)
        
        listener.start()
        if debug:  
            keyListener.subscribe(
                lambda x:print(navigation_gestures(x))) 
        else:
            keyListener.subscribe(
                lambda x:navigation_gestures(x))

# Function for main entry into navigation for gestures
def navigation_gestures(key):
    global pin_entry_screen, menu_present, main_menu_selection, deposit_menu_selection, acct_balance, \
        deposit_options_prompt, deposit_prompt, deposit_type, withdrawal_prompt, amount_entered, \
        acct_balance_displayed, another_trans_prompt, another_trans_selection, transaction_message, \
        pin_valid, pin_code, current, previous, after

    # Initial screen menu
    if initial_screen:
        if key is keyboard.Key.enter:
            gesture_pin_menu()
            return key
    # PIN entry screen
    if pin_entry_screen:
        pin_iterator(key)
        return key
    # Main menu
    if menu_present:
        if key is keyboard.Key.right:
            if main_menu_selection == DEPOSIT or main_menu_selection == CHECK_BAL:
                main_menu_selection = main_menu_selection + 1
                display_main_menu()
        if key is keyboard.Key.left:
            if main_menu_selection == CHECK_BAL or main_menu_selection == WITHDRAWAL:
                main_menu_selection = main_menu_selection - 1
                display_main_menu()
        if key is keyboard.Key.enter:
            if main_menu_selection == DEPOSIT:
                deposit_menu_selection = CASH
                display_deposit_options()
            if main_menu_selection == WITHDRAWAL:
                display_gesture_withdrawal_prompt()
            if main_menu_selection == CHECK_BAL:
                display_acct_balance()
            main_menu_selection = CHECK_BAL
        return key
    # Deposit Options menu
    if deposit_options_prompt:
        if key is keyboard.Key.right and deposit_menu_selection == CASH:
            deposit_menu_selection = deposit_menu_selection + 1
            display_deposit_options()
        if key is keyboard.Key.left and deposit_menu_selection == CHECK:
            deposit_menu_selection = deposit_menu_selection - 1
            display_deposit_options()
        if key is keyboard.Key.enter:
            if deposit_menu_selection == CASH:
                deposit_type = "cash"
                display_deposit_prompt()
            if deposit_menu_selection == CHECK:
                deposit_type = "check"
                display_deposit_prompt()
        return key
    # Deposit Menu
    if deposit_prompt:
        # TODO implement key listener logic for deposit
        increment_value = 20
        limit = 300
        if key is keyboard.Key.right:
            if amount_entered == limit:
                return 
            else:
                amount_entered = str(int(amount_entered) + increment_value)
        if key is keyboard.Key.left:
            if amount_entered == 0 or None:
                return 
            else:
                amount_entered = str(int(amount_entered) - increment_value)
                display_deposit_prompt()
        if key is keyboard.Key.enter:
            acct_balance = acct_balance + int(amount_entered)
            transaction_message = "Deposit successful"
            amount_entered = ""
            another_trans_selection == TRANS_NO
            display_another_trans_prompt()
            return 
        return 
    # Withdrawal Menu
    if withdrawal_prompt:
        # TODO implement key listener logic for withdrawal
        increment_value = 20
        if amount_entered == '' or None:
            amount_entered = '0'
        if key is keyboard.Key.right:
            if amount_entered == '300':
                if debug:
                    print(amount_entered)
                return 
            else:
                amount_entered = str(int(amount_entered) + increment_value)
                if debug:
                    print(amount_entered + ' incrementing')
                display_gesture_withdrawal_prompt()
        if key is keyboard.Key.left:
            if amount_entered == '0' or None:
                if debug:
                    print(amount_entered)
                return 
            else:
                amount_entered = str(int(amount_entered) - increment_value)
                if debug:
                    print(amount_entered + ' decrementing')
                
                display_gesture_withdrawal_prompt()
        if key is keyboard.Key.enter:
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
        return key
    #Check Balance screen
    if acct_balance_displayed:
        if key is keyboard.Key.left:
            display_main_menu()
        return key
    #Another transaction prompt
    if another_trans_prompt:
        if key is keyboard.Key.left and another_trans_selection == TRANS_NO:
            another_trans_selection = TRANS_YES
            display_another_trans_prompt()
        if key is keyboard.Key.right and another_trans_selection == TRANS_YES:
            another_trans_selection = TRANS_NO
            display_another_trans_prompt()
        if key is keyboard.Key.enter:
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
        return key


# Define method for PIN entry
def pin_iterator(key):
    global current, previous, after, pin_code, pin_valid, main_menu_selection
    if key is keyboard.Key.right:
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

    elif key is keyboard.Key.left:
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
    
    elif key is keyboard.Key.enter:
        if len(pin_code) < 4:
            pin_code = pin_code + str(current)
            gesture_pin_menu()
        if pin_code == correct_pin:
            pin_valid = True
            main_menu_selection = CHECK_BAL
            display_main_menu()

        
# Define function for pin entry screen
def gesture_pin_menu():
    global menu_present, withdrawal_prompt, another_trans_prompt, initial_screen, \
        deposit_options_prompt, deposit_prompt, acct_balance_displayed, \
        current, previous, after, pin_entry_screen
    initial_screen = False
    pin_entry_screen = True
    menu_present = False
    withdrawal_prompt = False
    deposit_prompt = False
    another_trans_prompt = False
    deposit_options_prompt = False
    acct_balance_displayed = False
    root.main_lcd.config(state=NORMAL)
    clear_tags()
    root.main_lcd.delete("1.0", END)
    root.main_lcd.insert("end", "\n\n{}\n".format(current))
    root.main_lcd.insert("1.0", "\n↓ Hover to select a # ↓\n\n\n\t\t  {}\t\t\t\t{}\n" .format(previous, after))
    root.main_lcd.insert("end", "\n" + pin_code + "\n\n← Swipe left or right →")
    
    root.main_lcd.tag_add("center", "1.0", "3.0")
    root.main_lcd.tag_add("left", "4.0", "end-3l")
    root.main_lcd.tag_add("center_selected", "end-5l", "end-3l")
    root.main_lcd.tag_add("center", "end-3l", END) 


# Defines function to back to initial screen for PIN entry
def display_initial_screen():
    global menu_present, withdrawal_prompt, another_trans_prompt, initial_screen, \
        deposit_options_prompt, deposit_prompt, acct_balance_displayed
    initial_screen = True
    menu_present = False
    withdrawal_prompt = False
    deposit_prompt = False
    another_trans_prompt = False
    deposit_options_prompt = False
    acct_balance_displayed = False
    root.main_lcd.config(state=NORMAL)
    root.main_lcd.delete("1.0", END)
    root.main_lcd.insert("1.0", "\n\n\n\nWelcome to the ASU ATM System\n")
    root.main_lcd.insert(END, "\n\nHover to begin")
    root.main_lcd.tag_add("center", "1.0", "end")
    root.main_lcd.config(state=DISABLED)


# Defines function to show the main menu
def display_main_menu():
    global menu_present, withdrawal_prompt, another_trans_prompt, initial_screen, \
        deposit_options_prompt, deposit_prompt, acct_balance_displayed, \
        main_menu_selection, pin_entry_screen
    initial_screen = False
    pin_entry_screen = False
    menu_present = True
    withdrawal_prompt = False
    deposit_prompt = False
    another_trans_prompt = False
    deposit_options_prompt = False
    acct_balance_displayed = False

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
    global menu_present, deposit_options_prompt, deposit_prompt, deposit_menu_selection
    menu_present = False
    deposit_prompt = False
    deposit_options_prompt = True

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


# [WIP] gesture withdrawal prompt 
def display_gesture_withdrawal_prompt():
    global menu_present, withdrawal_prompt, amount_entered
    menu_present = False
    withdrawal_prompt = True
    root.main_lcd.config(state=NORMAL)
    root.main_lcd.delete('1.0', END)
    root.main_lcd.insert('1.0', '\n\nEnter Amount to Withdrawal:\n')
    root.main_lcd.insert('4.0', "\n← Swipe Left/Right →\n\n ")
    root.main_lcd.insert('7.0', "\n$ {}" .format(amount_entered))
    root.main_lcd.tag_add("center", "1.0", "end")
    root.main_lcd.config(state=DISABLED)


# Defines function to display the deposit funds prompt
def display_deposit_prompt():
    global deposit_options_prompt, deposit_prompt, deposit_type
    deposit_prompt = True
    deposit_options_prompt = False
    root.main_lcd.config(state=NORMAL)
    root.main_lcd.delete("1.0", END)
    root.main_lcd.insert("1.0", "\n\n\n\nEnter " + deposit_type + " deposit amount:\n")
    root.main_lcd.insert(END, "\n$ ")
    root.main_lcd.tag_add("center", "1.0", "end")
    root.main_lcd.config(state=DISABLED)


# Define function to display current account balance
def display_acct_balance():
    global menu_present, acct_balance_displayed, acct_balance
    acct_balance_displayed = True
    menu_present = False
    root.main_lcd.config(state=NORMAL)
    root.main_lcd.delete("1.0", END)
    root.main_lcd.insert("1.0", "\n\n\nYour account balance is:\n")
    root.main_lcd.insert("end", "\n$ " + str(acct_balance) + "\n\n\n\n\n← Swipe left to go back")
    root.main_lcd.tag_add("center", "1.0", END)
    root.main_lcd.config(state=DISABLED)


# Define funtion to display 'Another Transaction' prompt
def display_another_trans_prompt():
    global another_trans_prompt, deposit_prompt, withdrawal_prompt, transaction_message, another_trans_selection
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
    global insufficient_funds, withdrawal_prompt
    insufficient_funds = True
    withdrawal_prompt = False
    root.main_lcd.delete("end-1l", END)
    root.main_lcd.insert(END, "\n" + msg + ", Press 'Clear'")
    root.main_lcd.tag_configure("center", justify='center', font="fixedsys 20")
    root.main_lcd.tag_add("center", "1.0", "end")


    # Define function for 'Cancel' button
def cancel():
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
    root.main_lcd.tag_remove("left", "1.0", "end")
    root.main_lcd.tag_remove("right", "1.0", "end")
    root.main_lcd.tag_remove("center", "1.0", "end")
    root.main_lcd.tag_remove("left_selected", "1.0", "end")
    root.main_lcd.tag_remove("right_selected", "1.0", "end")
    root.main_lcd.tag_remove("center_selected", "1.0", "end")


# Define function for the 'Clear' button (to clear PIN for now)
def clear():
    global pin_code
    if pin_entry_screen:
        pin_code = ""
        gesture_pin_menu()


# Entry point to initiate the program for execution    
if __name__ == '__main__':
    root = Tk()
    gui = Atm(root)
    root.mainloop()