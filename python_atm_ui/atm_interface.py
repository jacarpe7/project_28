# -*- coding: utf-8 -*-
"""
This generates a basic ATM interface for use in 
proximity sensor gesture recognition.

Created on Oct 28 11:36:59 2020
@author: Josh Carpenter
"""

from tkinter import Tk, Frame, Button, Text, SUNKEN, DISABLED, NORMAL, END

b_pad = 15
b_width = 8
b_ht = 4

initial_screen = True
cancel_pressed = False
pin_valid = False
menu_present = False
withdrawal_prompt = False
another_trans_prompt = False
invalid_msg = False

pin_code = ""
correct_pin = "4589"
amount_entered = ""
acct_balance = 1495.27

class atm:
    
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
        button_1L = Button(left_frame,text = "L1",width=b_width,height=b_ht,command=withdrawal)
        button_2L = Button(left_frame,text = "L2",width=b_width,height=b_ht)
        button_3L = Button(left_frame,text = "L3",width=b_width,height=b_ht)
        button_4L = Button(left_frame,text = "L4",width=b_width,height=b_ht)
        
        button_1L.grid(row=0,column=0,padx=b_pad,pady=b_pad)
        button_2L.grid(row=1,column=0,padx=b_pad,pady=b_pad)
        button_3L.grid(row=2,column=0,padx=b_pad,pady=b_pad)
        button_4L.grid(row=3,column=0,padx=b_pad,pady=b_pad)
        
        # Create main LCD panel and add text
        root.main_lcd = Text(center_frame,height=23,width=70,background="black",foreground="green")
        root.main_lcd.tag_configure("center", justify='center', font="fixedsys 20")
        root.main_lcd.insert("1.0", "\n\n\n\nWelcome to the ASU ATM System")
        root.main_lcd.insert(END, "\n\nEnter PIN to continue...\n\n")
        root.main_lcd.tag_add("center", "1.0", "end")
        root.main_lcd.grid(row=0, column=0,padx=5,pady=5)
        root.main_lcd.config(state=DISABLED)
        
        # Create buttons on right side of main LCD and add to grid
        button_1R = Button(right_frame,text = "R1",width=b_width,height=b_ht)
        button_2R = Button(right_frame,text = "R2",width=b_width,height=b_ht)
        button_3R = Button(right_frame,text = "R3",width=b_width,height=b_ht,command=yes)
        button_4R = Button(right_frame,text = "R4",width=b_width,height=b_ht,command=no)
        
        button_1R.grid(row=0,column=0,padx=b_pad,pady=b_pad)
        button_2R.grid(row=1,column=0,padx=b_pad,pady=b_pad)
        button_3R.grid(row=2,column=0,padx=b_pad,pady=b_pad)
        button_4R.grid(row=3,column=0,padx=b_pad,pady=b_pad)
        
        # Create buttons for num pad and add to center frame grid
        button_num_1 = Button(numpad_frame,text = "1",width=b_width,height=b_ht,command=lambda: input_num("1"))
        button_num_2 = Button(numpad_frame,text = "2",width=b_width,height=b_ht,command=lambda: input_num("2"))
        button_num_3 = Button(numpad_frame,text = "3",width=b_width,height=b_ht,command=lambda: input_num("3"))
        button_num_4 = Button(numpad_frame,text = "4",width=b_width,height=b_ht,command=lambda: input_num("4"))
        button_num_5 = Button(numpad_frame,text = "5",width=b_width,height=b_ht,command=lambda: input_num("5"))
        button_num_6 = Button(numpad_frame,text = "6",width=b_width,height=b_ht,command=lambda: input_num("6"))
        button_num_7 = Button(numpad_frame,text = "7",width=b_width,height=b_ht,command=lambda: input_num("7"))
        button_num_8 = Button(numpad_frame,text = "8",width=b_width,height=b_ht,command=lambda: input_num("8"))
        button_num_9 = Button(numpad_frame,text = "9",width=b_width,height=b_ht,command=lambda: input_num("9"))
        button_num_0 = Button(numpad_frame,text = "0",width=b_width,height=b_ht,command=lambda: input_num("0"))
        button_num_enter = Button(numpad_frame,text = "Enter",width=b_width,height=b_ht,bg='green',command=enter)
        button_num_clear = Button(numpad_frame,text = "Clear",width=b_width,height=b_ht,bg='yellow',command=clear)
        button_num_cancel = Button(numpad_frame,text = "Cancel",width=b_width,height=b_ht,bg='red',command=cancel)
        
        button_num_1.grid(row=0,column=0, padx=12,pady=8)
        button_num_2.grid(row=0,column=1, padx=12,pady=8)
        button_num_3.grid(row=0,column=2, padx=12,pady=8)
        button_num_4.grid(row=1,column=0, padx=12,pady=8)
        button_num_5.grid(row=1,column=1, padx=12,pady=8)
        button_num_6.grid(row=1,column=2, padx=12,pady=8)
        button_num_7.grid(row=2,column=0, padx=12,pady=8)
        button_num_8.grid(row=2,column=1, padx=12,pady=8)
        button_num_9.grid(row=2,column=2, padx=12,pady=8)
        button_num_0.grid(row=3,column=1, padx=12,pady=8)
        button_num_enter.grid(row=0,column=3, padx=12,pady=8)
        button_num_clear.grid(row=1,column=3, padx=12,pady=8)
        button_num_cancel.grid(row=2,column=3, padx=12,pady=8)
    
# Define function for entering the PIN from the numeric keypad
def input_num(num):
    root.main_lcd.config(state=NORMAL)
    global pin_code, withdrawal_prompt, amount_entered, initial_screen, \
        another_trans_prompt, invalid_msg
    if not invalid_msg and not another_trans_prompt:
        if len(pin_code) < 4 and initial_screen:
            root.main_lcd.insert(END, num)
            pin_code = pin_code + num
        if withdrawal_prompt and len(amount_entered) < 4:
            root.main_lcd.insert(END, num)
            amount_entered = amount_entered + num
    root.main_lcd.config(state=DISABLED)

# Define function for the 'Clear' button
def clear():
    root.main_lcd.config(state=NORMAL)
    global pin_valid, pin_code, withdrawal_prompt, cancel_pressed, \
        amount_entered, another_trans_prompt
    if not pin_valid and not cancel_pressed:
        display_initial_screen()
        pin_code = ""
    elif withdrawal_prompt and not another_trans_prompt:
        display_withdrawal_prompt()
        amount_entered = ""
    root.main_lcd.config(state=DISABLED)
    
# Define function for the 'Enter' button
def enter():
    root.main_lcd.config(state=NORMAL)
    global pin_valid, pin_code, correct_pin, cancel_pressed, withdrawal_prompt, \
        amount_entered, acct_balance, another_trans_prompt, invalid_msg
    if pin_code == correct_pin and not pin_valid and not cancel_pressed:
        pin_valid = True
        display_main_menu()
    elif pin_code != correct_pin and not cancel_pressed:
        display_invalid_msg("Invalid PIN")
    elif withdrawal_prompt and len(amount_entered) > 0:
        if int(amount_entered) % 20 != 0:
            display_invalid_msg("Invalid entry")
        elif int(amount_entered) > acct_balance:
            display_invalid_msg("Insufficient funds")
        else:
            acct_balance = acct_balance - int(amount_entered)
            amount_entered = ""
            root.main_lcd.delete("1.0", END)
            root.main_lcd.tag_configure("center", justify='center', font="fixedsys 20")
            root.main_lcd.insert("1.0", "\n\n\n\nPlease take your cash\n\n")
            root.main_lcd.insert(END, "Another transaction?")
            root.main_lcd.tag_add("center", "1.0", "end")
            root.main_lcd.tag_configure("right", justify='right', font="fixedsys 20")
            root.main_lcd.insert("end", "\n\tYes\n\n\n\n\tNo")
            root.main_lcd.tag_add("right", "end-5l", END)
            another_trans_prompt = True
    root.main_lcd.config(state=DISABLED)
    
# Define function for 'Cancel' button
def cancel():
    global cancel_pressed, menu_present, another_trans_prompt, invalid_msg, initial_screen
    if not another_trans_prompt and not invalid_msg and not initial_screen:
        cancel_pressed = True
        menu_present = False
        root.main_lcd.config(state=NORMAL)
        root.main_lcd.delete("1.0", END)
        root.main_lcd.tag_configure("center", justify='center', font="fixedsys 20")
        root.main_lcd.insert("1.0", "\n\n\n\nCancel - Are you sure?")
        root.main_lcd.tag_add("center", "1.0", "end")
        root.main_lcd.tag_configure("right", justify='right', font="fixedsys 20")
        root.main_lcd.insert("end", "\n\n\n\tYes\n\n\n\n\tNo")
        root.main_lcd.tag_add("right", "end-5l", END)
        root.main_lcd.config(state=DISABLED)
    
# Define function for 'Yes' button (R3)
def yes():
    global cancel_pressed, pin_code, pin_valid, amount_entered
    root.main_lcd.config(state=NORMAL)
    if cancel_pressed:
        display_initial_screen()
        cancel_pressed = False
        pin_valid = False
        pin_code = ""
        amount_entered = ""
    elif another_trans_prompt:
        display_main_menu()
    root.main_lcd.config(state=DISABLED)
        
# Define function for 'No' button (R4)
def no():
    global cancel_pressed, pin_valid, pin_code, menu_present, \
        withdrawal_prompt, amount_entered
    root.main_lcd.config(state=NORMAL)
    if cancel_pressed:
        if withdrawal_prompt:
            display_withdrawal_prompt()
            amount_entered = ""
        elif pin_valid:
            display_main_menu()
        elif not pin_valid:
            display_initial_screen()
            pin_code = ""
        cancel_pressed = False
    elif another_trans_prompt:
        display_initial_screen()
        pin_valid = False
        pin_code = ""
        amount_entered = ""
    root.main_lcd.config(state=DISABLED)
    
# Define funtion to withdrawal funds from account
def withdrawal():
    global menu_present, withdrawal_prompt
    if menu_present:
        root.main_lcd.config(state=NORMAL)
        display_withdrawal_prompt()
        root.main_lcd.config(state=DISABLED)
    
# Defines function to show the main menu
def display_main_menu():
    global menu_present, withdrawal_prompt, another_trans_prompt, invalid_msg, initial_screen
    initial_screen = False
    menu_present = True
    withdrawal_prompt = False
    another_trans_prompt = False
    invalid_msg = False
    root.main_lcd.delete("1.0", END)
    root.main_lcd.insert("1.0", "\nWithdrawal Funds\n\n\nDeposit Funds\n\n\nCheck Account Balance")
    root.main_lcd.tag_configure("left", justify='left', font="fixedsys 20")
    root.main_lcd.tag_add("left", "1.0", "end")
    
# Defines function to back to initial screen for PIN entry
def display_initial_screen():
    global menu_present, withdrawal_prompt, another_trans_prompt, invalid_msg, initial_screen
    initial_screen = True
    menu_present = False
    withdrawal_prompt = False
    another_trans_prompt = False
    invalid_msg = False
    root.main_lcd.delete("1.0", END)
    root.main_lcd.tag_configure("center", justify='center', font="fixedsys 20")
    root.main_lcd.insert("1.0", "\n\n\n\nWelcome to the ASU ATM System")
    root.main_lcd.insert(END, "\n\nEnter PIN to continue...\n\n")
    root.main_lcd.tag_add("center", "1.0", "end")    
    
# Defines function to display the withdrawal funds prompt
def display_withdrawal_prompt():
    global menu_present, withdrawal_prompt, another_trans_prompt, invalid_msg, initial_screen
    initial_screen = False
    menu_present = False
    withdrawal_prompt = True
    another_trans_prompt = False
    invalid_msg = False
    root.main_lcd.delete("1.0", END)
    root.main_lcd.tag_configure("center", justify='center', font="fixedsys 20")
    root.main_lcd.insert("1.0", "\n\n\n\nEnter Amount to Withdrawal:\n")
    root.main_lcd.insert(END, "(Multiples of $20)\n\n$ ")
    root.main_lcd.tag_add("center", "1.0", "end")
    
# Define function to clear last line and display specified invalid message
def display_invalid_msg(msg):
    global invalid_msg
    root.main_lcd.delete("end-1l", END)
    root.main_lcd.insert(END, "\n" + msg + ", Press 'Clear'")
    root.main_lcd.tag_configure("center", justify='center', font="fixedsys 20")
    root.main_lcd.tag_add("center", "1.0", "end")
    invalid_msg = True

# Entry point to initiate the program for execution    
if __name__ == '__main__':
    root = Tk()
    gui = atm(root)
    root.mainloop()
