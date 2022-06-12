import sys
import os
from tkinter import *
import tkinter
from logging import root
from pathlib import Path
from tkinter.ttk import Combobox
from tkinter import *
from IPython.terminal.pt_inputhooks import tk
from PIL import Image, ImageTk

path = str(Path(os.path.abspath(__file__)).parent)
sys.path.insert(0, path + "/software/transformations_interface/")
sys.path.insert(0, path + "/software/models/")

import stftMorph_function_2 as morph
import utilFunctions as UF

class Window(Frame):
    character = "None"
    phrase = "None"
    animal = "None"

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        selected_animal = StringVar()

        # ---------Buttons---------
        character_1 = Button(self, text="DIEGO", command=lambda: self.set_character("diego"))


        exitButton = Button(self, text="Exit", command=self.clickExitButton)
        phraseButton = Button(self, text="2", command=lambda: self.set_phrase("hi"))
        playButton = Button(self, text="3", command=lambda: self.play_sound())
        playAnimal = Button(self, text="listen animal", command=lambda: self.play_animal_sound())
        #goButton = Button(self, text="Go!", command=self.go_and_moprh(), height=2, width=19)



        # ---------Animals_List---------
        animals_list = Combobox(root, textvariable=selected_animal)
        animals_list['values'] = ["vaca", "obejas", "lleoo", "Gaviota", "cerdiño", "ballena", "pig2", "cat",
                                  "pig1", "jaguar"]
        # prevent typing a value
        animals_list['state'] = 'readonly'

        # ---------Buttons Positions---------

        wHeight = 720
        wWeight = 1045

        exitButton.place(x=0, y=0)
        character_1.place(x=50, y=50)
        phraseButton.place(x=70, y=70)
        playButton.place(x=80, y=80)
        #goButton.place(x=wWeight * 0.05, y=wHeight * 0.86)



        playAnimal.place(x=52, y=324)
        animals_list.place(x=52, y=288)
        # ---------Functions of the buttons---------
        def change_animal(event):
            self.animal = selected_animal.get()
            print(selected_animal.get())

        animals_list.bind('<<ComboboxSelected>>', change_animal)

    # clickExitButton: function that allow to exit the app
    """
    def go_and_moprh(self):
        makeMorph(self.animal,0.5, self.personaje+sel)
    """
    def clickExitButton(self):
        exit()

    # play_sound: Function that play a sound with the current information in character and phrase
    def play_sound(self):
        print(path + "/software/sounds/" + self.character + self.phrase + ".wav")
        if os.path.exists(path + "/software/sounds/" + self.character + self.phrase + ".wav"):
            UF.wavplay(path + "/software/sounds/" + self.character + self.phrase + ".wav")

    # play_animal: Function that play a sound with the current information in animal
    def play_animal_sound(self):
        print(path + "/software/sounds/" + self.animal + ".wav")
        if os.path.exists(path + "/software/sounds/" + self.animal + ".wav"):
            UF.wavplay(path + "/software/sounds/" + self.animal + ".wav")

    # set_character: Function that allow to set the current value of a new_character
    def set_character(self, new_character):
        self.character = new_character

    # set_phrase: Function that allow to set the current value of a new_phrase to the attribute phrase of the class
    def set_phrase(self, new_phrase):
        self.phrase = new_phrase


root = Tk()
app = Window(root)

wHeight = 720
wWeight = 1045

root.wm_title("PetTalks")
root.geometry("1045x720")
root.resizable(False, False)
root.mainloop()
