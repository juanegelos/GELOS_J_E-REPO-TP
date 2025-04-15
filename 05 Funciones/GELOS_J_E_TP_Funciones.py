"""
A LO LARGO DEL DESARROLLO DEL TRABAJO PRACTICO, ENCONTRE QUE DEBIA HACER FUNCIONES MUY SIMILARES PARA VALIDAR 
LOS NUMEROS INGRESADOS POR LOS USUARIOS, POR LO QUE DECIDI HACER FUNCIONES QUE ME SIRVIERAN PARA DISTINTOS EJERCICIOS
Y LAS DEJE AL COMIENZO DEL ARCHIVO
AQUI LAS FUNCIONES QUE VOY A USAR REPETIDAMENTE EN DISTINTAS RESOLUCIONES
"""

def es_entero(numero): # El numero pasado como argumento, lo intenta convertir a entero. Si es posible devuelve True
    try:
        int(numero)
        return True
    except ValueError:
        return False

def validar_numero_entero(mensaje, min = float("-Inf"), max = float("Inf")):
    num = input(f"{mensaje}: ")
    entero = es_entero(num)    
    while not entero: # Si la función es_entero devolvio False, vuelve a pedir un numero hasta que devuelva True
        num = input(f"ERROR. {mensaje}: ")
        entero = es_entero(num)    
    if int(num) < min or int(num) > max: # Si el numero es menor que el minimo, vuelve a llamar a la función y reinicia el ciclo
        print("El número ingresado está fuera de rango")
        return validar_numero_entero(f"{mensaje}: ", min)
        print()
    else:        
        return int(num)
    
def es_flotante(numero): # El numero pasado como argumento, lo intenta convertir a entero. Si es posible devuelve True
    try:
        float(numero)
        return True
    except ValueError:
        return False

def validar_numero_flotante(mensaje, min = float("-Inf"), max = float("Inf")):
    num = input(f"{mensaje}: ")
    flotante = es_flotante(num)    
    while not flotante: # Si la función es_entero devolvio False, vuelve a pedir un numero hasta que devuelva True
        num = input(f"ERROR. {mensaje}: ")
        flotante = es_flotante(num)    
    if float(num) < min or float(num) > max: # Si el numero es menor que el minimo, vuelve a llamar a la función y reinicia el ciclo
        print("El número ingresado está fuera de rango")
        return validar_numero_flotante(f"{mensaje}: ", min)
        print()
    else:        
        return float(num)    



"""
1.- Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal.
"""

# Definimos la función
def imprimir_hola_mundo():
    print("Hola Mundo")

# Programa principal

imprimir_hola_mundo()


"""
2.- Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver:
“Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario.

"""

# Definimos la función
def saludar_usuraio(nombre):
    print(f"Hola {nombre}!")

# Programa principal

nombre = input("Ingrese su nombre: ") # definimos una variable "nombre" que luego usaremos como argumento para la función
saludar_usuraio(nombre)


"""
3.- Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir
los datos al usuario y llamar a esta función con los valores ingresados.
"""

# Definimos la función
def informacion_personal(nombre, apellido, edad, residencia): # Defino la función que requiere 4 argumentos
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Programa principal

nombre = input("Ingrese su nombre: ") # definimos una variable "nombre" que luego usaremos como argumento para la función
apellido = input("Ingrese su nombre: ") # definimos una variable "apellido" que luego usaremos como argumento para la función
edad = int(input("Ingrese su edad: "))# definimos una variable "edad" que luego usaremos como argumento para la función
residencia = input("Ingrese su lugar de residencia: ") # definimos una variable "residencia" que luego usaremos como argumento para la función
informacion_personal(nombre, apellido, edad, residencia) #Llamo a la función pasandole los 4 argumentos que solicita.


"""
4.- Crear dos funciones: calcular_area_circulo(radio) que reciba el radio
como parámetro y devuelva el área del círculo. calcular_perimetro_
circulo(radio) que reciba el radio como parámetro y devuelva
el perímetro del círculo. Solicitar el radio al usuario y llamar ambas
funciones para mostrar los resultados.

"""

from math import pi

# Definimos las funciones
def calcular_area_circulo(radio):
    return pi * radio * radio

def calcular_perimetro_circulo(radio):
    return 2 * pi * radio

# Programa principal

radio_valido = validar_numero_flotante("Ingrese un numero positivo que será el radio del círculo", 0.01) # Agrego una función validar, para asegurarme que el radio ingresado no sea negativo
print(f"El área del círculo es {calcular_area_circulo(radio_valido):.2f}")
print(f"El perímetro del círculo es {calcular_perimetro_circulo(radio_valido):.2f}")



"""
5.- Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mostrar
el resultado usando esta función.
"""

# Definimos las funciones

def segundos_a_horas(segundos_validos): # Recibo el argumento "segundos_validos" y lo transforma en horas.
    return segundos_validos / 3600


# Programa principal

segundos_validos = validar_numero_entero("Ingrese la cantidad de segundos", 1)
print(f"{segundos_validos} segundos, equivalen a {segundos_a_horas(segundos_validos)} horas")


"""
6.- Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro e imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función.
"""

# Definimos las funciones

def tabla_multiplicar(numero):
    print(f"\n TABLA DE MULTIPLICAR DEL NUMERO {numero}\n")
    for i in range(1, 11):
        print(f"      {numero} x {i} = {numero * i}")

# Programa principal

entero_valido = validar_numero_entero("Ingrese el numero entero mayor que 0, cuya tabla de multiplicar desea conocer", 0)
tabla_multiplicar(entero_valido)


"""
7.- Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado
de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados
de forma clara.
"""

# Definimos la función

def ingreso_numeros(): # Pide los numeros y los valida hasta que sean numeros enteros o flotantes
    try:
        num1 = float(input("Ingrese un número: "))
        num2 = float(input("Ingrese otro número: "))  
        return (num1, num2)  
    except ValueError as e:
        print(f"Los valores ingresados son erroneos: {e}")
        return ingreso_numeros()

def operaciones_basicas(valores): # Realiza las 4 operaciones básicas verificando que el numero 2 sea distinto de 0
    num1, num2 = valores
    if num2 == 0:
        return (num1 + num2, num1 - num2, num1 * num2, "No posible")
    else:
        return (num1 + num2, num1 - num2, num1 * num2, num1 / num2)
    
# Programa principal

valores = ingreso_numeros() # Llamo a la función ingreso_numeros para ingresar y validar los valores
suma, resta, mult, div = operaciones_basicas(valores) # desempaqueto los valores que me arroja la función operaciones_basicas
print(f"\nLos numeros ingresados son: {valores[0]} y {valores[1]}\n")
print(f"La suma es {suma}\nLa resta es {resta}\nLa multiplicación es {mult}\nLa división es {div}")


"""
8.- Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la función
para mostrar el resultado con dos decimales.
"""

# definimos las funciones
def calcular_imc(peso, altura):
    return peso / (altura * altura)

# Programa principal

peso = validar_numero_flotante("Ingrese su peso en Kg.",0)
altura = validar_numero_flotante("Ingrese su altura en metros", 0)
print(f"Su índice de masa corporal es: {calcular_imc(peso, altura):.2f}")


"""
9.- Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función.
"""

# Definimos la función

def celsius_a_farenheit(celsius):
    return (celsius * 9 / 5) + 32

# Programa principal

celsius = validar_numero_flotante("Ingrese la temperatura en grados Celsius")
print(f"{celsius} grados celsius, equivalen a {celsius_a_farenheit(celsius)} grados farenheit")


"""
10.- Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función.
"""

# Definimos la funcion

def calcular_promedio(mumero):
    num1, num2, num3 = numeros # desempaquetamos los numeros que vienen en una lista para operarlos
    return (num1 + num2 + num3) / 3

# Programa principal
print("PROMEDIO DE TRES NUMEROS INGRESADOS POR EL USUARIO\n")
numeros = []
for i in range(3): 
     numeros.append(validar_numero_flotante(f"Ingrese el numero {i+1}"))
print(f"\nLos números ingresados son: {numeros[0]}, {numeros[1]} y {numeros[2]}\n")
print(f"El promedio de los numeros ingresados es: {calcular_promedio(numeros)}")

# OPCION EJERCICIO 10

from statistics import mean

# Definimos la funcion
def calcular_promedio(mumero): # idem anterior pero usamos la función mean del modulo statistics
    return mean(numeros)

# Programa principal
print("PROMEDIO DE TRES NUMEROS INGRESADOS POR EL USUARIO\n")
numeros = []
for i in range(3):
     numeros.append(validar_numero_flotante(f"Ingrese el numero {i+1}"))
print(f"\nLos números ingresados son: {numeros[0]}, {numeros[1]} y {numeros[2]}\n")
print(f"El promedio de los numeros ingresados es: {calcular_promedio(numeros)}")
