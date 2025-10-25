'''
Week 09 | Graphical User Interface (GUI) using Tkinter Module
'''

import tkinter as tk
root = tk.Tk() # Create a window
root.geometry('400x300+200+200') #Window size
root.title("HOMEWORK-GUI") #title of the window
root_bg_color = "#C0BCBD"
root.configure(bg=root_bg_color)

label1 = tk.Label(text="Name: Raphee Rattanamanoonporn",fg='black',font=("Arial","10"),bg='#FFC107') #Create a label (Capital L)
label2 = tk.Label(text="M.4 Major: E-AI",fg='black',font=("Arial","10"),bg='#8BC34A') #Create another label
label3 = tk.Label(text=" ",bg='#e75491')
label4 = tk.Label(text=" ",bg='#e2495b')
label5 = tk.Label(text=" ",bg='#e466a9')
label6 = tk.Label(text=" ",bg='#C62828')
label7 = tk.Label(text="SPSM ",bg='white')
label8 = tk.Label(text="OK",bg='black',fg='white',font=("Arial","10"))

# label1.pack(anchor='nw',fill='x') #Place the label in the window
# label2.pack(anchor='nw',fill='x') #Place the second label in the window
label1.place(height=35,width=400,x=0,y=0) #Place the first label at specific position
label2.place(height=35,width=400,x=0,y=35) #Place the
label3.place(height=95,width=95,x=0,y=70) #Place the third label at specific position
label4.place(height=95,width=95,x=101,y=70) #Place the fourth label at specific position
label5.place(height=95,width=95,x=202,y=70) #Place the fourth label at specific position
label6.place(height=95,width=95,x=305,y=70) #Place the fourth label at specific position
label7.place(height=35,width=400,x=0,y=175) #Place the fourth label at specific position
label8.place(height=35,width=150,x=125,y=215) #Place the fourth label at specific position


root.mainloop() #stay open until closed by user (always at the end)
