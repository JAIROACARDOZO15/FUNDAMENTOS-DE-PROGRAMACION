"""PROGRAMA PARA CALCULAR EL IVA Y 
 PRECIO DE VENTA DE UN PRODUCTO"""

print("-----------------------------------")
print("---- IVA Y PRECIO DE VENTA --------")
print("-----------------------------------")

# input
x = int(input("Ingrese valor inicial"))
y = float(0.19)

# processing
z = x*y
w = z+x
# output
print(str(x) + " más el " + str(y) + " es " + str(z))
print("El valor total es " + str(w))