from tkinter import Tk, Canvas, Scale, Frame, BOTH, Button
# Molino de viento

BASE =350
ALTURA=350

def modificar_arco(angulo):
    C.itemconfig(aspa_1,start=angulo)  
    C.itemconfig(aspa_3,start=int(angulo)+120) 
    C.itemconfig(aspa_5,start=int(angulo)+240)

ventana_principal= Tk()
ventana_principal.title("Molino de viento")
ventana_principal.resizable(False, False)
ventana_principal.geometry("400x475")


frame_1= Frame(ventana_principal)
frame_1.config(bg="aquamarine",width=380,height=380)
frame_1.place(x=10,y=10)

C = Canvas(frame_1, width=360, height=360,bg="LightSkyBlue2")
C.place(x=10,y=10)

triangulo=C.create_polygon(100,300,250,300,BASE/2,150, fill="sienna4",outline="sienna4")

#arc_1= C.create_arc(95,70,255,230, start=0, extent=359, fill= "white",outline="white")
#ASPAS

aspa_1= C.create_arc(95,70,255,230, start=0, extent=60, fill= "white",outline="LightSkyBlue2")
#aspa_2= C.create_arc(95,70,255,230, start=60, extent=60, fill= "white",outline="black")
aspa_3= C.create_arc(95,70,255,230, start=120, extent=60, fill= "white",outline="LightSkyBlue2")
#aspa_4= C.create_arc(95,70,255,230, start=180, extent=60, fill= "white",outline="black")
aspa_5= C.create_arc(95,70,255,230, start=240, extent=60, fill= "white",outline="LightSkyBlue2")
#aspa_6= C.create_arc(95,70,255,230, start=300, extent=60, fill= "white",outline="black")

frame_2=Frame(ventana_principal)
frame_2.config(bg="aquamarine",width=380,height=90)
frame_2.place(x=10,y=380)
barra_deslizamiento = Scale(frame_2, label='ÁNGULO', from_=0, to=360, orient="horizontal", length=355, command=modificar_arco, tickinterval=90)
barra_deslizamiento.place(x=10,y=10)


ventana_principal.mainloop()