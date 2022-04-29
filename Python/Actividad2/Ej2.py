numeroAlumnos = int(input("Introduce el numero de alumnos que van al viaje: "));
precioBus = 0 ;
precioViaje = 0;
precioTotal = 0;

def alquilerBus():
    global precioBus;
    global numeroAlumnos;
    precioBus = 4000 / numeroAlumnos;

def viaje():
    global numeroAlumnos
    global precioViaje
    if numeroAlumnos >= 100:
        precioViaje = 65;
    elif numeroAlumnos in range(50,100):
        precioViaje = 70;
    elif numeroAlumnos in range(30,50):
        precioViaje = 95;
    elif numeroAlumnos in range (0,30):
        precioViaje = 115;
    else:
        print("No hay alumnos suficientes");

def total():
    global precioTotal;
    precioTotal = precioViaje + precioBus

alquilerBus()
viaje()
total()
print(precioTotal)