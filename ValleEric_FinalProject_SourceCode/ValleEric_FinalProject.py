"""

Author:  Eric Valle
Date written: 07/15/24
Assignment:   Final Project
Short Desc:   The program displays a GUI to showcase Marty's Music. The GUI consists of two windows.

"""
#Importing necessary libraries for GUI
from tkinter import *
import tkinter as tk
import PIL
from PIL import ImageTk, Image # type: ignore

#Function openNewWindow to open a new window
def openPhotoGalleryWindow():
	# Toplevel object decalred as new_window
	new_window = Toplevel(root)
	new_window.title("Marty's Music - Photo Gallery")

	#GUI frame to organize GUI elements
	collage_frame = tk.Frame(new_window)
	collage_frame.pack(pady=10, padx=10)

	#Label describing photos displayed in new window
	photo_gallery_description = "These images were taken during the Bridgeport Music Festival in October 2022"
	photo_gallery_label = tk.Label(collage_frame, text=photo_gallery_description, font=('Helvetica', 12))
	photo_gallery_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

	#Displaying IMG_1.png
	image1 = Image.open("IMG_1.png")
	image1 = image1.resize((200, 200), PIL.Image.Resampling.LANCZOS)
	photo1 = ImageTk.PhotoImage(image1)
	photo1_label = tk.Label(collage_frame, image=photo1)
	photo1_label.image = photo1  # Keep a reference to avoid garbage collection
	photo1_label.grid(row=1, column=0, padx=10, pady=10)
	
	#Displaying IMG_2.png
	image2 = Image.open("IMG_2.png")
	image2 = image2.resize((200, 200), PIL.Image.Resampling.LANCZOS)
	photo2 = ImageTk.PhotoImage(image2)
	photo2_label = tk.Label(collage_frame, image=photo2)
	photo2_label.image = photo2  # Keep a reference to avoid garbage collection
	photo2_label.grid(row=1, column=1, padx=10, pady=10)

	#Button to exit new_window
	new_window_exit_button = tk.Button(collage_frame, text="Exit Photo Gallery", command = new_window.destroy)
	new_window_exit_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
	

#Create the main window with title Guessing Game
root = tk.Tk()
root.title("Marty's Music")

#GUI frame to organize GUI elements
main_window_frame = tk.Frame(root)
main_window_frame.pack(pady=10, padx=10)

#Title Label
title_label = tk.Label(main_window_frame, text="Marty's Music", font=('Helvetica', 20))
title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

#GUI Description Label with block of text
GUI_description = """Welcome to Marty's Music GUI! This GUI provides information about Marty and his music journey.
Marty began learning how to play the guitar during college. Having spent time playing the saxaphone during high-school,
learning to play this new instrument was not too difficult. Marty improved his playing skills and abilities which led to
him playing with friends. He then started a band with a few of his friends from back home in Bishop, CA. Since it was a
small town, word spread of this new band and their popularity spread throughout the town. Soon they were playing at
different events in Bishop and the surrounding areas, which led to them playing in the Bridgeport Music Festival. 

"""
title_label = tk.Label(main_window_frame, text=GUI_description, font=('Helvetica', 12))
title_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


#Button to open new window
btn = tk.Button(main_window_frame, text ="Click to see latest photo gallery", command = openPhotoGalleryWindow)
btn.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

#Button to exit root
root_exit_button = tk.Button(main_window_frame, text="Exit Marty's Music", command = root.destroy)
root_exit_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)



#Main event loop
root.mainloop()