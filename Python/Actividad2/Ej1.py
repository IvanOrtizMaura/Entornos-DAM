from turtle import goto


precio = 0;
cantidad = int(input("Introduce la catidad de uva que quieres en kg: "))
tipo = (input("Introduce el tipo (A o B): "));
medida = int(input("Introduce el tamaño (1 o 2): "));

def tipoA():
    global precio 
    if medida == 1 :
        precio = (2 * cantidad) + 20 ;
    else:
        precio =  (2 * cantidad) + 30 ;

def tipoB():
    global precio
    if medida == 1:
        precio =   (2 * cantidad) -30;
    else:
        precio = (2 * cantidad) - 50;

def final():
    if tipo == "A":
        tipoA();
        
        
    else:
        tipoB();
        

final()
print(precio)