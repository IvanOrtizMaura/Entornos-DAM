import random
numAleatorio = random.randrange(0,11)
numUsuario = int(input("Introduce un numero del 1 al 10: "))

def juego():
    global numUsuario
    while numUsuario != numAleatorio:
        print("Incorrecto")
        numUsuario = int(input("Introduce un número del 1 al 10: "))
    else:
        print("Correcto")
        
juego()