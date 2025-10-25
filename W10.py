import tkinter as tk


def printtotal():
    print("Button 1 clicked")

def menu_display():
    menu_window = tk.Tk()
    menu_window.title("Restaurant Menu")
    menu_window.geometry('1500x600')

    pic1 = tk.PhotoImage(file='east.png')
    pic2 = tk.PhotoImage(file='north.png')
    pic3 = tk.PhotoImage(file='south.png')
    pic4 = tk.PhotoImage(file='west.png')

    global button1
    global button2      
    global button3
    global button4

    button1 = tk.Button(menu_window, text="North", image=pic1, compound="top",command=printtotal)
    button1.grid(row=0,column=1)
    button2 = tk.Button(menu_window, text="East", image=pic2, compound="top")
    button2.grid(row=0,column=2)
    button3 = tk.Button(menu_window, text="West", image=pic4, compound="top")
    button3.grid(row=0,column=3)
    button4 = tk.Button(menu_window, text="South", image=pic3, compound="top")
    button4.grid(row=0,column=4)

    total_pts = tk.StringVar()
    count = 0
    total_pts.set(f"pts = {count}")
    
    menu_window.mainloop()

menu_display()

