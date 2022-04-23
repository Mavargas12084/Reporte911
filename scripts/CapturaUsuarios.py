from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
from tkcalendar import Calendar
from tkinter import messagebox
import csv
import subprocess
import datetime

root = Tk()
root.title("Secretaría de Educación Pública")
root.geometry("645x395")
root.configure(bg = 'white')
root.resizable(False, False)

#Funciones

def Guardar():
    if(cmbActual.get() != ''):
        File = cmbActual.get()
        FechaActual = Calendario.get_date()
        NombreAlumno = txtNombre.get()
        FechaDelta = str(cmbActual.get())
        if(File=='2022'):
            Size=(len(FechaActual))
            if Size==6:
                a = FechaDelta;a = int(a);b = FechaActual[4:7]; b=('20'+b);a=int(a);b=int(b)
                file = open(r'c:\Norma 911\files\2022.csv', 'a', newline='')
                b=(a-b)
                data = (NombreAlumno,FechaActual,b)
                writer = csv.writer(file)
                writer.writerow(data)
                file.close()
                txtNombre.delete(0, END)
                
            if Size==7:
                a = FechaDelta;a = int(a);b = FechaActual[5:8];b=('20'+b);a=int(a);b=int(b)
                file = open(r'c:\Norma 911\files\2022.csv', 'a', newline='')
                b=(a-b)
                data = (NombreAlumno,FechaActual,b)
                writer = csv.writer(file)
                writer.writerow(data)
                file.close()
                txtNombre.delete(0, END)                    
                                
        if(File=='2023'):
           Size=(len(FechaActual))
           if Size==6:
                a = FechaDelta;a = int(a);b = FechaActual[4:7]; b=('20'+b);a=int(a);b=int(b)
                file = open(r'c:\Norma 911\files\2023.csv', 'a', newline='')
                b=(a-b)
                data = (NombreAlumno,FechaActual,b)
                writer = csv.writer(file)
                writer.writerow(data)
                file.close()
                
           if Size==7:
                a = FechaDelta;a = int(a);b = FechaActual[5:8];b=('20'+b);a=int(a);b=int(b)
                file = open(r'c:\Norma 911\files\2023.csv', 'a', newline='')
                b=(a-b)
                data = (NombreAlumno,FechaActual,b)
                writer = csv.writer(file)
                writer.writerow(data)
                file.close()  
           
        if(File=='2024'):
           Size=(len(FechaActual))
           if Size==6:
                a = FechaDelta;a = int(a);b = FechaActual[4:7]; b=('20'+b);a=int(a);b=int(b)
                file = open(r'c:\Norma 911\files\2024.csv', 'a', newline='')
                b=(a-b)
                data = (NombreAlumno,FechaActual,b)
                writer = csv.writer(file)
                writer.writerow(data)
                file.close()
                
           if Size==7:
                a = FechaDelta;a = int(a);b = FechaActual[5:8];b=('20'+b);a=int(a);b=int(b)
                file = open(r'c:\Norma 911\files\2024.csv', 'a', newline='')
                b=(a-b)
                data = (NombreAlumno,FechaActual,b)
                writer = csv.writer(file)
                writer.writerow(data)
                file.close()  
            
        if(File=='2025'):
           Size=(len(FechaActual))
           if Size==6:
                a = FechaDelta;a = int(a);b = FechaActual[4:7]; b=('20'+b);a=int(a);b=int(b)
                file = open(r'c:\Norma 911\files\2025.csv', 'a', newline='')
                b=(a-b)
                data = (NombreAlumno,FechaActual,b)
                writer = csv.writer(file)
                writer.writerow(data)
                file.close()
                
           if Size==7:
                a = FechaDelta;a = int(a);b = FechaActual[5:8];b=('20'+b);a=int(a);b=int(b)
                file = open(r'c:\Norma 911\files\2025.csv', 'a', newline='')
                b=(a-b)
                data = (NombreAlumno,FechaActual,b)
                writer = csv.writer(file)
                writer.writerow(data)
                file.close()  
                
        if(File=='2026'):
           Size=(len(FechaActual))
           if Size==6:
                a = FechaDelta;a = int(a);b = FechaActual[4:7]; b=('20'+b);a=int(a);b=int(b)
                file = open(r'c:\Norma 911\files\2026.csv', 'a', newline='')
                b=(a-b)
                data = (NombreAlumno,FechaActual,b)
                writer = csv.writer(file)
                writer.writerow(data)
                file.close()
                txtNombre.delete(0, END) 
                
           if Size==7:
                a = FechaDelta;a = int(a);b = FechaActual[5:8];b=('20'+b);a=int(a);b=int(b)
                file = open(r'c:\Norma 911\files\2026.csv', 'a', newline='')
                b=(a-b)
                data = (NombreAlumno,FechaActual,b)
                writer = csv.writer(file)
                writer.writerow(data)
                file.close()              
    
    else:
        messagebox.showinfo(message="Favor de Verificar la Fecha Actual", title="ADVERTENCIA")

def Volver():
    subprocess.Popen(['python',r'C:\Norma 911\scripts\Principal.py'])
    root.destroy()

lblNombre = Label(root, text="Nombre del Alumno", bg='white', font=('Arial',10,'bold'))
lblNombre.place(x=10, y=50)

txtNombre = Entry(root, width =40)
txtNombre.place(x=150, y=50)

lblFechaNacimiento = Label(root, text="Fecha de Nacimiento", bg='white', font=('Arial',10,'bold'))
lblFechaNacimiento.place(x=10, y=100)

Calendario = Calendar(root, selectmode ='day', year = 2022, month =1, day = 1)
Calendario.place(x=150,y =100)

lblActual= Label(root, text="Año Actual", bg='white', font=('Arial',10,'bold'))
lblActual.place(x=470, y=100)


cmbActual = ttk.Combobox(root, 
                            values=[
                                    "2022", 
                                    "2023",
                                    "2024",
                                    "2025",
                                    "2026"],
                                    width=5)


cmbActual.place(x=550,y=100)


btnGuardar= Button(root, text="Guardar",height = 1, width = 10, command=lambda:[Guardar()])
btnGuardar.place(x=50, y= 320)

btnVolver= Button(root, text="Volver",height = 1, width = 10, command=lambda:[Volver()])
btnVolver.place(x=250, y= 320)

btnSalir= Button(root, text="Salir",height = 1, width = 10, command=lambda:[exit()])
btnSalir.place(x=450, y= 320)

lblISC = Label(root, text="ISC10-D19A", bg='white', font=('Arial',9,'bold'))
lblISC.place(x=550, y=370)

root.mainloop()