"""
1) Dado el diccionario precios_frutas precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 
Añadir las siguientes frutas con sus respectivos precios: 
● Naranja = 1200 
● Manzana = 1500 
● Pera = 2300
"""

# Diccionario Precios

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Añadimos nuevos precios

precios_frutas["Naranja"] = 1200 
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print(precios_frutas)
print(precios_frutas.keys())
print(precios_frutas.values())


"""
2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado
en el punto anterior, actualizar los precios de las siguientes frutas: 
● Banana = 1330 
● Manzana = 1700 
● Melón = 2800
"""

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print(precios_frutas)

"""
3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado 
en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.
"""

frutas = list(precios_frutas.keys())
print(frutas)
print(type(frutas)) # Para verificar que tipo de objeto es frutas


"""
4) Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe.
"""

productos={}
ingresa=True
while ingresa:
    print("**** MENU DE OPCIONES ****")
    print("1.- Registrar número")
    print("2. Consultar número\n")
    opcion=int(input("Elija la opción deseada: "))

    if opcion==1 or opcion==2:
        match opcion:
            case 1: 
                nombre=input("\nIngrese el nombre: ")
                numero=int(input("\nIngrese el numero telefónico: "))
                if nombre in productos:
                    print(f"\nEl nombre {nombre} ya está productosdo")
                    print(f"\nEl numero productosdo para {nombre} es: {productos[nombre]}")
                else:
                    productos[nombre]=numero
            case 2:
                nombre=input("\nIngrese el nombre: ")
                if nombre in productos:
                    print(f"\nEl numero productosdo para {nombre} es: {productos[nombre]}")
                else:
                    print(f"\n{nombre} no está productosdo")
    else:
        print("\nOpción inválida")
    
    continuar=input("\nDesea realizar otra operación (si/no): ")
    if continuar.lower() == "no":
        ingresa = False
    


"""
5) Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra.
"""

frase = input("Ingrese una frase tan larga como desee: ")
lista_palabras=frase.split()
conjunto_palabras=set(lista_palabras)

conteo_palabras={}
for item in lista_palabras:
    if item not in conteo_palabras:
        conteo_palabras[item]=0
    conteo_palabras[item]+=1    

print(f"Las palabras no repetidas de su frase son: {conjunto_palabras}")
print(f"Las palabras que se repiten son: {conteo_palabras}")

"""
6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno.
"""

from  statistics import mean

lista_alumnos={}

for i in range(2):
    lista_notas=[]
    nombre = input("\nIngrese el nombre del alumno: ")
    for j in range(3):
        nota = float(input(f"Ingrese la nota Nª {j} del alumno: "))
        lista_notas.append(nota)
    t_notas=tuple(lista_notas)    
    
    if nombre not in lista_alumnos:
        lista_alumnos[nombre]=t_notas
    else:
        print(f"{nombre} ya está cargado")
print(lista_alumnos)

for i, j in lista_alumnos.items():
    list_notas = [int(x) for x in j]
    promedio = mean(list_notas)
    print(f"Alumno {i}, promedio: {promedio} ")


"""
7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
"""

aprob_parc_1={5450, 5320, 5489, 5229, 5478, 5523, 5987, 5865, 8475, 5632, 5942, 5824, 5102}
aprob_parc_2={5489, 5523, 5865, 5632, 5742, 5698, 5204, 5463, 5792, 5812, 5656, 5544, 5219}

aprobaron_ambos = aprob_parc_1.intersection(aprob_parc_2)
print(f"Estos alumnos aprobaron ambos parciales: {aprobaron_ambos}")

aprob_solo_1= aprob_parc_1.symmetric_difference(aprob_parc_2)
print(f"Alumnos que aprobaron solo 1 parcial: {aprob_solo_1}")

aprob_1_o_mas= aprob_parc_1.union(aprob_parc_2)
print(f"Alumnos que aprobaron al menos 1 parcial: {aprob_1_o_mas}")

"""
8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe.
"""


productos={"Camisas": 50, "Pantalones": 150, "Camperas": 25, "Cintos": 30, "Chalecos": 60}
ingresa=True
while ingresa:
    print("**** MENU DE OPCIONES ****")
    print("1.- Consultar stock de un producto")
    print("2. Agregar unidades al stock")
    print("3. Agregar productos al listado de stock\n")
    opcion=int(input("Elija la opción deseada: "))

    if opcion in [1, 2, 3]:
        match opcion:
            case 1: 
                nombre=input("\nIngrese el producto que desea consultar: ")
                if nombre in productos:
                    print(f"\nEl stock del producto {nombre} es {productos[nombre]}")
                else:
                    print(f"\nEl producto {nombre} no existe")
            case 2:
                nombre=input("\nIngrese el nombre: ")
                cantidad=int(input("Ingrese la cantidad de producto: "))
                if nombre in productos:
                    productos[nombre]+=cantidad
                else:
                    print("El producto no existe, agreguelo por la opcion 3")
            case 3:
                nombre=input("\nIngrese el nombre: ")
                cantidad=int(input("Ingrese la cantidad de producto: "))
                if nombre in productos:
                    productos[nombre]+=cantidad
                else:
                    productos[nombre]=cantidad

    else:
        print("\nOpción inválida")
    
    continuar=input("\nDesea realizar otra operación (si/no): ")
    if continuar.lower() == "no":
        ingresa = False


"""
9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. Ejemplo:
Permití consultar qué actividad hay en cierto día y hora.
"""

agenda={("Lunes", "10:00"):"Dentista", ("Lunes", "18:30"): "Reunion de padres", ("Martes", "20:30"): "Asado en Pablo",
        ("Miercoles", "21:30"): "Juntada Oficina", ("Jueves", "9:00"): "Turno en registro", ("Viernes", "10:30"): "Turno en Arca"}

dia = input("Ingrese el día que desaa consultar: ")
hora = input("ingrese la hora del evento que desea consultar: ")
control=0

for llave in agenda:
    if dia in llave and hora in llave:
        print(f"El día {dia} a la hora {hora}, Ud. tiene: {agenda[llave]}")
        control+=1

if control < 1:
        print(f"El día {dia} a la hora {hora}, Ud. no tiene nada agendado")
        
# Otra opción, que liste todos los eventos del dia seleccionado

for llave in agenda:
    if dia in llave:
        print(f"El día {dia}, Ud. tiene: {agenda[llave]} a la hora {llave[1]}")
        control+=1

if control < 1:
        print(f"El día {dia}, Ud. no tiene nada agendado")


"""
10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
• Las capitales sean las claves.
• Los países sean los valores.
"""

pais_capital= {"Argentina": "Buenos Aires", "Brasil": "Brasilia", "Chile": "Santiago", "Colombia": "Bogotá",
    "España": "Madrid", "Francia": "París", "Italia": "Roma", "México": "Ciudad de México", "Perú": "Lima",
    "Alemania": "Berlín"}

capitales_pais={}
for pais, capital in pais_capital.items():
    capitales_pais[capital]=pais

print(pais_capital)
print(capitales_pais)


# EJERCICIOS HECHOS DEL PRACTICO ANTERIOR A LA ELIMINACION TEMPORAL


"""
4) Crear una clase llamada Persona que contenga un método __init__ con los atributos nombre, pais y edad 
y el método saludar. El método saludar debe imprimir por pantalla un mensaje de salud que siga la estructura 
"¡Hola! Soy [nombre], vivo en [pais] y tengo [edad] años."
"""

class Persona:

    def __init__(self, nombre, pais, edad):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad

    def saludar(self):
        print(f"Hola! soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años")

juan = Persona("Juan", "Argentina", 52)
juan.saludar()


"""
5) Crear una clase llamada Circulo que contenga el atributo radio y los métodos calcular_area 
y calcular_perimetro. Dichos métodos deben calcular el parámetro correspondiente.
"""

from math import pi

class Circulo:

    def __init__(self, radio):
        self.radio = radio

    def perímetro_circulo(self):
        return 2 * pi * self.radio
    
    def area_circulo(self):
        return pi * self.radio **2
    

circulo1 = Circulo(1)
print(f"El perimetro del círculo es {circulo1.perímetro_circulo():.2f}")
print(f"El área del círculo es {circulo1.area_circulo():.2f}")

"""
6) Dado un string con paréntesis "()", "{}", "[]", verifica si están correctamente balanceados usando una pila.
Ejemplo de entrada y salida:
"""


"""
7) Usa una cola para simular un sistema de turnos en un banco. La cola debe permitir: 
● Agregar clientes (encolar). 
● Atender clientes (desencolar). 
● Mostrar el siguiente cliente en la fila.
"""

from collections import deque

class Cola:

    def __init__(self):
        self.turnero = deque()  

    def encolar(self, nombre):
        self.turnero.append(nombre)

    def sin_clientes(self):
        return len(self.turnero) == 0

    def desencolar(self):
        self.turnero.popleft() if not self.sin_clientes() else "No hay clientes en espera"

    def mostrar_proximo(self):
        return self.turnero[0] if not self.sin_clientes() else "No hay clientes en espera"
    
    def listar(self):
        return list(self.turnero)

turnero1 = Cola()
turnero1.encolar("Garay, Cacho")
turnero1.encolar("Alvarez, Negro")
print(f"Clientes en espera: {turnero1.listar()}")
print(f"Proximo: {turnero1.mostrar_proximo()}")
turnero1.desencolar()
turnero1.encolar("Viale, Chichilo")
print(f"Clientes en espera: {turnero1.listar()}")
print(f"Proximo: {turnero1.mostrar_proximo()}")
turnero1.desencolar()
print(f"Proximo: {turnero1.mostrar_proximo()}")
turnero1.desencolar()
print(f"Proximo: {turnero1.mostrar_proximo()}")


"""
8) Crea una lista enlazada que permita insertar nodos al inicio y recorrer la lista para mostrar los valores almacenados.
"""

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None 

    def agregar(self, valor):
        nuevo_valor = Nodo(valor)
        nuevo_valor.siguiente = self.cabeza
        self.cabeza = nuevo_valor

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end= " --> ")
            actual = actual.siguiente
        print("Nome")

    def insertar_despues_de(self, valor_previo, nuevo_valor): # Noo funciona,. Revisar, falta determinar valor previo
        if not valor_previo:
            print("El valor previo no existe.")
            return
        nuevo_nodo = Nodo(nuevo_valor)
        nuevo_nodo.siguiente = valor_previo.siguiente
        valor_previo.siguiente = nuevo_nodo


lista_canciones = ListaEnlazada()
lista_canciones.agregar("Canción A")
lista_canciones.agregar("Canción B")
lista_canciones.agregar("Canción C")
lista_canciones.mostrar()
lista_canciones.insertar_despues_de("Canción B", "Canción H")
lista_canciones.mostrar()