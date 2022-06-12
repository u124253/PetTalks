from tkinter import *

ws = Tk()
ws.title("PythonGuides")
ws.geometry('400x300')
ws['bg'] = '#ffbf00'


def printValue():
    pname = player_name.get()
    Label(ws, text=f'{pname}, Registered!', pady=20, bg='#ffbf00').pack()


player_name = Entry(ws)
player_name.pack(pady=30)

Button(
    ws,
    text="Register Player",
    padx=10,
    pady=5,
    command=printValue
    ).pack()

ws.mainloop()