
import tkinter as tk
import requests as r

user = None

def make(root, back):
    global user 
    weatherForm = tk.Frame(root, bg="blue")
    
    weatherForm.bind("<Button-3>", back)
    
    label1 = tk.Label(weatherForm, text="-- °C",
      fg="white", bg="blue",font=("Arial",25))
    label1.place(x = 80, y = 330)
    
    label2 = tk.Label(weatherForm, text="-- %RH",
      fg="white", bg="blue",font=("Arial",25))
    label2.place(x = 230, y = 330)
    
    
    label3 = tk.Label(weatherForm, text="",
      fg="white", bg="blue",font=("Arial",18))
    label3.place(x=0, y = 0)
    
    
    def update():
        label3.config(text=f"Welcome {user['name']}")
        label3.update_idletasks()
        x = int((400 - label3.winfo_width()) / 2)
        label3.place(x=x, y = 380)
    
    def run():
        data =r.get("https://cdn.ituring.ir/weather/today").json()
        status = data["status"]
        image = tk.PhotoImage(file=f"./ax/{status}.png")
        labelax.config(image=image)
        labelax.image = image
        
        temp = data["temperature"]
        label1.config(text=f"{temp} °C")
        
        hum = data["humidity"]
        label2.config(text=f"{hum} %RH")
        
    button = tk.Button(weatherForm, command=run,text="Update", width=30)
    button.place(x = 90,y = 290 )
    
    image = tk.PhotoImage(file="./ax/clear.png")
    labelax = tk.Label(weatherForm, image=image, bg="blue")
    labelax.config(image=image)
    labelax.image = image
    labelax.place(x =70, y = 30)
    
    return (weatherForm, update)
