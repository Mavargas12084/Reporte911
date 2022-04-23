from tkinter import *
from tkinter import ttk
import tkinter as tk
import PIL
from PIL import Image, ImageTk
import subprocess

root = Tk()
root.title("Secretaría de Educación Pública")
root.geometry("645x395")
root.configure(bg = 'white')
root.resizable(False, False) 

lblNombre = Label(root, text="Formato 911", bg='white', fg='blue',font=('Arial',18,'bold'))
lblNombre.place(x=50, y=50)
img = ImageTk.PhotoImage(Image.open("C:\\Norma 911\\files\\img1.jpg"))
lblImg = Label(root, image = img).pack()

def Captura():
    subprocess.Popen(['python',r'C:\Norma 911\scripts\CapturaUsuarios.py'])
    root.destroy()

def Reporte():
    subprocess.Popen(['python',r'C:\Norma 911\scripts\Reporte911.py'])
    root.destroy()


btnCapturar= Button(root, text="Captura de Alumnos",height = 1, width = 18, command=lambda:[Captura()])
btnCapturar.place(x=250, y= 200)

btnReporte= Button(root, text="Reporte Anual 911",height = 1, width = 18, command=lambda:[Reporte()])
btnReporte.place(x=250, y= 250)

btnCerrar= Button(root, text="Cerrar",height = 1, width = 18, command=lambda:[exit()])
btnCerrar.place(x=250, y= 300)

lblISC = Label(root, text="ISC10-D19A", bg='white', font=('Arial',9,'bold'))
lblISC.place(x=550, y=370)

root.mainloop()