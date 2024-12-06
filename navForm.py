
import tkinter as tk
import requests as r


def make(root, nav_to_weather, nav_to_tether):

    bg = "#cde8c3"
    navForm = tk.Frame(root, bg=bg)
    
    
    image = tk.PhotoImage(file="./ax/tether.png")
    labelax = tk.Label(navForm, image=image, bg=bg)
    labelax.config(image=image)
    labelax.image = image
    labelax.place(x =(400-150)//2, y = 20)
    labelax.bind("<Button-1>", nav_to_tether)
    
    lblPrice = tk.Label(navForm, text="قیمت دلار", bg=bg,font=("B Nazanin",25))
    lblPrice.place(x = 0, y = 0)
    lblPrice.update_idletasks()
    lblPrice.place(x = (400 - lblPrice.winfo_width()) // 2, y = 180)
    
    
    
    image1 = tk.PhotoImage(file="./ax/weather.png")
    labelax1 = tk.Label(navForm, image=image1, bg=bg)
    labelax1.config(image=image1)
    labelax1.image = image1
    labelax1.place(x =(400-150)//2, y = 240)
    labelax1.bind("<Button-1>", nav_to_weather)
    
    lblWeather = tk.Label(navForm, text="آب و هوا", bg=bg,font=("B Nazanin",25))
    lblWeather.place(x = 0, y = 0)
    lblWeather.update_idletasks()
    lblWeather.place(x = (400 - lblWeather.winfo_width()) // 2, y = 400)
    
    
    return navForm
