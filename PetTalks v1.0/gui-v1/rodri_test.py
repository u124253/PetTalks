import os
import sys
import tkinter as tk
from pathlib import Path
from tkinter import ttk
path = str(Path(os.path.abspath(__file__)).parent)
sys.path.insert(0, path + "/software/transformations_interface/")
sys.path.insert(0, path + "/software/models/")
root = tk.Tk()
root.config(width=300, height=200)
root.title("Botón en Tk")
img_boton = tk.PhotoImage(file="boton.png")
boton = ttk.Button(image=img_boton)
boton.place(x=50, y=50)
root.mainloop()