from asyncio import set_child_watcher
from pickle import READONLY_BUFFER
import tkinter.ttk as ttk
from tkinter import *
from tkinter import simpledialog
from random import *
window = Tk()
window.title("Passgen")
window.geometry("400x400")
import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUWXYZabcdefghijklmnopqrstuvwxyz"
alphanum = "ABCDEFGHIJKLMNOPQRSTUWXYZabcdefghijklmnopqrstuvwxyz0123456789~`!@#$%^&*()-=+_\\|}{][.,<>:;'/?"
from random import randint
from math import ceil
setch = IntVar()
setch.set(1)
d = alphanum
def genpass():
    global setch, lower, upper, alphanum, d
    passd = ""
    if setch.get() == 0:
        d = lower
    elif setch.get() == 1:
        d = upper
    else:
        d = alphanum
    leng = 8
    for i in range(0, leng, 1):
        passd += d[randint(0, (len(d)-1))]
    e1["state"] = NORMAL
    e1.delete(0, END)
    e1.insert(0, passd)
    e1.config(state="readonly")
    return passd
def encrypt(text):
    global setch, lower, upper, alphanum, d
    encrypted = ""
    for char in text:
        of = d.find(char)
        newof = ((of + 13) - 10) % len(d)
        encrypted += d[newof]
    return encrypted
def decrypt(text):
    decrypted = ""
    for char in text:
        of = d.find(char)
        newof = ((of - 13) + 10)
        decrypted += d[newof]
    return decrypted
s = ttk.Style()
s.configure('Test.TRadiobutton', foreground='#FF0000')
ss = ttk.Style()
ss.configure('Test1.TRadiobutton', foreground='#000000')
def copyy():
    global window, e1
    window.clipboard_clear()
    window.clipboard_append(e1.get())
def coppy():
    global window, e2
    window.clipboard_clear()
    window.clipboard_append(e2.get())
def chcolor():
    global setch, rb1, rb2, rb3, s
    if setch.get() == 0:
        rb1.configure(style='Test.TRadiobutton')
        rb2.configure(style='Test1.TRadiobutton')
        rb3.configure(style='Test1.TRadiobutton')
    elif setch.get() == 1:
        rb1.configure(style='Test1.TRadiobutton')
        rb2.configure(style='Test.TRadiobutton')
        rb3.configure(style='Test1.TRadiobutton')
    else:
        rb1.configure(style='Test1.TRadiobutton')
        rb2.configure(style='Test1.TRadiobutton')
        rb3.configure(style='Test.TRadiobutton')
def encr():
    global e1, e2, e3, encrypt
    encrypted = encrypt(e1.get())
    e2.configure(state="normal")
    e2.delete(0, END)
    e2.insert(0, encrypted)
    e2.configure(state="readonly")
def decr():
    global e2, e3, decrypt
    decrypted = decrypt(e2.get())
    e2.configure(state="normal")
    e2.delete(0, END)
    e2.insert(0, decrypted)
    e2.configure(state="readonly")
e1 = Entry(window, state="readonly", fg='#000000')
e2 = Entry(window, fg="#000000", state="readonly")
btn1 = Button(window, text="Copy", command=copyy)
btn2 = Button(window, text="Generate", command=lambda: genpass())
btn3 = Button(window, text="Copy", command=coppy)
btn4 = Button(window, text="Encrypt", command=lambda: encr())
btn5 = Button(window, text="Decrypt", command=decr)
rb = IntVar()
rb.set(1)
rb1 = ttk.Radiobutton(window, text="Low", value=0, var=setch)
rb2 = ttk.Radiobutton(window, text="Medium", value=1, var=setch, style='Test.TRadiobutton')
rb3 = ttk.Radiobutton(window, text="Strong", value=2, var=setch)
lbl1 = Label(window, text="Password: ")
lbl3 = Label(window, text="Encrypt: ")
rb.trace('w', lambda event, e, g: chcolor())
lbl1.grid(column=0, row=0)
e1.grid(column=1, row=0)
btn1.grid(column=2, row=0)
btn2.grid(column=3, row=0)
rb1.grid(column=0, row=1)
rb2.grid(column=1, row=1)
rb3.grid(column=2, row=1)
lbl3.grid(column=0, row=2)
e2.grid(column=1, row=2)
btn3.grid(column=2, row=2)
btn4.grid(column=3, row=2)
btn5.grid(column=4, row=2)
window.mainloop()