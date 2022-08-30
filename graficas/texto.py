from tkinter import Tk,Frame, BOTH, Canvas, PhotoImage

#----------------------
# VENTANA PRINCIPAL
#----------------------
BASE = 460
ALTURA = 380

#----------------------
# VENTANA PRINCIPAL
#----------------------

ventana_principal = Tk()
ventana_principal.title("GRAFICAS 2D - TEXTO")
ventana_principal.resizable(False,False)
ventana_principal.config(bg= "green")

#----------------------
# FRAME DE GRAFICACIÓN
#----------------------
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg ="white", width=480, height=400)
frame_graficacion.pack(fill=BOTH, padx=10, pady=10)

# creacion de canvas
c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.place(x=10 , y=10)

#Texto
texto = c.create_text(BASE/2 , ALTURA/2, anchor="center", text="UIS SOCORRO" , font=("Arial", "20", "bold"), fill="blue",activefill="red")

#Lineas rectas
linea1 = c.create_line(0,0,BASE,ALTURA, fill="red")
linea2 = c.create_line(0,ALTURA,BASE,0, fill="red")
linea3 = c.create_line(BASE/2,0,BASE/2,ALTURA/2, fill="blue")
linea4 = c.create_line(BASE,ALTURA/2,BASE/2,ALTURA/2, fill="yellow")
linea5 = c.create_line(BASE/2,ALTURA,BASE/2,ALTURA/2, fill="black")
linea6 = c.create_line(0, ALTURA/2, BASE/2, ALTURA/2, fill="green")

# Cuadrados y rectangulos (outline= el color del borde del cuadrado)
"""rect1 = c.create_rectangle(10,10, BASE/2-10,ALTURA/2-10, fill="pink", outline="pink")
rect2 = c.create_rectangle(10,10,110,110, fill="green")"""

#Poligonos
#poli1 = c.create_polygon(0, ALTURA, BASE/2, 0, BASE, ALTURA, fill="green", outline= "red", width=5)

#Rombo
"""romb1 = c.create_polygon(BASE/2)"""

#elipses - circulos
"""elip1 = c.create_oval(0,0, BASE/2,ALTURA/2, fill="yellow")
elip2 = c.create_oval(BASE/2, ALTURA/2, BASE/2+100, ALTURA/2+100, fill="blue violet")"""

#Arcos
#arc1 = c.create_arc(10,10,210,210, start=45, extent=270, fill="yellow")

#Imagenes
#img = PhotoImage(file="pelota.gif")
#pelota = c.create_image(300,300, image=img,anchor="center")

# desplegar ventana principal. Queda a la espera de eventos
ventana_principal.mainloop()