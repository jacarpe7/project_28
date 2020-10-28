# -*- coding: utf-8 -*-
"""
This generates a basic ATM interface for use in 
proximity sensor gesture recognition.

Created on Oct 28 11:36:59 2020
@author: Josh Carpenter
"""

import tkinter as tk
     
b_pad = 7

atm = tk.Tk()
atm.title("ASU Capstone ATM Simulator")
atm.geometry("800x800")

left_frame = tk.Frame(master=atm)
center_frame = tk.Frame(master=atm, relief=tk.SUNKEN)
right_frame = tk.Frame(master=atm)
numpad_frame = tk.Frame(master=atm)

button_1L = tk.Button(master=left_frame,text = "L1",width=10,height=5)
button_2L = tk.Button(master=left_frame,text = "L2",width=10,height=5)
button_3L = tk.Button(master=left_frame,text = "L3",width=10,height=5)
button_4L = tk.Button(master=left_frame,text = "L4",width=10,height=5)

button_1L.pack(padx=b_pad,pady=b_pad)
button_2L.pack(padx=b_pad,pady=b_pad)
button_3L.pack(padx=b_pad,pady=b_pad)
button_4L.pack(padx=b_pad,pady=b_pad)

button_1R = tk.Button(master=right_frame,text = "R1",width=10,height=5)
button_2R = tk.Button(master=right_frame,text = "R2",width=10,height=5)
button_3R = tk.Button(master=right_frame,text = "R3",width=10,height=5)
button_4R = tk.Button(master=right_frame,text = "R4",width=10,height=5)

button_1R.pack(padx=b_pad,pady=b_pad)
button_2R.pack(padx=b_pad,pady=b_pad)
button_3R.pack(padx=b_pad,pady=b_pad)
button_4R.pack(padx=b_pad,pady=b_pad)

left_frame.pack(side=tk.LEFT,fill=tk.BOTH)
#center_frame.pack()
right_frame.pack(side=tk.RIGHT,fill=tk.BOTH)

atm.mainloop()

