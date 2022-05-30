import tkinter
from tkinter import ttk


def generaMatriz(capaMatrizGen):
    def which_button(button_pressed):
        print(button_pressed)
        # return button_pressed

    pad_1 = tkinter.Button(capaMatrizGen, text="button1", width=16, height=8,
                           command=lambda m="button1": which_button(m))
    pad_2 = tkinter.Button(capaMatrizGen, text="button2", width=16, height=8,
                           command=lambda m="button2": which_button(m))
    pad_3 = tkinter.Button(capaMatrizGen, text="button3", width=16, height=8,
                           command=lambda m="button3": which_button(m))
    pad_4 = tkinter.Button(capaMatrizGen, text="button4", width=16, height=8,
                           command=lambda m="button4": which_button(m))
    pad_5 = tkinter.Button(capaMatrizGen, text="button5", width=16, height=8,
                           command=lambda m="button5": which_button(m))
    pad_6 = tkinter.Button(capaMatrizGen, text="button6", width=16, height=8,
                           command=lambda m="button6": which_button(m))
    pad_7 = tkinter.Button(capaMatrizGen, text="button7", width=16, height=8,
                           command=lambda m="button7": which_button(m))
    pad_8 = tkinter.Button(capaMatrizGen, text="button8", width=16, height=8,
                           command=lambda m="button8": which_button(m))
    pad_9 = tkinter.Button(capaMatrizGen, text="button9", width=16, height=8,
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

class Aplicacion:
    def __init__(self, root):
        root.title("PetTalk")
        

        # la ventana no es responsive aun
        # x en funcion del wWeight
        wHeight = 720  #adecuado al tamaño de la foto tanto HxW 
        wWeight = 1045
        root.configure(width = wWeight, height = wHeight, bg="black")
        root.resizable(False,False) #para que el usuario no pueda redimensionar la ventana ya predifinida

        # fondo
        self.imagenFondo = tkinter.PhotoImage(file="bg_v3.png")
        self.label0 = tkinter.Label(root, image=self.imagenFondo)
        #self.label0.place(relwidth=1,relheight=1)
        self.canvas1 = tkinter.Canvas(root, width=wWeight, height=wHeight)
        self.canvas1.pack(fill="both", expand=True)
        self.canvas1.create_image(0, 0, image=self.imagenFondo, anchor="nw")

        # logo
        '''
        self.logo = tkinter.PhotoImage(file="petalks.png")
        self.label00 = tkinter.Label(root, image=self.logo, width=234, height=83)
        self.label00.configure(bg="white")
        self.label00.pack(fill="both", expand=True)
        self.label00.place(x=10, y=10)
        '''
        # lista desplegable para seleccionar el audio input1
        self.combo = ttk.Combobox(state="readonly", values=["Dog", "Cat", "Donkey"])
        self.combo.place(x=wWeight*0.1, y=wHeight*0.4)
        self.combo.set("Dog") #valor por defecto
        #este boton se tiene que usar para poder recoger lo que seleccionas en el combobox, podriamos poner un boton
        #solo para el combo o valdria con uno al finald el
        #todo que nos haga lo mismo y sea para toda la aplicacion
        #self.comboBoton = tkinter.Button(root, text="Listo1", command=self.returnLista).place(x=wWeight*0.30, y=wHeight*0.4)
        #self.returnLista()

        # matriz de botones de audio para el diaologo que se escoge
        #self.capaMatriz = tkinter.Frame(root, bg="black")
        #self.capaMatriz.place(x=wWeight * 0.5, y=wHeight * 0.3)
        #generaMatriz(self.capaMatriz)

        # notebook para hacer la seleccion de distintos personages
        self.notebook1 = ttk.Notebook(root)
        ttk.Style().configure("TNotebook", background="black")
        self.notebook1.place(x=wWeight * 0.5, y=wHeight * 0.3)
        #esto se tiene que hacer para cada personaje
        self.frame1 = ttk.Frame(self.notebook1) #se genera un frame
        self.notebook1.add(self.frame1, text="TinkyWinky") #se le agrega su respectiva pestaña dentro del notebook
        self.label1 = ttk.Label(self.frame1, text="¡Yo soy TinkyWinky!") #texto, es opcional
        generaMatriz(self.frame1) #esta es su respectiva matriz

        self.frame2 = ttk.Frame(self.notebook1)  # se genera un frame
        self.notebook1.add(self.frame2, text="Dipsy")  # se le agrega su respectiva pestaña dentro del notebook
        self.label2 = ttk.Label(self.frame1, text="¡Yo soy Dipsy!")  # texto, es opcional
        generaMatriz(self.frame2)  # esta es su respectiva matriz

        self.frame3 = ttk.Frame(self.notebook1)  # se genera un frame
        self.notebook1.add(self.frame3, text="LaaLaa")  # se le agrega su respectiva pestaña dentro del notebook
        self.label3 = ttk.Label(self.frame3, text="¡Yo soy LaaLaa!")  # texto, es opcional
        generaMatriz(self.frame3)  # esta es su respectiva matriz

        self.frame4 = ttk.Frame(self.notebook1)  # se genera un frame
        self.notebook1.add(self.frame4, text="Po")  # se le agrega su respectiva pestaña dentro del notebook
        self.label4 = ttk.Label(self.frame4, text="¡Yo soy Po!")  # texto, es opcional
        generaMatriz(self.frame4)  # esta es su respectiva matriz

        #pasa lo mismo que con el combobox
        #self.notebookBoton = tkinter.Button(root, text="Listo2", command=self.returnNotebook).place(x=wWeight * 0.4, y=wHeight * 0.3)
        #self.notebook1.tab(self.notebook1.select(), "text")

        # slider para cambiar el grado
        self.scl = ttk.Scale(root, from_=0, to=100, length=400, orient="horizontal")
        self.scl.place(x=wWeight*0.02, y=wHeight*0.8)

        self.finalButon = tkinter.Button(root, text="Listo", command=self.returnDeTodo).place(x=wWeight * 0.4, y=wHeight * 0.9)

    def returnDeTodo(self):
        self.returnLista()
        self.returnNotebook()
        self.returnSlider()

    def returnLista(self):
        print(self.combo.get())
        #return self.combo.get() #para recoger la respuesta a la seleccion seria

    def returnNotebook(self):
        print (self.notebook1.tab(self.notebook1.select(), "text"))

    def returnSlider(self):
        print(self.scl.get())

root = tkinter.Tk()
aplicacion = Aplicacion(root)

root.mainloop()
