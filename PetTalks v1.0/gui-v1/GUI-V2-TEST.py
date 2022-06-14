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


class Window(Frame):
    character = "diego"
    phrase = "hi"
    animal = "jaguar"
    balance = 0.5
    save_to = "None"


    def __init__(self, master=None):

        Frame.__init__(self, master)
        self.master = master
        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        # selected_animal = StringVar()
        ###########################################################################################################


        # --------------------------------------
        """
        
        self.imagenFondo = tkinter.PhotoImage(file="gui_desing_7.png")
        self.label0 = tkinter.Label(self, image=self.imagenFondo)
        self.canvas1 = tkinter.Canvas(root, width=1045, height=720)
        self.canvas1.pack(fill="both", expand=True)
        self.canvas1.create_image(0, 0, image=self.imagenFondo, anchor="nw")
        """

        # slider current value
        current_value = DoubleVar()

        def get_current_value():
            self.balance = current_value.get() / 100
            return

        def slider_changed(event):
            value_label.configure(text=get_current_value())

        """
        # label for the slider
        slider_label = Label(
            self,
            text='Balance:'
        )

        slider_label.grid(column=0,row=0,sticky='w'
        )
        """
        #  slider
        slider = Scale(self, from_=0, to=100, orient='horizontal', command=slider_changed, variable=current_value,
                       length=145)

        slider.grid(column=1, row=0, sticky='we')
        slider.place(x=440, y=503)

        # value label
        value_label = Label(self, text=get_current_value())
        value_label.grid(row=2, columnspan=4, sticky='n')

        ############################################################################################################

        # ---------Buttons---------
        character_1 = Button(self, text="DIEGO",
                             height=5, width=10, command=lambda: self.set_character("diego"))
        character_2 = Button(self, text="RODRIGO",
                             height=5, width=10, command=lambda: self.set_character("rodrigo"))
        character_3 = Button(self, text="AMANDA",
                             height=5, width=10, command=lambda: self.set_character("amanda"))
        character_4 = Button(self, text="TOMAS",
                             height=5, width=10, command=lambda: self.set_character("tomas"))

        phrase_1 = Button(self, text="phrase_1",
                          height=5, width=10, command=lambda: self.set_phrase("hi"))
        phrase_2 = Button(self, text="phrase_2",
                          height=5, width=10, command=lambda: self.set_phrase("hi"))
        phrase_3 = Button(self, text="phrase_3",
                          height=5, width=10, command=lambda: self.set_phrase("hi3"))
        phrase_4 = Button(self, text="phrase_4",
                          height=5, width=10, command=lambda: self.set_phrase("hi4"))
        phrase_5 = Button(self, text="phrase_5",
                          height=5, width=10, command=lambda: self.set_phrase("hi5"))
        phrase_6 = Button(self, text="phrase_6",
                          height=5, width=10, command=lambda: self.set_phrase("hi6"))
        phrase_7 = Button(self, text="phrase_7",
                          height=5, width=10, command=lambda: self.set_phrase("hi7"))
        phrase_8 = Button(self, text="phrase_8",
                          height=5, width=10, command=lambda: self.set_phrase("hi8"))

        animal_1 = Button(self, text="JAGUAR",
                          height=5, width=10, command=lambda: self.set_animal("jaguar"))
        animal_2 = Button(self, text="BALLENA",
                          height=5, width=10, command=lambda: self.set_animal("ballena"))
        animal_3 = Button(self, text="animal 3",
                          height=5, width=10, command=lambda: self.set_animal("jaguar"))
        animal_4 = Button(self, text="animal 4",
                          height=5, width=10, command=lambda: self.set_animal("jaguar"))

        animal_5 = Button(self, text="animal 5",
                          height=5, width=10, command=lambda: self.set_animal("jaguar"))
        animal_6 = Button(self, text="animal 6",
                          height=5, width=10, command=lambda: self.set_animal("jaguar"))
        animal_7 = Button(self, text="animal 7",
                          height=5, width=10, command=lambda: self.set_animal("jaguar"))
        animal_8 = Button(self, text="animal 8",
                          height=5, width=10, command=lambda: self.set_animal("jaguar"))

        playVoice = Button(self, text="PLAY VOICE", height=2, width=53, command=lambda: self.play_sound())
        playAnimal = Button(self, text="PLAY ANIMAL", height=2, width=53, command=lambda: self.play_animal_sound())
        stopAnimal = Button(self, text="STOP ANIMAL", height=2, width=53, command=lambda: self.stop_sound())

        exitButton = Button(self, text="Exit", command=self.clickExitButton)
        goButton = Button(self, text="Go!", command=lambda: self.make_Morph(), height=2, width=19)

        saveButton = Button(self, text="Save To!", command=lambda: self.save_to(), height=2, width=19)
        saveButton.place(x=0, y=0)
        """
        # ---------Animals_List---------
        animals_list = Combobox(root, textvariable=selected_animal)
        animals_list['values'] = ["vaca", "obejas", "lleoo", "Gaviota", "cerdiño", "ballena", "pig2", "cat",
                                  "pig1", "jaguar"]
        # prevent typing a value
        animals_list['state'] = 'readonly'
        """
        # ---------Buttons Positions---------
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
        # animals_list.place(x=700, y=700)

        # ---------Functions of the buttons---------
        """
        def change_animal(event):
            self.animal = selected_animal.get()
            print(selected_animal.get())

        #animals_list.bind('<<ComboboxSelected>>', change_animal)
        """

    def make_Morph(self):
        # Delete old results
        audios = os.listdir(path + '/software/transformations_interface/temp/')
        for audio in audios:
            os.remove(path + '/software/transformations_interface/Temp/' + audio)

        audios = os.listdir(path + "/software/sounds/")

        for audio in audios:
            audio_name = audio.split('.')[0]
            name = audio_name.split('_')[0]

            if name == self.animal:
                inputFile1 = self.animal + '.wav'
                inputFile2 = self.character + self.phrase + '.wav'
                morph.main(path + "/software/sounds/" + inputFile1, path + "/software/sounds/" + inputFile2,
                           balancef=self.balance)

    def save_to(self):

        import shutil

        self.save_to = askdirectory(title='Select your folder')  # Shows dialog box and return the path
        source_dir = path + '\\software\\transformations_interface\\temp\\moprh_result.wav'
        print(source_dir)
        print(self.save_to)
        shutil.copytree(source_dir, self.save_to)

    # clickExitButton: Exit the GUI
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

    # stop_sound: Function that stop audio by playing a .wav file with silence
    def stop_sound(self):
        if os.path.exists(path + "/software/sounds/" + "stop.wav"):
            UF.wavplay(path + "/software/sounds/" + "stop.wav")

    # set_character: Function that allow to set the current value of a new_character
    def set_character(self, new_character):
        self.character = new_character

    # set_phrase: Function that allow to set the current value of a new_phrase to the attribute phrase of the class
    def set_phrase(self, new_phrase):
        self.phrase = new_phrase

    # set_animal : Function that allow to set the self.animal a given animal in string format
    def set_animal(self, new_animal):
        self.animal = new_animal





root = Tk()
bg = PhotoImage(file="gui_desing_7.png")


app = Window(root)

root.wm_title("PetTalks")
root.geometry("1045x720")
#root.resizable(False, False)




root.mainloop()
