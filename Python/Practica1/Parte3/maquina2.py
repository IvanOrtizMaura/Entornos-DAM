import random;

# variables globales
numeroAleatorio = 5;
boteMaquina = 20;
intentos= 1;
opcionMenu=0;
salir=False;

# métodos
def segundaOportunidad():
    global numeroAleatorio;
    global numeroCliente;
    global intentos;
    global boteMaquina;
    intentos = 2;
    menu()
    # numeroCliente = int(input("Introduce un numero del 0 al 99: "))
    # boteMaquina = boteMaquina + 1;

    # while intentos < 1:
    #     if numeroCliente != numeroAleatorio:
    #         intentos = intentos + 1;
    #         print("Incorrecto");
    #         if numeroCliente < numeroAleatorio:
    #             print("El numero es mayor")
    #         else:
    #             print("El numero es menor")
    #     break
    # else:
    #      print("Correcto")
    #      print("Lo has acertado en " , intentos, "intentos")
    #      print("Has conseguido 5 €")
    #      boteMaquina = boteMaquina - 5;
    #      print("El bote restante es de " , boteMaquina)


def jugar():
    global numeroAleatorio;
    global numeroCliente;
    global intentos;
    global boteMaquina;

    numeroCliente = int(input("Introduce un numero del 0 al 99: "))
    boteMaquina = boteMaquina + 1;

    while intentos < 4:
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
            break
    else:
        segundaOportunidad()





def comprobarBote():
    if boteMaquina >= 5:
        jugar()
    else:
        print("No hay bote suficiente, avise al responsable")

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
