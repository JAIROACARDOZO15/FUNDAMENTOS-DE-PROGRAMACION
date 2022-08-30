#import la libreria tkinter, con el alias tk
from pydoc import plain
import tkinter as tk
from tkinter import Tk,Frame, BOTH, Canvas, PhotoImage, messagebox

BASE=350
ALTURA=350

def graficar():
    messagebox.showinfo("Graficar plano cartesiano", "La grafica es...")
    
def pendiente():
    messagebox.showinfo("Graficar plano cartesiano", "La respectiva pendiente es.....")


ventana_principal = tk.Tk()
ventana_principal.title("GRAFICAR EN PLANO CARTESIANO")
ventana_principal.geometry("800x600")
ventana_principal.resizable(0,0)
ventana_principal.config(bg="gray")

x1=tk.IntVar()
y1=tk.IntVar()
x2=tk.IntVar()
y2=tk.IntVar()

frame_entrada = tk.Frame(ventana_principal)
frame_entrada.config(background="pale green" , width="780", height="580")
frame_entrada.place(x=10, y=10)

titulo = tk.Label(frame_entrada, text="GRAFICADORA EN PLANO CARTESIANO")
titulo.config(bg="pale green", fg="black", font=("Arial, 14"))
titulo.place(x=200, y=10)

c = Canvas(frame_entrada, width=360, height=360, bg="ivory3")
c.place(x=230 , y=50)

texto = c.create_text(BASE/2 , ALTURA-340, text="+x" , font=("Arial", "12", "bold"), fill="red",activefill="red")
texto = c.create_text(BASE/2 , ALTURA+5, text="-x" , font=("Arial", "12", "bold"), fill="red",activefill="red")
texto = c.create_text(BASE-340 , ALTURA/2, text="+y" , font=("Arial", "12", "bold"), fill="red",activefill="red")
texto = c.create_text(BASE+5 , ALTURA/2, text="-y" , font=("Arial", "12", "bold"), fill="red",activefill="red")

linea1 = c.create_line(20, ALTURA/2, BASE, ALTURA/2, fill="black", width=2)
linea2 = c.create_line(BASE/2,20,BASE/2,ALTURA, fill="black", width=2)


#etiqueta x1
label_x = tk.Label(frame_entrada , text= "X1 =")
label_x.config(bg="pale green", fg="black", font=("Arial, 12"))
label_x.place(x=50, y=420)

#caja de texto para x1
entry_x = tk.Entry(frame_entrada, textvariable=x1)
entry_x.config(font=("Arial, 12"))
entry_x.focus_set()
entry_x.place(x=90 , y=420)

#etiqueta y1
label_y = tk.Label(frame_entrada , text= "Y1 =")
label_y.config(bg="pale green", fg="black", font=("Arial, 12"))
label_y.place(x=50, y=480)

#caja de texto para y1
entry_y = tk.Entry(frame_entrada, textvariable=y1)
entry_y.config(font=("Arial, 12"))
entry_y.place(x=90 , y=480)

#etiqueta x2
label_y = tk.Label(frame_entrada , text= "X2 =")
label_y.config(bg="pale green", fg="black", font=("Arial, 12"))
label_y.place(x=500, y=420)

#caja de texto para x2
entry_y = tk.Entry(frame_entrada, textvariable=x2)
entry_y.config(font=("Arial, 12"))
entry_y.place(x=540 , y=420)

#etiqueta y2
label_y = tk.Label(frame_entrada , text= "Y2 =")
label_y.config(bg="pale green", fg="black", font=("Arial, 12"))
label_y.place(x=500, y=480)

#caja de texto para y2
entry_y = tk.Entry(frame_entrada, textvariable=y2)
entry_y.config(font=("Arial, 12"))
entry_y.place(x=540 , y=480)

#boton graficar
boton_graficar = tk.Button(frame_entrada, text="GRAFICAR", command=graficar)
boton_graficar.place(x=310, y=450)

#boton pendiente
boton_pendiente = tk.Button(frame_entrada, text="PENDIENTE", command=pendiente)
boton_pendiente.place(x=400, y=450)

# desplegar ventana principal y queda a la espera de lo que el usuario haga 
ventana_principal.mainloop()