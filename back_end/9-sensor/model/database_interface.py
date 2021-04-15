#!/usr/bin/env python
# coding: utf-8

# In[14]:


import sqlite3
import os

DB_PATH = os.path.abspath('bank_db')


# In[15]:


def check_balance(uuid):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute('SELECT balance FROM userinfo WHERE uuid = (?)', (uuid,))
    return cur.fetchone()


# In[16]:


def check_pin(uuid, pin):
    print(DB_PATH)
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute('SELECT * FROM userinfo WHERE uuid = (?) AND pin = (?)', (uuid,pin,))
    return cur.fetchone()
    


# In[17]:


def withdraw(uuid, amount):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute('SELECT balance FROM userinfo WHERE uuid = (?)', (uuid,))
    current_amount = cur.fetchone()[0]
    if (current_amount - amount) < 0:
        return False
    else:
        new_amount = current_amount - amount
        print(new_amount)
        cur.execute('UPDATE userinfo SET balance = (?) WHERE uuid= (?)', (new_amount, uuid,))
        con.commit()
        return True


# In[18]:

def deposit(new_amount):
    uuid = "123456789"
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute('UPDATE userinfo SET balance = (?) WHERE uuid= (?)', (new_amount, uuid,))
    return

#Example Functions
print(check_pin("123456789", 1234))
print(check_balance("123456789"))
print(withdraw("123456789", 5))
print(check_balance("123456789"))


# In[ ]:




