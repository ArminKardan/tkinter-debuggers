
import tkinter as tk
import requests as r
from tkinter import messagebox
import credForm as cred
import weatherForm as weather
import tetherForm as tether
import navForm as nav

users = [
    {"name":"Armin", "username":"armin", "password":"1234"},
    {"name":"Ali", "username":"ali", "password":"1111"},
    {"name":"Hassan", "username":"hassan_h", "password":"12345678"},
    {"name":"Hamid", "username":"hmd", "password":"hamidwow"},
]

page = None
user = None
root = tk.Tk()
root.title("Weather App")
root.configure(bg="blue")
root.geometry("400x480")


def onloginrequest(u):
    global user
    global page
    user = u
    weather.user = u
    updateWeather()
    page = "nav"
    refreshPage()
    
def back(e):
    global page
    page = "nav"
    refreshPage()
    
credForm = cred.make(root, users, onloginrequest)
weatherForm, updateWeather = weather.make(root, back)
tetherForm = tether.make(root, back)

def nav_to_weather(e):
    global page
    page = "weather"
    refreshPage()
    
def nav_to_tether(e):
    global page
    page = "tether"
    refreshPage()
        
navForm = nav.make(root, nav_to_weather, nav_to_tether)

def refreshPage():
    global user
    if user == None:
        weatherForm.pack_forget()
        tetherForm.pack_forget()
        navForm.pack_forget()
        credForm.pack(fill="both", expand=True)
    elif page == "nav":
        weatherForm.pack_forget()
        tetherForm.pack_forget()
        credForm.pack_forget()
        navForm.pack(fill="both", expand=True)
    elif page == "weather":
        navForm.pack_forget()
        tetherForm.pack_forget()
        credForm.pack_forget()
        weatherForm.pack(fill="both", expand=True)
    elif page == "tether":
        navForm.pack_forget()
        weatherForm.pack_forget()
        credForm.pack_forget()
        tetherForm.pack(fill="both", expand=True)


refreshPage()

root.mainloop()


