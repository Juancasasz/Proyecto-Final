class Empleado:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad


listaEmp = []


def Mostrar():
    k = 0
    while (k < len(listaEmp)):
        print(listaEmp[k].nombre, "",
              listaEmp[k].apellido, "", listaEmp[k].edad)
        k += 1


i = 0
while (True):
    print("\n\n1. Registrar Empleado")
    print("2. Consultar listado")
    print("3. Salir")
    opcion = int(input("Ingrese una opción: "))
    if (opcion == 1):
        nom = input("Nombre: ")
        apel = input("Apellido: ")
        edad = int(input("Edad: "))
        empleado1 = Empleado(nom, apel, edad)
        listaEmp.append(empleado1)
        print("Empleado guardado exitosamente.")
    elif (opcion == 2):
        Mostrar()
    elif (opcion == 3):
        exit()
    else:
        print("Opción no válida. Intentalo de nuevo")
