
import tkinter as tk
import requests as r


def make(root, back):

    json = (r.get("https://api.tetherland.com/currencies").json())
    price = json["data"]["currencies"]["USDT"]["price"]
    diff24d = json["data"]["currencies"]["USDT"]["diff24d"]
    diff7d = json["data"]["currencies"]["USDT"]["diff7d"]
    diff30d	 = json["data"]["currencies"]["USDT"]["diff30d"]
    
    bg = "#cde8c3"
    tetherForm = tk.Frame(root, bg=bg)
    

        
    tetherForm.bind("<Button-3>", back)
    
    lblPrice = tk.Label(tetherForm, text="قیمت تتر: "+str(price), bg=bg,font=("B Nazanin",25))
    lblPrice.place(x = 0, y = 0)
    lblPrice.update_idletasks()
    lblPrice.place(x = (400 - lblPrice.winfo_width()) // 2, y = 200)
    


    lblYes = tk.Label(tetherForm, text="٪"+ "تغییرات ۲۴ ساعت: "+str(diff24d), bg=bg,font=("B Nazanin",20))
    lblYes.place(x = 0, y = 0)
    lblYes.update_idletasks()
    lblYes.place(x = (400 - lblYes.winfo_width()) // 2, y = 250)
    
    
    
    lblWeek = tk.Label(tetherForm, text="٪"+ "تغییرات ۷ روز گذشته: "+str(diff7d), bg=bg,font=("B Nazanin",20))
    lblWeek.place(x = 0, y = 0)
    lblWeek.update_idletasks()
    lblWeek.place(x = (400 - lblWeek.winfo_width()) // 2, y = 300)
    
    
    lblMonth = tk.Label(tetherForm, text="٪"+ "تغییرات ماه گذشته: "+str(diff30d), bg=bg,font=("B Nazanin",20))
    lblMonth.place(x = 0, y = 0)
    lblMonth.update_idletasks()
    lblMonth.place(x = (400 - lblMonth.winfo_width()) // 2, y = 350)
    
    
    
    image = tk.PhotoImage(file="./ax/tether.png")
    labelax = tk.Label(tetherForm, image=image, bg=bg)
    labelax.config(image=image)
    labelax.image = image
    labelax.place(x =(400-150)//2, y = 30)
    
    return tetherForm
