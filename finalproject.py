"""

Author:  Eric Valle
Date written: 07/15/24
Assignment:   Final Project
Short Desc:   

"""
#Importing necessary libraries for GUI
import tkinter as tk

def openNewWindow():
	
	# Toplevel object which will 
	# be treated as a new window
	newWindow = Toplevel(root)
  
	# sets the title of the
	# Toplevel widget
	newWindow.title("New Window")

	# sets the geometry of toplevel
	newWindow.geometry("200x200")

	# A Label widget to show in toplevel
	newWindow.Label(newWindow, text ="This is a new window").pack()

#Create the main window with title Guessing Game
root = tk.Tk()
root.title("Marty's Music")

#Title Label
title_label = tk.Label(root, text="Marty's Music", font=('Helvetica', 20))
title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

#Button to open new window
btn = Button(root, text ="Click to open a new window", 
             command = openNewWindow)



root.mainloop()
top.mainloop()

"""
# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import *
from tkinter.ttk import *

# creates a Tk() object
master = Tk()

# sets the geometry of main 
# root window
master.geometry("200x200")


# function to open a new window 
# on a button click
def openNewWindow():
	
	# Toplevel object which will 
	# be treated as a new window
	newWindow = Toplevel(master)

	# sets the title of the
	# Toplevel widget
	newWindow.title("New Window")

	# sets the geometry of toplevel
	newWindow.geometry("200x200")

	# A Label widget to show in toplevel
	Label(newWindow, 
		text ="This is a new window").pack()


label = Label(master, 
			text ="This is the main window")

label.pack(pady = 10)

# a button widget which will open a 
# new window on button click
btn = Button(master, 
			text ="Click to open a new window", 
			command = openNewWindow)
btn.pack(pady = 10)

# mainloop, runs infinitely
mainloop()

"""


