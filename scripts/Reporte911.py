from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import PIL

import subprocess
import pandas as pd

root = Tk()
root.title("Secretaría de Educación Pública")
root.geometry("645x395")
root.configure(bg = 'white')
root.resizable(False, False) 

def Consultar():
    File = int(cmbActual.get())
    Edad6=0;Edad7=0;Edad8=0;Edad9=0;Edad10=0;Edad11=0
    
    try:
        if File == 2022:
            DataFrame = pd.read_csv(r'c:\Norma 911\files\2022.csv',header=None,usecols=[2])
            for i in range (len(DataFrame)):
                if DataFrame.iloc[i][2] == 6:
                    Edad6=Edad6+1
                if DataFrame.iloc[i][2] == 7:
                    Edad7=Edad7+1
                if DataFrame.iloc[i][2] == 8:
                    Edad8=Edad8+1
                if DataFrame.iloc[i][2] == 9:
                    Edad9=Edad9+1
                if DataFrame.iloc[i][2] == 10:
                    Edad10=Edad10+1
                if DataFrame.iloc[i][2] == 11:
                    Edad11=Edad11+1 
            
            txtResultado.insert(INSERT,'Niños con 6 años de edad cumplidos: ') 
            txtResultado.insert(END,Edad6)
            
            txtResultado.insert(INSERT,'\nNiños con 7 años de edad cumplidos: ') 
            txtResultado.insert(END,Edad7)
            
            txtResultado.insert(INSERT,'\nNiños con 8 años de edad cumplidos: ') 
            txtResultado.insert(END,Edad8)
            
            txtResultado.insert(INSERT,'\nNiños con 9 años de edad cumplidos: ') 
            txtResultado.insert(END,Edad9)
            
            txtResultado.insert(INSERT,'\nNiños con 10 años de edad cumplidos: ') 
            txtResultado.insert(END,Edad10)
            
            txtResultado.insert(INSERT,'\nNiños con 11 años de edad cumplidos: ') 
            txtResultado.insert(END,Edad11)

        if File == 2023:
            DataFrame = pd.read_csv(r'c:\Norma 911\files\2023.csv',header=None,usecols=[2])
            for i in range (len(DataFrame)):
                if DataFrame.iloc[i][2] == 6:
                    Edad6=Edad6+1
                if DataFrame.iloc[i][2] == 7:
                    Edad7=Edad7+1
                if DataFrame.iloc[i][2] == 8:
                    Edad8=Edad8+1
                if DataFrame.iloc[i][2] == 9:
                    Edad9=Edad9+1
                if DataFrame.iloc[i][2] == 10:
                    Edad10=Edad10+1
                if DataFrame.iloc[i][2] == 11:
                    Edad11=Edad11+1
              
            txtResultado.insert(INSERT,'Niños con 6 años de edad cumplidos: ') 
            txtResultado.insert(END,Edad6)
            
            txtResultado.insert(INSERT,'\nNiños con 7 años de edad cumplidos: ') 
            txtResultado.insert(END,Edad7)
            
            txtResultado.insert(INSERT,'\nNiños con 8 años de edad cumplidos: ') 
            txtResultado.insert(END,Edad8)
            
            txtResultado.insert(INSERT,'\nNiños con 9 años de edad cumplidos: ') 
            txtResultado.insert(END,Edad9)
            
            txtResultado.insert(INSERT,'\nNiños con 10 años de edad cumplidos: ') 
            txtResultado.insert(END,Edad10)
            
            txtResultado.insert(INSERT,'\nNiños con 11 años de edad cumplidos: ') 
            txtResultado.insert(END,Edad11)
                 
        if File == 2024:
            DataFrame = pd.read_csv(r'c:\Norma 911\files\2024.csv',header=None,usecols=[2])
            for i in range (len(DataFrame)):
                if DataFrame.iloc[i][2] == 6:
                    Edad6=Edad6+1
                if DataFrame.iloc[i][2] == 7:
                    Edad7=Edad7+1
                if DataFrame.iloc[i][2] == 8:
                    Edad8=Edad8+1
                if DataFrame.iloc[i][2] == 9:
                    Edad9=Edad9+1
                if DataFrame.iloc[i][2] == 10:
                    Edad10=Edad10+1
                if DataFrame.iloc[i][2] == 11:
                    Edad11=Edad11+1     
                 
            txtResultado.insert(INSERT,'Niños con 6 años de edad cumplidos: ') 
            txtResultado.insert(END,Edad6)
            
            txtResultado.insert(INSERT,'\nNiños con 7 años de edad cumplidos: ') 
            txtResultado.insert(END,Edad7)
            
            txtResultado.insert(INSERT,'\nNiños con 8 años de edad cumplidos: ') 
            txtResultado.insert(END,Edad8)
            
            txtResultado.insert(INSERT,'\nNiños con 9 años de edad cumplidos: ') 
            txtResultado.insert(END,Edad9)
            
            txtResultado.insert(INSERT,'\nNiños con 10 años de edad cumplidos: ') 
            txtResultado.insert(END,Edad10)
            
            txtResultado.insert(INSERT,'\nNiños con 11 años de edad cumplidos: ') 
            txtResultado.insert(END,Edad11)
         
                 
        if File == 2025:
            DataFrame = pd.read_csv(r'c:\Norma 911\files\2025.csv',header=None,usecols=[2])
            for i in range (len(DataFrame)):
                if DataFrame.iloc[i][2] == 6:
                    Edad6=Edad6+1
                if DataFrame.iloc[i][2] == 7:
                    Edad7=Edad7+1
                if DataFrame.iloc[i][2] == 8:
                    Edad8=Edad8+1
                if DataFrame.iloc[i][2] == 9:
                    Edad9=Edad9+1
                if DataFrame.iloc[i][2] == 10:
                    Edad10=Edad10+1
                if DataFrame.iloc[i][2] == 11:
                    Edad11=Edad11+1

            txtResultado.insert(INSERT,'Niños con 6 años de edad cumplidos: ') 
            txtResultado.insert(END,Edad6)
            
            txtResultado.insert(INSERT,'\nNiños con 7 años de edad cumplidos: ') 
            txtResultado.insert(END,Edad7)
            
            txtResultado.insert(INSERT,'\nNiños con 8 años de edad cumplidos: ') 
            txtResultado.insert(END,Edad8)
            
            txtResultado.insert(INSERT,'\nNiños con 9 años de edad cumplidos: ') 
            txtResultado.insert(END,Edad9)
            
            txtResultado.insert(INSERT,'\nNiños con 10 años de edad cumplidos: ') 
            txtResultado.insert(END,Edad10)
            
            txtResultado.insert(INSERT,'\nNiños con 11 años de edad cumplidos: ') 
            txtResultado.insert(END,Edad11)
                    
        if File == 2026:
            DataFrame = pd.read_csv(r'c:\Norma 911\files\2026.csv',header=None,usecols=[2])
            for i in range (len(DataFrame)):
                if DataFrame.iloc[i][2] == 6:
                    Edad6=Edad6+1
                if DataFrame.iloc[i][2] == 7:
                    Edad7=Edad7+1
                if DataFrame.iloc[i][2] == 8:
                    Edad8=Edad8+1
                if DataFrame.iloc[i][2] == 9:
                    Edad9=Edad9+1
                if DataFrame.iloc[i][2] == 10:
                    Edad10=Edad10+1
                if DataFrame.iloc[i][2] == 11:
                    Edad11=Edad11+1

            txtResultado.insert(INSERT,'Niños con 6 años de edad cumplidos: ') 
            txtResultado.insert(END,Edad6)
            
            txtResultado.insert(INSERT,'\nNiños con 7 años de edad cumplidos: ') 
            txtResultado.insert(END,Edad7)
            
            txtResultado.insert(INSERT,'\nNiños con 8 años de edad cumplidos: ') 
            txtResultado.insert(END,Edad8)
            
            txtResultado.insert(INSERT,'\nNiños con 9 años de edad cumplidos: ') 
            txtResultado.insert(END,Edad9)
            
            txtResultado.insert(INSERT,'\nNiños con 10 años de edad cumplidos: ') 
            txtResultado.insert(END,Edad10)
            
            txtResultado.insert(INSERT,'\nNiños con 11 años de edad cumplidos: ') 
            txtResultado.insert(END,Edad11)
            
             
        
    except:
        messagebox.showerror("Error", "No se pudo generar la consulta")

    
def Volver():
    subprocess.Popen(['python',r'C:\Norma 911\scripts\Principal.py'])
    root.destroy()


lblFechaNacimiento = Label(root, text="Seleccione el año para realizar la consulta y presione Consultar", bg='white', font=('Arial',10,'bold'))
lblFechaNacimiento.place(x=10, y=50)

cmbActual = ttk.Combobox(root, 
                            values=[
                                    "2022", 
                                    "2023",
                                    "2024",
                                    "2025",
                                    "2026"],
                                    width=7)


cmbActual.place(x=450,y=50)

txtResultado = Text(root)
txtResultado.place(x=50, y=140, width=500, height=100)

btnGuardar= Button(root, text="Consultar",height = 1, width = 10, command=lambda:[Consultar()])
btnGuardar.place(x=50, y= 320)

btnVolver= Button(root, text="Volver",height = 1, width = 10, command=lambda:[Volver()])
btnVolver.place(x=250, y= 320)

btnSalir= Button(root, text="Salir",height = 1, width = 10, command=lambda:[exit()])
btnSalir.place(x=450, y= 320)

lblISC = Label(root, text="ISC10-D19A", bg='white', font=('Arial',9,'bold'))
lblISC.place(x=550, y=370)



root.mainloop()