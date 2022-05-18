import random;
from datetime import datetime
import json

# variables globales
numeroAleatorio = random.randint(0,99);
lista = []
boteMaquina = 20;
intentos= 1;
opcionMenu=0;
salir=False;
informacion = {}
infoDia = 'partida_' + datetime.now().strftime("%y-%m-%d")
informacion[infoDia] = []


# métodos
def segundaOportunidad():
    global numeroAleatorio;
    global numeroCliente;
    global intentos;
    global boteMaquina;
    intentos = 2;
    menu()


#Empieza el juego, comparamos el numero del cliente con el número random
def jugar():
    global numeroAleatorio;
    global numeroCliente;
    global intentos;
    global boteMaquina;

    numeroCliente = int(input("Introduce un numero del 0 al 99: "))
    lista.append(numeroCliente)
    boteMaquina = boteMaquina + 1;

    while intentos < 3:
        if numeroCliente != numeroAleatorio:
            intentos = intentos + 1;
            print("Incorrecto");
            if numeroCliente < numeroAleatorio:
                print("El numero es mayor")
            else:
                print("El numero es menor")
            numeroCliente=int(input("Introduce un numero del 0 al 99:"))
            
        else:
            print("Correcto")
            print("Lo has acertado en " , intentos, "intentos")
            print("Has conseguido 5 €")
            boteMaquina = boteMaquina - 5;
            print("El bote restante es de " , boteMaquina)
            documento()
            break
    else:
        segundaOportunidad()


#Compruebo si hay bote en la máquina, si no hay más de 5 euros no se juega más
def comprobarBote():
    global salir
    if boteMaquina >= 5:
        jugar()
    else:
        print("No hay bote suficiente, avise al responsable")
        salir = True


#Aquí se crea el formato del documento y las variables que quieres que coja el documento
def documento():
    global informacion 

    informacion[infoDia].append({
        'Hora': datetime.now().strftime("%H:%M:%S"),
        'Intentos': intentos,
        'Numero Aleaotrio': numeroAleatorio,
        'Numeros Probados': lista,
        'Saldo Maquina': boteMaquina 
    }) 


#Aquí se crea el archivo, ponemos el nombre del json 
def archivo():
    
    with open("registro.json", "w") as file:
        json.dump(informacion, file)


#Es el menu donde el jugador puede elegir lo que quiere
def menu():
    global opcionMenu;
    global salir;

    while not salir:
         print("1 → Jugar")
         print("2 → Salir")
         opcionMenu = int(input("Elige una opcion: "))

         if opcionMenu == 1:
             comprobarBote()
         elif opcionMenu == 2:
             salir = True;
         else:
             print("Introduce un numero del 1 al 2 ")

menu()
documento()
archivo()
