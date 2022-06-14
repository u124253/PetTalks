import sys
import os
import tkinter
from logging import root
from pathlib import Path
from tkinter.ttk import Combobox
from tkinter import *
from tkinter.filedialog import askdirectory

path = str(Path(os.path.abspath(__file__)).parent)
sys.path.insert(0, path + "/software/transformations_interface/")
sys.path.insert(0, path + "/software/models/")

import stftMorph_function_2 as morph
import utilFunctions as UF

root = Tk()
bg = PhotoImage(file="gui_desing_7.png")

# Create Canvas
canvas1 = Canvas(root, width=720,
                 height=1045)

canvas1.pack(fill="both", expand=True)

# Display image
canvas1.create_image(0, 0, image=bg, anchor="nw")

# ------------------------------

character = "diego"
phrase = "hi"
animal = "jaguar"
balance = 0.5
save_to = "None"


# -------------------------


def get_current_value():
    balance = current_value.get() / 100
    return


def slider_changed(event):
    balance = current_value.get() / 100
    print(balance)


# slider current value
current_value = DoubleVar()

#  slider
slider = Scale(root, from_=0, to=100, orient='horizontal', command=slider_changed, variable=current_value,
               length=145)

slider.place(x=500, y=500)


def set_character(new_character):
    character = new_character
    print(character)


# set_phrase: Function that allow to set the current value of a new_phrase to the attribute phrase of the class
def set_phrase(new_phrase):
    phrase = new_phrase

    # set_animal : Function that allow to set the self.animal a given animal in string format


def set_animal(new_animal):
    animal = new_animal

#-----------------------------------------------------------------------------------------------------------------------

# clickExitButton: Exit the GUI
def clickExitButton():
    exit()

# play_sound: Function that play a sound with the current information in character and phrase
def play_sound():
    print(path + "/software/sounds/" + character + phrase + ".wav")
    if os.path.exists(path + "/software/sounds/" + character + phrase + ".wav"):
        UF.wavplay(path + "/software/sounds/" + character + phrase + ".wav")

# play_animal: Function that play a sound with the current information in animal
def play_animal_sound():
    print(path + "/software/sounds/" + animal + ".wav")
    if os.path.exists(path + "/software/sounds/" + animal + ".wav"):
        UF.wavplay(path + "/software/sounds/" + animal + ".wav")

# stop_sound: Function that stop audio by playing a .wav file with silence
def stop_sound():
    if os.path.exists(path + "/software/sounds/" + "stop.wav"):
        UF.wavplay(path + "/software/sounds/" + "stop.wav")

# set_character: Function that allow to set the current value of a new_character
def set_character( new_character):
    character = new_character

# set_phrase: Function that allow to set the current value of a new_phrase to the attribute phrase of the class
def set_phrase(new_phrase):
    phrase = new_phrase

# set_animal : Function that allow to set the self.animal a given animal in string format
def set_animal(new_animal):
    animal = new_animal

def make_Morph():
    # Delete old results
    audios = os.listdir(path + '/software/transformations_interface/temp/')
    for audio in audios:
        os.remove(path + '/software/transformations_interface/Temp/' + audio)

    audios = os.listdir(path + "/software/sounds/")

    for audio in audios:
        audio_name = audio.split('.')[0]
        name = audio_name.split('_')[0]

        if name == animal:
            inputFile1 = animal + '.wav'
            inputFile2 = character + phrase + '.wav'
            morph.main(path + "/software/sounds/" + inputFile1, path + "/software/sounds/" + inputFile2,
                       balancef=balance)

def save_to():

    import shutil

    save_to = askdirectory(title='Select your folder')  # Shows dialog box and return the path
    source_dir = path + '\\software\\transformations_interface\\temp\\moprh_result.wav'
    print(source_dir)
    print(save_to)
    shutil.copytree(source_dir, save_to)

"""
Botones
"""
character_1 = Button(root, text="DIEGO",
                     height=5, width=10, command=lambda: set_character("diego"))
character_2 = Button(root, text="RODRIGO",
                     height=5, width=10, command=lambda: set_character("rodrigo"))
character_3 = Button(root, text="AMANDA",
                     height=5, width=10, command=lambda: set_character("amanda"))
character_4 = Button(root, text="TOMAS",
                     height=5, width=10, command=lambda: set_character("tomas"))

phrase_1 = Button(root, text="phrase_1",
                  height=5, width=10, command=lambda: set_phrase("hi"))
phrase_2 = Button(root, text="phrase_2",
                  height=5, width=10, command=lambda: set_phrase("hi"))
phrase_3 = Button(root, text="phrase_3",
                  height=5, width=10, command=lambda: set_phrase("hi3"))
phrase_4 = Button(root, text="phrase_4",
                  height=5, width=10, command=lambda: set_phrase("hi4"))
phrase_5 = Button(root, text="phrase_5",
                  height=5, width=10, command=lambda: set_phrase("hi5"))
phrase_6 = Button(root, text="phrase_6",
                  height=5, width=10, command=lambda: set_phrase("hi6"))
phrase_7 = Button(root, text="phrase_7",
                  height=5, width=10, command=lambda: set_phrase("hi7"))
phrase_8 = Button(root, text="phrase_8",
                  height=5, width=10, command=lambda: set_phrase("hi8"))
#######################################################################################################################

animal_1 = Button(root, text="JAGUAR",
                  height=5, width=10, command=lambda: set_animal("jaguar"))
animal_2 = Button(root, text="BALLENA",
                  height=5, width=10, command=lambda: set_animal("ballena"))
animal_3 = Button(root, text="animal 3",
                  height=5, width=10, command=lambda: set_animal("jaguar"))
animal_4 = Button(root, text="animal 4",
                  height=5, width=10, command=lambda: set_animal("jaguar"))
animal_5 = Button(root, text="animal 5",
                  height=5, width=10, command=lambda: set_animal("jaguar"))
animal_6 = Button(root, text="animal 6",
                  height=5, width=10, command=lambda: set_animal("jaguar"))
animal_7 = Button(root, text="animal 7",
                  height=5, width=10, command=lambda: set_animal("jaguar"))
animal_8 = Button(root, text="animal 8",
                  height=5, width=10, command=lambda: set_animal("jaguar"))

playVoice = Button(root, text="PLAY VOICE", height=2, width=53, command=lambda: play_sound())
playAnimal = Button(root, text="PLAY ANIMAL", height=2, width=53, command=lambda: play_animal_sound())
stopAnimal = Button(root, text="STOP ANIMAL", height=2, width=53, command=lambda: stop_sound())

exitButton = Button(root, text="Exit", command=clickExitButton)
goButton = Button(root, text="Go!", command=lambda: make_Morph(), height=2, width=19)

saveButton = Button(root, text="Save To!", command=lambda: save_to(), height=2, width=19)
saveButton.place(x=0, y=0)




character_1.place(x=600, y=200)
character_2.place(x=700, y=200)
character_3.place(x=800, y=200)
character_4.place(x=900, y=200)

phrase_1.place(x=600, y=300)
phrase_2.place(x=700, y=300)
phrase_3.place(x=800, y=300)
phrase_4.place(x=900, y=300)

phrase_5.place(x=600, y=400)
phrase_6.place(x=700, y=400)
phrase_7.place(x=800, y=400)
phrase_8.place(x=900, y=400)

slider.place(x=440, y=503)

animal_1.place(x=50, y=300)
animal_2.place(x=150, y=300)
animal_3.place(x=250, y=300)
animal_4.place(x=350, y=300)

animal_5.place(x=50, y=400)
animal_6.place(x=150, y=400)
animal_7.place(x=250, y=400)
animal_8.place(x=350, y=400)

playVoice.place(x=600, y=500)
playAnimal.place(x=50, y=500)
stopAnimal.place(x=50, y=600)

goButton.place(x=600, y=600)
exitButton.place(x=500, y=600)


root.wm_title("PetTalks")
root.geometry("1045x720")
root.resizable(False, False)


root.mainloop()
