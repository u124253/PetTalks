#Import the required library
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

# Create object
root = Tk()

# Define the geometry of the window
root.geometry("500x450")

# Add the image file
bg = ImageTk.PhotoImage(file="C:\\Python37\\scripts\\projects\\natural_img1.png")

# Create a canvas
canvas = Canvas(root,width= 400, height= 300)
canvas.pack(fill= "both", expand=True)

# Display image
canvas.create_image(0, 0, image=bg, anchor="nw")

# Add a text in canvas
canvas.create_text(250,250,text="Good Morning!",font=("Times New Roman", 24))

# Execute tkinter
root.mainloop()