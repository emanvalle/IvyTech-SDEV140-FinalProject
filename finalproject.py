"""

Author:  Eric Valle
Date written: 07/15/24
Assignment:   Final Project
Short Desc:   

"""
#Importing necessary libraries for GUI
import tkinter as tk

#Create the main window with title Guessing Game
root = tk.Tk()
root.title("Marty's Music")

#Title Label
title_label = tk.Label(root, text="Marty's Music", font=('Helvetica', 20))
title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)


