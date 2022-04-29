import random
vida = int(input("Introduce el número de vidas que quieres "));
numUsuario = int(input("Introduce un numero del 1 al 10 "));
numeroAleatorio =random.randrange(0,11);
def intentos ():
    i = 0;
    while i > vida:
        nuevoNum = int(input("Introduce otro número"))
        if nuevoNum == numeroAleatorio:
            print("Número correcto")
        

def juego():
    if numUsuario == numeroAleatorio:
        print("El número es correcto")
    else:
        print(intentos());

 

def validarNumero():
    if numUsuario <= 10:
        print(juego());
    else:
        print("El número no es válido")
        
validarNumero()