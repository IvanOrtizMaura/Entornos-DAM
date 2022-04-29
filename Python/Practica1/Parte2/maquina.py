
import random
numeroAleatorio = random.randrange(0,100)
numeroCliente = int(input("Introduce un número del 0 al 99: "))
oportunidades = 1


def validarNumeroUsuario(numCliente, numAleatorio):
    if numCliente in range (0,100):
        juego(numCliente,numAleatorio )
    else:
        print("Error!") 

def juego(numCliente, numAleatorio):
    global oportunidades
    while oportunidades < 6 :
        if numCliente != numAleatorio:
            oportunidades = oportunidades + 1
            print("Incorrecto");
            if numCliente>numAleatorio:
                print("El numero es menor");
            else:
                print("El numero es mayor");
            numCliente = int(input("Introduce un número del 0 al 99: "))
            
        else:
            print("Correcto")
            print("Lo has hacertado en " , oportunidades, " oportunidades")
            print("El numero era", numAleatorio)
            break
    else:
        print("Se ha terminado las ",oportunidades ,"oportunidades")
        print("El numero era ", numAleatorio)    
validarNumeroUsuario(numeroCliente, numeroAleatorio)