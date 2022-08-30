"""Ejercicio No. 9
Programa que al ingresar el monto de la compra se obtengan los descuentos, el recargo y el valor total """

print("------------------------------------")
print("-- valor total de un monto a pagar--")
print("------------------------------------")

x = float(input("ingrese monto de la compra: "))
y = input("Es cliente general o cliente afiliado : ")
z = input("Pago de contado  o pago a plazos : ")

if y == "cliente general " and z == "pago de contado ":
    w = x * 0.15
    t = (x - w)
    print("El monto de la compra es: $ " + str(x) + "El monto de recargo o descuento es: $ " + 
    str(w) + " El valor a pagar es: $ " + str(t))
elif y == "cliente general" and z == "pago a plazos":
    w = x * 0.1
    t = (x + w)
    print("El monto de la compra es: $ " + str(x) + "El monto de recargo o descuento es: $ " + 
    str(w) + "y el total a pagar es: $ " + str(t))
elif y == "cliente afiliado" and z == "pago de contado":
    w = x * 0.2
    t= (x - w)
    print("El monto de la compra es: $ " + str(x) + "El monto de recargo o descuento es: $ " + 
    str(w) + "y el total a pagar es: $ "+ str(t))
elif y == "cliente afliado" and z == "pago a plazos":
    w = x * 0.05
    t = (x + w)
    print("El monto de la compra es: $ " + str(x) + "El monto de recargo o descuento es: $ " + 
    str(w) + "y el total a pagar es: $" + str(t))
else:
    print("Porfavor verifique los datos ingresados; gracias")