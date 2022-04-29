
import random
numeroAleatorio = 1
numeroCliente = int(input("Introduce un número del 0 al 9: "))
oportunidades = 1

def validarNumeroUsuario(numCliente, numAleatorio):
    if numCliente in range (0,10):
        juego(numCliente,numAleatorio )
    else:
        print("error") 

def juego(numCliente, numAleatorio):
    global oportunidades
    while numCliente != numAleatorio:
      print("Error, vuelve a intentarlo")
      numCliente = int(input("Introduce un numero del 1 al 9: "))
      oportunidades = oportunidades+1
    else:
        print()
        print("****************************************************************")
        print("Correcto, lo has conseguido en ", oportunidades, " oportunidades")
        print()
      

validarNumeroUsuario(numeroCliente, numeroAleatorio)