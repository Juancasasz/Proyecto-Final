"""Archivo principal del proyecto final"""
# Primera Versión


class Empleado():
    def __init__(self, nom, apell, edad, sal, dni, fechav):
        self.nombre = nom
        self.apellido = apell
        self.edad = edad
        self.salario = sal
        self.dni = dni
        self.fechavin = fechav

    # Uso de GET(extraer) y SET(establecer) cuando está encapsulado
    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad

    def getFecha(self):
        return self.fechavin

    def setEdad(self, edad):
        self.edad = edad

    def obtener_nombre_completo(self):
        return f"{self.nombre} {self.apellido}"


class Jefe(Empleado):
    def __init__(self, nom, apell, edad, sal, dni, fechav):
        super().__init__(nom, apell, edad, sal, dni, fechav)
        self.listaEmp = []

    def agregar_empleado(self, empleado):
        if isinstance(empleado, Empleado):
            self.listaEmp.append(empleado)

    def listarEmp(self):
        return [empleado.obtener_nombre_completo() for empleado in self.listaEmp]


class Area:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.empleados = []

    def agregar_empleado(self, empleado):
        if isinstance(empleado, Empleado):
            self.empleados.append(empleado)

    def listar_empleados(self):
        return [empleado.obtener_nombre_completo() for empleado in self.empleados]


def pruebas():

    jefe = Jefe("Carlos", "Martínez", 40, 5000, "11223344", "2020-01-01")

    area = Area("Desarrollo", "Área de desarrollo de software")

    empleado1 = Empleado("Juan", "Pérez", 30, 3000, "12345678", "2021-01-01")
    empleado2 = Empleado("Ana", "Gómez", 25, 2500, "87654321", "2021-02-01")

    jefe.agregar_empleado(empleado1)
    jefe.agregar_empleado(empleado2)

    print("Empleados a cargo del jefe:")
    for nombre_completo in jefe.listarEmp():
        print(nombre_completo)

    print("Jefe: ")
    print(f"{jefe.nombre} {jefe.apellido}")

    area.agregar_empleado(empleado2)

    print("Empleados en el área de Desarrollo:")
    for nombre_completo in area.listar_empleados():
        print(nombre_completo)


pruebas()
