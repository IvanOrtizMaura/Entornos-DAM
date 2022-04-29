num1 = int(input("Introduce un numero del 0 - 100"))
num2 = int(input("Introduce un numero del 0 - 100"))
resultado = 0 
print("A → Suma de los dos numeros")
print("B → Resta de los dos numeros")
print("C → Multiplica de los dos numeros")
print("D → Divide de los dos numeros")
opcion = input("Introduce una letra de las que sale en el menu ")

def suma ():
    resultado = num1 + num2
    print(resultado)

def resta():
    resultado = num1 - num2
    print(resultado)

def multiplicacion():
    resultado = num1 * num2
    print(resultado)

def division ():
    resultado = num1 / num2
    print(resultado)

if opcion.upper() == "A":
    suma()
elif opcion.upper() == "B":
    resta()
elif opcion.upper() == "C":
   multiplicacion()
elif opcion.upper() == "D":
    division()
else:
    print("error!")

