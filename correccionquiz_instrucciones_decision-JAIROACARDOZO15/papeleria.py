"""Papelería"""

print("--------------------------------------")
print("--------------PAPELERÍA---------------")
print("--------------------------------------")

# input
x = int(input("digite el precio_costo del producto: "))
# processing
if x < 3000:
    y = x * 0.15
    q1 = (x + y)
    print("el precio_costo es: $ " + str(x) + " la ganancia es: $ " + str(y) + " El precio_venta es: $ "
     + str(q1))
elif x >= 3000 and x <= 6000:
    y1 = 500
    q2 = (x + y1)
    print("El precio_costo es: $ " + str(x) + " La ganancia es: $ " + str(y1) + " El precio_venta es: $ "
    + str(q2))
elif x > 6000:
    y2 = x * 0.25
    q3 = (x + y2)
    print("El precio_costo es: $ " + str(x) + " La ganancia es: $ " + str(y2) + " El precio_venta es: $ "
    + str(q3))
else: 
    print("El precio-costo: $ " + str(x) + " No tiene ningun recargo")