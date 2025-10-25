'''
Week 10 | Graphical User Interface (GUI) - Part (2) Homework
NOTED: Check the path of the attatched picture before running the code
'''

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime

price = {"Thai Tea": 40, "Milk Tea": 35, "Matcha": 60, "Drip Coffee": 30}
count = {"Thai Tea": 0, "Milk Tea": 0, "Matcha": 0, "Drip Coffee": 0}
que = 0

def update_clock(clock_label):
    """Updates the clock label every second."""
    now = datetime.now()
    time_string = now.strftime("%H:%M:%S")
    clock_label.config(text=time_string)
    clock_label.after(1000, update_clock, clock_label)

def clear_order():
    
    for item in count:
        count[item] = 0

    button1.config(text=f"Thai Tea 40THB")
    button2.config(text=f"Milk Tea 35THB")
    button3.config(text=f"Matcha 60THB")
    button4.config(text=f"Drip Coffee 30THB")
    print("Order has been cleared.")

def count_order(item):
    count[item] += 1
    if item == "Thai Tea":
        button1.config(text=f"Thai Tea 40THB ({count['Thai Tea']})")
    elif item == "Milk Tea":
        button2.config(text=f"Milk Tea 35THB ({count['Milk Tea']})")
    elif item == "Matcha":
        button3.config(text=f"Matcha 60THB ({count['Matcha']})")
    elif item == "Drip Coffee":
        button4.config(text=f"Drip Coffee 30THB ({count['Drip Coffee']})")

def order_cost():
    global que
    que +=1
    total_cost = 0
    order_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    receipt = f"------------- Your Order ({que}) -------------"+"\n"
    receipt += f"Date & Time: {order_time}"+"\n"
    
    for item, quantity in count.items():
        if quantity > 0:
            item_cost = price[item] * quantity
            receipt += f"{item}: {quantity} x {price[item]} THB = {item_cost} THB\n"
            total_cost += item_cost
            
    receipt += f"\n------------- Total: {total_cost} THB -------------"
    
    messagebox.showinfo("Order Receipt", receipt)
    clear_order()

def menu_display():
    menu_window = tk.Tk()
    menu_window.title("Restaurant Menu")
    menu_window.geometry('915x430')
    menu_window.resizable(False, False)
    menu_window.config(bg='#ffffff')
    
    pic1 = tk.PhotoImage(file='pic/1.png')
    pic2 = tk.PhotoImage(file='pic/2.png')
    pic3 = tk.PhotoImage(file='pic/3.png')
    pic4 = tk.PhotoImage(file='pic/4.png')

    global button1, button2, button3, button4, button5
    
    label1 = tk.Label(menu_window, text="Night Cafe for Software Engineer",font=("Arial", 13),width=30,bg='#0091FF',fg='#FFFFFF')
    label1.grid(row=0, column=2, columnspan=2, pady=20)
    
    clock_label = tk.Label(menu_window,width=30)
    clock_label.grid(row=1, column=2, columnspan=2, pady=10)
    update_clock(clock_label)
    
    button1 = tk.Button(menu_window, text="Thai Tea 40THB", image=pic1, compound="top", command=lambda: count_order("Thai Tea"))
    button1.grid(row=3, column=1, padx=10, pady=10)
    
    button2 = tk.Button(menu_window, text="Milk Tea 35THB", image=pic2, compound="top", command=lambda: count_order("Milk Tea"))
    button2.grid(row=3, column=2, padx=10, pady=10)
    
    button3 = tk.Button(menu_window, text="Matcha 60THB", image=pic3, compound="top", command=lambda: count_order("Matcha"))
    button3.grid(row=3, column=3, padx=10, pady=10)
    
    button4 = tk.Button(menu_window, text="Drip Coffee 30THB", image=pic4, compound="top", command=lambda: count_order("Drip Coffee"))
    button4.grid(row=3, column=4, padx=10, pady=10)

    button5 = tk.Button(menu_window, text="Submit Order", bg="#0091FF",fg='#FFFFFF', width=15, command=order_cost)
    button5.grid(row=4, column=2, columnspan=2, pady=20)
    
    button6 = tk.Button(menu_window, text="Clear Order", bg='#FF5733', fg='#FFFFFF', width=15, command=clear_order)
    button6.grid(row=4, column=2, pady=20)

    button7 = tk.Button(menu_window, text="Close Window", width=15, command=lambda: menu_window.destroy())
    button7.grid(row=4, column=3, pady=20)
    
    menu_window.mainloop()

menu_display()
    

