
import sys
import os
from pathlib import Path
from tkinter import Tk,PhotoImage,Canvas,DoubleVar,Scale,Button
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename

path = str(Path(os.path.abspath(__file__)).parent)
sys.path.insert(0, path + "/software_resources/transformations_interface/")
sys.path.insert(0, path + "/software_resources/models/")

import stftMorph_function_2 as morph
import utilFunctions as UF

global character
global phrase
global animal
global balance
global save_to

root = Tk()

character = "diego"
phrase = "hi"
animal = "jaguar"
balance = 0.5
save_to = "None"

phrase_loaded="No"
animal_loaded="No"
flag_animal=0
flag_phrase=0

morph_filename= "None"

bg = PhotoImage(file="visual_resources/gui.png")

# Create Canvas
canvas1 = Canvas(root, width=720, height=1045)
canvas1.pack(fill="both", expand=True)

# Display background image
canvas1.create_image(0, 0, image=bg, anchor="nw")

def slider_changed(event):
    global balance
    balance = slider_current_value.get() / 100

# slider current value
slider_current_value = DoubleVar()

#  slider
slider = Scale(root, from_=0, to=100, orient='horizontal', command=slider_changed, variable=slider_current_value, length=145)
slider.place(x=500, y=500)

"""
Load Button
"""
load_phrase = Button(root, text="LOAD VOICE", height=2, width=24, command=lambda: load_phrase())

load_animal = Button(root, text="LOAD ANIMAL", height=2, width=24, command=lambda: load_animal())
load_animal.place(x=600,y=650)

load_phrase.place(x=800,y=650)

# load_phrase: load a phrase to perform custom morph
def load_phrase():
    global phrase_loaded,flag_phrase,phrase
    phrase_loaded= str(askopenfilename())
    flag_phrase=1

# load_phrase: load a phrase to perform custom morph
def load_animal():
    global animal_loaded,flag_animal,animal
    animal_loaded = str(askopenfilename())
    flag_animal=1



# play_sound: Function that play a sound with the current information in character and phrase
def play_interface_sound(audio_name):
    if os.path.exists(path + "/sounds_resources/"+ audio_name+".wav"):
        UF.wavplay(path + "/sounds_resources/"+ audio_name+".wav")

# play_sound: Function that play a sound with the current information in character and phrase
def play_sound():
    if os.path.exists(path + "/sounds_resources/" + character + '_' + phrase + ".wav"):
        UF.wavplay(path + "/sounds_resources/" + character +'_' + phrase + ".wav")


# play_animal: Function that play a sound with the current information in animal
def play_animal_sound():
    if os.path.exists(path + "/sounds_resources/" + animal + ".wav"):
        UF.wavplay(path + "/sounds_resources/" + animal + ".wav")


# stop_sound: Function that stop audio by playing a .wav file with silence
def stop_sound():
    if os.path.exists(path + "/sounds_resources/" + "stop.wav"):
        UF.wavplay(path + "/sounds_resources/" + "stop.wav")


# set_character: Function that allow to set the current value of a new_character
def set_character(new_character):
    global character
    character = new_character

# set_phrase: Function that allow to set the current value of a new_phrase to the attribute phrase of the class
def set_phrase(new_phrase):
    global phrase,flag_phrase
    phrase = new_phrase
    play_sound()
    flag_phrase=0

# set_animal : Function that allow to set the self.animal a given animal in string format
def set_animal(new_animal):
    global animal,flag_animal
    animal = new_animal
    play_animal_sound()
    flag_animal=0

def make_morph():
    if not os.path.exists(path + '/software_resources/transformations_interface/Temp/'):
        os.mkdir(path + '/software_resources/transformations_interface/Temp/')
    global flag_animal
    global flag_phrase
    global morph_filename
    if flag_phrase == 0 or flag_phrase == 0:
        # Delete old results
        audios = os.listdir(path + '/software_resources/transformations_interface/Temp/')
        for audio in audios:
            os.remove(path + '/software_resources/transformations_interface/Temp/' + audio)

        audios = os.listdir(path + "/sounds_resources/")

        for audio in audios:
            audio_name = audio.split('.')[0]
            name = audio_name.split('_')[0]
            if name == animal:
                inputFile1 = animal + '.wav'
                inputFile2 = character + '_'+ phrase + '.wav'
                morph.main(path + "/sounds_resources/" + inputFile1, path + "/sounds_resources/" + inputFile2,
                           balancef=balance)
            # set the final filename to:
            morph_filename=("petTalks_" + animal + '_' + character + '_'+ phrase + ".wav")

    if flag_phrase==1 and flag_phrase==1:

        name_file_1=animal_loaded.split('/')[-1].split('.')[0]
        name_file_2=phrase_loaded.split('/')[-1].split('.')[0]

        #set the final filename to:
        morph_filename="petTalks_" + name_file_1 + '_' + name_file_2 + ".wav"
        morph.main(animal_loaded, phrase_loaded, balancef=balance)

        flag_animal = 0
        flag_phrase = 0

def save_to():
    import shutil
    import os
    result_filename = morph_filename
    source = path + "\\software_resources\\transformations_interface\\temp\\" + result_filename
    destiny = askdirectory(title ='Select your folder')  # Shows dialog box and return the path
    shutil.copy2(source, destiny)  # complete target filename given

"""
Characters Buttons
"""

img_char_1 = PhotoImage(file="visual_resources/character_1.png")
character_1 = Button(root, text="DIEGO",
                     height=80, width=80,image=img_char_1, command=lambda: set_character("diego"))

img_char_2 = PhotoImage(file="visual_resources/character_2.png")
character_2 = Button(root, text="COCO",
                     height=80, width=80,image=img_char_2, command=lambda: set_character("coco"))

img_char_3 = PhotoImage(file="visual_resources/character_3.png")
character_3 = Button(root, text="TOMAS",
                     height=80, width=80,image=img_char_3, command=lambda: set_character("tomas"))

img_char_4 = PhotoImage(file="visual_resources/character_4.png")
character_4 = Button(root, text="AMANDA",
                     height=80, width=80,image=img_char_4, command=lambda: set_character("amanda"))
"""
Phrase Buttons
"""
img_phrase_1 = PhotoImage(file="visual_resources/hi_button.png")
phrase_1 = Button(root, text="Hi",
                  height=80, width=80,image=img_phrase_1,command=lambda: set_phrase("hi"))


img_phrase_2 = PhotoImage(file="visual_resources/name_button.png")
phrase_2 = Button(root, text="Name",
                  height=80, width=80,image=img_phrase_2, command=lambda: set_phrase("name"))

img_phrase_3 = PhotoImage(file="visual_resources/old_button.png")
phrase_3 = Button(root, text="Age",
                  height=80, width=80,image=img_phrase_3, command=lambda: set_phrase("age"))

img_phrase_4 = PhotoImage(file="visual_resources/hbb_button.png")
phrase_4 = Button(root, text="Birthday",
                  height=80, width=80,image=img_phrase_4,command=lambda: set_phrase("birthday"))

img_phrase_5 = PhotoImage(file="visual_resources/other_button.png")
phrase_5 = Button(root, text="Other",
                  height=80, width=80,image=img_phrase_5, command=lambda: set_phrase("other"))

img_phrase_6 = PhotoImage(file="visual_resources/xmass_button.png")
phrase_6 = Button(root, text="Christmas",
                  height=80, width=80,image=img_phrase_6, command=lambda: set_phrase("christmas"))

img_phrase_7 = PhotoImage(file="visual_resources/friend_button.png")
phrase_7 = Button(root, text="Friend",
                  height=80, width=80,image=img_phrase_7, command=lambda: set_phrase("friend"))

img_phrase_8 = PhotoImage(file="visual_resources/nice_button.png")
phrase_8 = Button(root, text="Bye",
                  height=80, width=80,image=img_phrase_8, command=lambda: set_phrase("bye"))

"""
Animals Buttons
"""

img_animal_1 = PhotoImage(file="visual_resources/lion_button.png")
animal_1 = Button(root, text="lion",
                  height=80, width=80,image=img_animal_1, command=lambda: set_animal("lion"))

img_animal_2 = PhotoImage(file="visual_resources/whale_button.png")
animal_2 = Button(root, text="whale",
                  height=80, width=80,image=img_animal_2, command=lambda: set_animal("whale"))

img_animal_3 = PhotoImage(file="visual_resources/goat_button.png")
animal_3 = Button(root, text="goat",
                  height=80, width=80,image=img_animal_3, command=lambda: set_animal("goat"))

img_animal_4 = PhotoImage(file="visual_resources/cheetah_button.png")
animal_4 = Button(root, text="cheetah",
                  height=80, width=80,image=img_animal_4, command=lambda: set_animal("cheetah"))

img_animal_5 = PhotoImage(file="visual_resources/pig_button.png")
animal_5 = Button(root, text="pig",
                  height=80, width=80,image=img_animal_5, command=lambda: set_animal("pig"))

img_animal_6 = PhotoImage(file="visual_resources/cow_button.png")
animal_6 = Button(root, text="animal 6",
                  height=80, width=80,image=img_animal_6, command=lambda: set_animal("cow"))

img_animal_7 = PhotoImage(file="visual_resources/seagul_button.png")
animal_7 = Button(root, text="seagul",
                  height=80, width=80,image=img_animal_7, command=lambda: set_animal("seagul"))

img_animal_8 = PhotoImage(file="visual_resources/cat_button.png")
animal_8 = Button(root, text="cat",
                  height=80, width=80,image=img_animal_8, command=lambda: set_animal("cat"))
"""
Other Buttons
"""
stopVoice = Button(root, text="STOP ", height=2, width=24, command=lambda: stop_sound())
stopAnimal = Button(root, text="STOP ", height=2, width=24, command=lambda: stop_sound())

goButton = Button(root, text="GO!", command=lambda: make_morph(), height=2, width=24)

saveButton = Button(root, text="SAVE TO", command=lambda: save_to(), height=2, width=24)

"""
Buttons Places
"""
character_1.place(x=600, y=100)
character_2.place(x=700, y=100)
character_3.place(x=800, y=100)
character_4.place(x=900, y=100)

phrase_1.place(x=600, y=300)
phrase_2.place(x=700, y=300)
phrase_3.place(x=800, y=300)
phrase_4.place(x=900, y=300)

phrase_5.place(x=600, y=400)
phrase_6.place(x=700, y=400)
phrase_7.place(x=800, y=400)
phrase_8.place(x=900, y=400)

slider.place(x=440, y=499)

animal_1.place(x=50, y=300)
animal_2.place(x=150, y=300)
animal_3.place(x=250, y=300)
animal_4.place(x=350, y=300)

animal_5.place(x=50, y=400)
animal_6.place(x=150, y=400)
animal_7.place(x=250, y=400)
animal_8.place(x=350, y=400)

stopVoice.place(x=800, y=500)
stopAnimal.place(x=250, y=500)

goButton.place(x=600, y=580)
saveButton.place(x=800, y=580)

root.wm_title("PetTALKS")
root.geometry("1015x720")
root.resizable(False, False)
root.iconbitmap("visual_resources/PetTalks_icon.ico")

root.mainloop()
