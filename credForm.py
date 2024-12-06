

import tkinter as tk
from tkinter import messagebox

def make(root, users, onloginrequest):
        
    credForm = tk.Frame(root)
    
    imagelock = tk.PhotoImage(file="./ax/lock.png")
    labellock = tk.Label(credForm, image=imagelock)
    labellock.config(image=imagelock)
    labellock.image = imagelock
    labellock.place(x =90, y = 30)
    
    
    labelusername = tk.Label(credForm, text="Username:")
    labelusername.place(x=68, y= 280)
    
    username = tk.Entry(credForm, width=40)
    username.place(x=70, y= 300)
    
    labelpassword = tk.Label(credForm, text="Password:")
    labelpassword.place(x=68, y= 330)
    
    password = tk.Entry(credForm, width=40, show="*")
    password.place(x=70, y= 350)
    
    
    def onlogin():
        usr = username.get()
        pwd = password.get()
        for u in users:
            if u["username"] == usr and u["password"] == pwd:
                onloginrequest(u)
                break
        else:
            messagebox.showerror("Wrong username or password", "you entered wrong username and password.")
    
    
    loginbutton = tk.Button(credForm, text="Login", width=30, command=onlogin)
    loginbutton.place(x=79, y= 380)
    
    return credForm
