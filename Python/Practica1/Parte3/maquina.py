
import random
numeroAleatorio = random.randrange(0,100)
numeroCliente = int(input("Introduce un número del 0 al 99: "))
oportunidades = 1
bote = 20



def juego(numCliente, numAleatorio):
    global oportunidades
    global bote
    bote = bote + 1
    while oportunidades < 3 :
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
            print(bote)
            break
    else:
        print("Se ha terminado las ",oportunidades ,"oportunidades")
        print("El numero era ", numAleatorio) 
        print(bote)   

def validarNumeroUsuario(numCliente, numAleatorio):
    if numCliente in range (0,100):
        juego(numCliente,numAleatorio )
    else:
        print("Error!") 


    

validarNumeroUsuario(numeroCliente, numeroAleatorio)