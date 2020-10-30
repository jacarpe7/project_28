# -*- coding: utf-8 -*-
"""
This generates a basic ATM interface for use in 
proximity sensor gesture recognition.

Created on Oct 28 11:36:59 2020
@author: Josh Carpenter
"""

import tkinter as tk
     
b_pad = 15
b_width = 8
b_ht = 4

atm = tk.Tk()
atm.title("ASU Capstone ATM Simulator")
atm.geometry("800x800")

# Create the main frames for the various sections on the UI
left_frame = tk.Frame(atm,width=150,height=500)
center_frame = tk.Frame(atm, width=400,height=500,relief=tk.SUNKEN)
right_frame = tk.Frame(atm,width=150,height=500)
numpad_frame = tk.Frame(atm,width=800,height=300)

# Grid layouts for the main window
atm.grid_rowconfigure(1, weight=1)
atm.grid_columnconfigure(0, weight=1)

left_frame.grid(row=0,sticky="nw")
center_frame.grid(row=0)
right_frame.grid(row=0,sticky="ne")
numpad_frame.grid(row=1)

# Create buttons on left side of main LCD and add to grid
button_1L = tk.Button(left_frame,text = "L1",width=b_width,height=b_ht)
button_2L = tk.Button(left_frame,text = "L2",width=b_width,height=b_ht)
button_3L = tk.Button(left_frame,text = "L3",width=b_width,height=b_ht)
button_4L = tk.Button(left_frame,text = "L4",width=b_width,height=b_ht)

button_1L.grid(row=0,column=0,padx=b_pad,pady=b_pad)
button_2L.grid(row=1,column=0,padx=b_pad,pady=b_pad)
button_3L.grid(row=2,column=0,padx=b_pad,pady=b_pad)
button_4L.grid(row=3,column=0,padx=b_pad,pady=b_pad)

# Create main LCD panel and add text
main_lcd = tk.Text(center_frame,width=70,background="black",foreground="green")
main_lcd.tag_configure("center", justify='center', font="fixedsys 20")
main_lcd.insert("1.0", "\n\n\n\nWelcome to the ASU ATM System")
main_lcd.tag_add("center", "1.0", "end")
main_lcd.grid(row=0, column=0,padx=5,pady=5)
main_lcd.config(state=tk.DISABLED)

# Create buttons on right side of main LCD and add to grid
button_1R = tk.Button(right_frame,text = "R1",width=b_width,height=b_ht)
button_2R = tk.Button(right_frame,text = "R2",width=b_width,height=b_ht)
button_3R = tk.Button(right_frame,text = "R3",width=b_width,height=b_ht)
button_4R = tk.Button(right_frame,text = "R4",width=b_width,height=b_ht)

button_1R.grid(row=0,column=0,padx=b_pad,pady=b_pad)
button_2R.grid(row=1,column=0,padx=b_pad,pady=b_pad)
button_3R.grid(row=2,column=0,padx=b_pad,pady=b_pad)
button_4R.grid(row=3,column=0,padx=b_pad,pady=b_pad)

# Create buttons for num pad and add to center frame grid
button_num_1 = tk.Button(numpad_frame,text = "1",width=b_width,height=b_ht)
button_num_2 = tk.Button(numpad_frame,text = "2",width=b_width,height=b_ht)
button_num_3 = tk.Button(numpad_frame,text = "3",width=b_width,height=b_ht)
button_num_4 = tk.Button(numpad_frame,text = "4",width=b_width,height=b_ht)
button_num_5 = tk.Button(numpad_frame,text = "5",width=b_width,height=b_ht)
button_num_6 = tk.Button(numpad_frame,text = "6",width=b_width,height=b_ht)
button_num_7 = tk.Button(numpad_frame,text = "7",width=b_width,height=b_ht)
button_num_8 = tk.Button(numpad_frame,text = "8",width=b_width,height=b_ht)
button_num_9 = tk.Button(numpad_frame,text = "9",width=b_width,height=b_ht)
button_num_0 = tk.Button(numpad_frame,text = "0",width=b_width,height=b_ht)
button_num_enter = tk.Button(numpad_frame,text = "Enter",width=b_width,height=b_ht,bg='green')
button_num_clear = tk.Button(numpad_frame,text = "Clear",width=b_width,height=b_ht,bg='yellow')
button_num_cancel = tk.Button(numpad_frame,text = "Cancel",width=b_width,height=b_ht,bg='red')

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

atm.mainloop()

