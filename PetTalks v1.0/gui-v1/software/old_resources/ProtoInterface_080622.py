import tkinter
from tkinter import ttk
import sys
import os
from pathlib import Path

global frase

path = str(Path(os.path.abspath(__file__)).parent)
sys.path.insert(0, path + "/software/transformations_interface/")
sys.path.insert(0, path + "/software/models/")

frase = 'null'
personaje_g='null'
import stftMorph_function_2 as morph
import utilFunctions as UF

def saludar():
    messagebox.showinfo(message="¡Hola, mundo!", title="Saludo")

def generaMatriz(capaMatrizGen):
    def which_button(button_pressed):
        pages = {0:'Amanda', 1:'Diego', 2: 'Thomas', 3: 'Rodrigo'}
        selected_page = aplicacion.notebook1.select()
        #print("lolllllllllllllllllllllllllllll",selected_page)
        num = aplicacion.notebook1.index(selected_page)
#############################aqui cambiar el path para que se reproduzca el sonido que se desee y no solo el hi_fast.wav
        if os.path.exists(path + "/software/sounds/" + "diegohi.wav"):
            UF.wavplay(path + "/software/sounds/" + "diegohi.wav")
        print("iuuuuuuuu",personaje_g)

        frase = button_pressed
        print("--------------------------------------------------")
        print("button pressed ",button_pressed, frase)
        print("personaje", personaje_g)

    pad_1 = tkinter.Button(capaMatrizGen, text="greetings ", width=16, height=8,
                           command=lambda m='hi': which_button(m))
    pad_2 = tkinter.Button(capaMatrizGen, text="Merry Christmas", width=16, height=8,
                           command=lambda m="button2": which_button(m))
    pad_3 = tkinter.Button(capaMatrizGen, text="Happy Birthday", width=16, height=8,
                           command=lambda m="button3": which_button(m))
    pad_4 = tkinter.Button(capaMatrizGen, text="Good Night", width=16, height=8,
                           command=lambda m="button4": which_button(m))
    pad_5 = tkinter.Button(capaMatrizGen, text="Frase 5", width=16, height=8,
                           command=lambda m="button5": which_button(m))
    pad_6 = tkinter.Button(capaMatrizGen, text="Frase 6 ", width=16, height=8,
                           command=lambda m="button6": which_button(m))
    pad_7 = tkinter.Button(capaMatrizGen, text="Frase 7", width=16, height=8,
                           command=lambda m="button7": which_button(m))
    pad_8 = tkinter.Button(capaMatrizGen, text="Frase 8", width=16, height=8,
                           command=lambda m="button8": which_button(m))
    pad_9 = tkinter.Button(capaMatrizGen, text="Frase 9", width=16, height=8,
                           command=lambda m="button9": which_button(m))

    pad_1.grid(row=0, column=0, padx=1, pady=1)
    pad_2.grid(row=0, column=1, padx=1, pady=1)
    pad_3.grid(row=0, column=2, padx=1, pady=1)
    pad_4.grid(row=1, column=0, padx=1, pady=1)
    pad_5.grid(row=1, column=1, padx=1, pady=1)
    pad_6.grid(row=1, column=2, padx=1, pady=1)
    pad_7.grid(row=2, column=0, padx=1, pady=1)
    pad_8.grid(row=2, column=1, padx=1, pady=1)
    pad_9.grid(row=2, column=2, padx=1, pady=1)

def makeMorph(animal, balance,personaje):
    ## BORRAMOS LOS AUDIOS DE LA CARPETA OUTPUT SOUND
    audios = os.listdir(path + '/software/transformations_interface/Temp/')
    for audio in audios:
        os.remove(path + '/software/transformations_interface/Temp/' + audio)

    audios = os.listdir(path + "/software/sounds/")

    for audio in audios:
        audio_name = audio.split('.')[0]
        name = audio_name.split('_')[0]
        
        if name == animal:
            print("*****parametros morph****")
            print("-> animal",animal)
            print("-> personas",personaje)
            #print("-> boton", button)
            inputFile1 = animal.lower()+'.wav'
            inputFile2 = personaje + frase +'.wav'
            print(inputFile1, inputFile2)

            morph.main(path + "/software/sounds/" + inputFile1,path + "/software/sounds/" + inputFile2,balancef=balance)


class Aplicacion:
    def __init__(self, root):
        root.title("PetTalk")

        # x en funcion del wWeight
        wHeight = 720  #adecuado al tamaño de la foto tanto HxW
        wWeight = 1045
        root.configure(width = wWeight, height = wHeight, bg="white")
        root.resizable(False,False) #para que el usuario no pueda redimensionar la ventana ya predifinida

        # fondo
        self.imagenFondo = tkinter.PhotoImage(file="../../gui_desing_7.png")
        self.label0 = tkinter.Label(root, image=self.imagenFondo)
        #self.label0.place(relwidth=1,relheight=1)
        self.canvas1 = tkinter.Canvas(root, width=wWeight, height=wHeight)
        self.canvas1.pack(fill="both", expand=True)
        self.canvas1.create_image(0, 0, image=self.imagenFondo, anchor="nw")


        # lista desplegable para seleccionar el audio input1
        self.combo = ttk.Combobox(state="readonly", values=["vaca","obejas","lleoo","Gaviota","cerdiño","ballena","pig2", "cat", "pig1","jaguar"])
        self.combo.place(x=wWeight*0.05, y=wHeight*0.4)
        self.combo.set("jaguar") #valor por defecto


        # notebook para hacer la seleccion de distintos personages
        self.notebook1 = ttk.Notebook(root)
        ttk.Style().configure("TNotebook", background="white")
        self.notebook1.place(x=wWeight * 0.5, y=wHeight * 0.255)

        #esto se tiene que hacer para cada personaje
        self.frame1 = ttk.Frame(self.notebook1) #se genera un frame
        self.notebook1.add(self.frame1, text="Amanda") #se le agrega su respectiva pestaña dentro del notebook
        self.label1 = ttk.Label(self.frame1, text="¡Yo soy Amanda!") #texto, es opcional
        test1=generaMatriz(self.frame1) #esta es su respectiva matriz


        self.frame2 = ttk.Frame(self.notebook1)  # se genera un frame
        self.notebook1.add(self.frame2, text="Diego")  # se le agrega su respectiva pestaña dentro del notebook
        self.label2 = ttk.Label(self.frame1, text="¡Yo soy Diego!")  # texto, es opcional
        test2=generaMatriz(self.frame2)  # esta es su respectiva matriz

        self.frame3 = ttk.Frame(self.notebook1)  # se genera un frame
        self.notebook1.add(self.frame3, text="Thomas")  # se le agrega su respectiva pestaña dentro del notebook
        self.label3 = ttk.Label(self.frame3, text="¡Yo soy Thomas!")  # texto, es opcional
        generaMatriz(self.frame3)  # esta es su respectiva matriz

        self.frame4 = ttk.Frame(self.notebook1)  # se genera un frame
        self.notebook1.add(self.frame4, text="Rodrigo")  # se le agrega su respectiva pestaña dentro del notebook
        self.label4 = ttk.Label(self.frame4, text="¡Yo soy Rodrigo!")  # texto, es opcional
        generaMatriz(self.frame4)  # esta es su respectiva matriz

        # slider para cambiar el grado
        self.scl = ttk.Scale(root, from_=0, to=1, length=347, orient="horizontal", value = 0.5)
        self.scl.place(x=wWeight*0.047, y=wHeight*0.81)

        #######################################
        self.animal = "perro"
        self.personaje = "diego"
        self.balance = "0.5"
        #######################################
        self.GoButton = tkinter.Button(root, text="Go!", command=self.returnDeTodo,height=2, width=19).place(x=wWeight*0.05, y=wHeight * 0.86)

        self.SaveButton = tkinter.Button(root, text="Save", command=self.returnDeTodo, height=2, width=19).place(x=wWeight * 0.242, y=wHeight * 0.86)

        #print("aqui quiero que se vea el boton"+frase)
        #print("finalButon _ line 145",self.finalButon )


#Boton play animal
        self.play_animal = tkinter.Button(root, text="Listen Animal", command=self.returnDeTodo, height=2, width=19).place(x=wWeight*0.05, y=wHeight * 0.45)

#Botones load voice
        self.load_audio=tkinter.Button(root, text="Load", command=self.returnDeTodo, height=2, width=19).place(x=wWeight*0.725, y=wHeight * 0.86)
#############################################################################################
    def returnDeTodo(self):
        self.returnLista()
        #print("return boton_149",self.returnLista())
        self.returnNotebook()
        self.returnSlider()
        #self.morph()
        makeMorph(self.animal, self.balance,self.personaje)

    def returnLista(self):
        self.animal=self.combo.get()
        #return self.combo.get() #para recoger la respuesta a la seleccion seria

    def returnNotebook(self):
        self.personaje = self.notebook1.tab(self.notebook1.select(), "text")
        #print ("personaje:",self.notebook1.tab(self.notebook1.select(), "text"))
        #personaje=self.notebook1.tab(self.notebook1.select())
        global personaje_g
        personaje_g = self.notebook1.tab(self.notebook1.select(), "text")

    def returnSlider(self):
        self.balance = self.scl.get()
        #print("balance:",self.scl.get())

root = tkinter.Tk()
aplicacion = Aplicacion(root)
root.mainloop()