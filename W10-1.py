import tkinter as tk
from tkinter import messagebox
def login():
    username = user.get()
    messagebox.showinfo("Alert Message:",f"welcome {username}")
    print(f"{username} login successful")
    root.destroy()
def display_login_window():
    global user
    global code
    global root
    root = tk.Tk()
    root.title("CMD")
    root.geometry('400x200')
    input_frame = tk.Frame(root)
    input_frame.pack(pady=20)
    password_frame = tk.Frame(root)
    password_frame.pack(pady=5)
    label = tk.Label(input_frame,text="System Login")
    label.pack(side="top",pady=10)
    label = tk.Label(input_frame, text="Username:")
    label.pack(side="left")
    user = tk.Entry(input_frame, width=30)
    user.pack(padx=10,side="left")
    button = tk.Button(root, text="Submit", command=login)
    button.pack(pady=15)
    button = tk.Button(root, text="destroy", command=root.destroy)
    button.pack(pady=15)
    root.mainloop()
display_login_window()

