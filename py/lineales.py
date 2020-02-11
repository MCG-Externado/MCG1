def situacion1():
    if R1==65000:
        print("¡Tu respuesta es correcta!")
    else:
        print("¡Tu respuesta es incorrecta!")
        
def situacion2():
  if D1==51000:
    print("El valor del descuento es",D1)
    P1=input("¿Cuál es el precio por pagar?:  ") #Descuento situación 2
    P1=float(P1)
    if P1==289000:
        print("El precio por pagar es", P1)
        S1=input("¿Cuánto dinero le sobra por la compra?")
        S1=float(S1)
        if S1==11000:
            print("El dinero es suficiente para comprar el disco duro y sobran",S1)
        else:
            print("La cantidad ingresada no es correcta")
        
    else:
        print("El precio por pagar es incorrecto")
        
  else:
    print("El valor del descuento es incorrecto")
