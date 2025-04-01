"""
Práctico 3: Estructuras condicionales 

Objetivo: Comprender y aplicar las estructuras condicionales en la programación, 
desarrollando algoritmos que involucren tomas de decisiones.

Alumno: Gelos Juan Esteban
"""

# Actividades
"""
1) Escribir un programa que solicite la edad del usuario. 
Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
"""

EDAD_MIN = 18
edad = int(input("Ingrese su edad: "))

if edad > EDAD_MIN:
    print("Es mayor de edad")

"""
2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, 
deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar 
el mensaje “Desaprobado”.
"""

NOTA_MIN = 6
nota = float(input("Ingrese su nota (0-10): "))

if nota <= 10 and nota >= 0:
    if nota >= NOTA_MIN:
        print("Aprobado")
    else:
        print("Desaprobado")
else: 
    print("El valor ingresado esta fuera de rango")
# A este programa deberíamos sumarle controlar la posibilidad que el usuario ingrese un valor distinto
# a un número, ej: a, %, -, etc.


"""
3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, 
imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla 
"Por favor, ingrese un número par". 
Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.
"""

numero = int(input("Ingrese un numero par: "))

if numero % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par")
# Otra vez, a este programa deberíamos sumarle controlar la posibilidad que el usuario ingrese un valor distinto
# a un número entero, ej: 5.5 a, %, -, etc. para que no nos produzca un error


"""
4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes 
categorías pertenece: 
● Niño/a: menor de 12 años. 
● Adolescente: mayor o igual que 12 años y menor que 18 años. 
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
● Adulto/a: mayor o igual que 30 años. 
"""

print("Categoría a la que pertenece segun su edad")
print("")
edad = int(input("Ingrese su edad: "))

if edad >=0:
    if edad < 12:
        print("Ud es un Niño/a")
    elif edad >=12 and edad < 18:
        print("Ud es un Adolescente")
    elif edad >= 18 and edad < 30:
        print("Ud es un Adulto/ta joven")
    else:
        print("Ud es un Adulto/ta mayor")    
else:
    print("Su edad no puede ser negativa")
# Otra vez, a este programa deberíamos sumarle controlar la posibilidad que el usuario ingrese un valor distinto
# a un número entero, ej: 5.5 a, %, -, etc. para que no nos produzca un error

"""
5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). 
Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje 
"Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, 
ingrese una contraseña de entre 8 y 14 caracteres". 
Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene 
un iterable tal como una lista o un string.
"""

contrasena = input("Ingrese una contraseña de 8 a 14 caracteres: ")

if len(contrasena) >= 8 and len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")    
# A este programa deberíamos sumarle una función que haga que los caracteres ingresados no se muestren por pantalla
# como por ejemplo getpass() en lugar de input

# Opcion ejercicio 5
from getpass import getpass
contrasena = getpass("Ingrese una contraseña de 8 a 14 caracteres: ")

if len(contrasena) >= 8 and len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
# De todas formas, a mi no me muestra los asteriscos que pretendía en lugar de los caracteres. He revisado en internet 
# y parece que la función trabaja asi nomas. No era lo que pretedía.


"""
6) El paquete statistics de python contiene funciones que permiten tomar una lista de números y calcular la moda, 
la mediana y la media de dichos números. Un ejemplo de su uso es el siguiente: 
from statistics import mode, median, mean 
mi_lista = [1,2,5,5,3] 
mean(mi_lista) 
En la documentación oficial se puede encontrar más información sobre este paquete: https://docs.python.org/es/3.8/library/statistics.html. 
La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se pueden utilizar para predecir 
la forma de una distribución normal a partir del siguiente criterio: 
● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda. 
● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, la mediana es menor que la moda. 
● Sin sesgo: cuando la media, la mediana y la moda son iguales.
Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista numeros_aleatorios, calcule su moda, 
su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. 
Imprimir el resultado por pantalla.
Definir la lista numeros_aleatorios de la siguiente forma: 
import random 
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de forma aleatoria.
"""

from statistics import mode, median, mean
from random import randint

numeros_aleatorios = [randint(1, 100) for i in range(50)]

print(numeros_aleatorios)
media = mean(numeros_aleatorios)
print(f"Media = {media}")
mediana = median(numeros_aleatorios)
print(f"Mediana = {mediana}")
moda = mode(numeros_aleatorios)
print(f"Moda = {moda}")

if media == mediana == moda:
    print("Distribución normal, sin sesgo")
elif media > mediana and mediana > moda:
    print("distribución con sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("distribución con sesgo negativo o a la izquierda")
# Agregue algunas impresiones para ver porque en algunos casos no me daba ningun resultado la ejecución
# y pude ver que faltaban definir otros casos posibles como que la media fuera igual a la mediana pero  
# mayor o menor que la moda, que puede haber multiples modas o modas indefinidas.

# Opcion ejercicio 6
"""
Relación entre Media, Mediana y Moda / Tipo de Sesgo / Descripción	
0 Media = Mediana = Moda / Cero sesgo / (Simétrica)	
1 Moda < Mediana < Media / Sesgo Positivo / Cola derecha más larga, valores extremos altos "jalan" la media hacia arriba	
2 Media < Mediana < Moda / Sesgo Negativo / Cola izquierda más larga, valores extremos bajos "jalan" la media hacia abajo
3 Media ≈ Mediana, Múltiples Modas (simétricas) / Cero sesgo / (Simétrica) Dos o más picos simétricos	
4 Media > Mediana, Múltiples Modas / Sesgo Positivo / Sesgo general hacia la derecha con múltiples picos	
5 Media < Mediana, Múltiples Modas / Sesgo Negativo / Sesgo general hacia la izquierda con múltiples picos
6 Moda Indefinida, Media = Mediana / Cero sesgo / Distribución uniforme o sin un pico claro
7 Moda Indefinida, Media > Mediana / Sesgo Positivo / Distribución sin pico claro pero con cola derecha más larga	
8 Moda Indefinida, Media < Mediana / Sesgo Negativo / Distribución sin pico claro pero con cola izquierda más larga	
"""

from statistics import mode, median, mean
from random import randint

numeros_aleatorios = [randint(1, 100) for i in range(50)]

print(numeros_aleatorios)
media = mean(numeros_aleatorios)
print(f"Media = {media}")
mediana = median(numeros_aleatorios)
print(f"Mediana = {mediana}")
moda = mode(numeros_aleatorios)
print(f"Moda = {moda}")

if (media == mediana == moda) or (media == mediana): # casos 0 (coinciden todas), 3 (hay dos o más modas simétricamente distribuidas) y 5
    print("Distribución normal, sin sesgo")
elif (media > mediana and mediana > moda) or (media > mediana): # casos 1,  4 y 7
    print("distribución con sesgo positivo o a la derecha")
elif (media < mediana and mediana < moda) or (media < mediana) :# casos 2 ,  5 y 8
    print("distribución con sesgo negativo o a la izquierda")
# otro problema que tiene esto, es que la función mode solo da un valor modal, el primero que ocurre, no permitiendo
# establecer valores bimodales, multimodales. 


"""
7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal,
añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar 
el string tal cual lo ingresó el usuario e imprimirlo por pantalla.
"""

frase = input("Ingrese una frase o palabra: ")

if frase[-1].lower() in "aeiou":
    frase = frase + "!"
    print(frase)
else:
    print(frase)



"""
8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción 
que desee:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el
resultado por pantalla. 
Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.
"""

nombre = input("Ingrese su nombre: ")

print(f"""INGRESE UNA OPCIÓN SEGUN DESEE
        1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
        2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
        3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.""")
        

opcion = int(input("Opción elegida (1/3): "))

if opcion >0 and opcion < 4:
    if opcion == 1:
        nombre = nombre.upper()
        print(nombre)
    elif opcion == 2:
        nombre = nombre.lower()
        print(nombre)
    elif opcion == 3:
        nombre = nombre.title()
        print(nombre)
else:
    print("Opción invalida")


"""
9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de 
las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
● Menor que 3: "Muy leve" (imperceptible).
● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala)."
"""

magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud > 0:
    if magnitud < 3:
        print("Muy leve (imperceptible)")  
    elif magnitud >= 3 and magnitud < 4:
        print("Leve (ligeramente perceptible)")
    elif magnitud >= 4 and magnitud < 5:
        print( "Moderado (sentido por personas, pero generalmente no causa daños)")
    elif magnitud >= 5 and magnitud < 6:
        print("Fuerte (puede causar daños en estructuras débiles)")
    elif magnitud >= 6 and magnitud < 7:
        print("Muy Fuerte (puede causar daños significativos)")
    elif magnitud >= 7:
        print("Extremo (puede causar graves daños a gran escala)")
else:
    print("Error de carga, verifique")


"""
10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año Periodo del año
                                            Estación en el hemisferio norte   Estación en el hemisferio sur
Desde el 21 de diciembre hasta el 20 de
marzo (incluidos)                               Invierno                                Verano

Desde el 21 de marzo hasta el 20 de junio
(incluidos)                                     Primavera                               Otoño

Desde el 21 de junio hasta el 20 de
septiembre (incluidos)                          Verano                                  Invierno

Desde el 21 de septiembre hasta el 20 de
diciembre (incluidos)                           Otoño                                   Primavera

Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es.
El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, 
primavera o verano.
"""

hemisferio = input("Ingrese en que emisferio se encuentra (N/S): ").upper()

if hemisferio in "NS":
    mes = input("ingrese en que mes del año se encuentra: ").capitalize()
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Setiembre", 
             "Octubre", "Noviembre", "Diciembre"]

    if mes in meses:
        dia = int(input("Ingrese el número del día de hoy: "))

        if dia > 0 and dia <= 31:
            if (mes == "Diciembre" and dia >= 21) or mes == "Enero" or mes == "Febrero" or (mes == "Marzo" and dia <=20):
                if hemisferio == "N":
                    print("Ud. esta en INVIERNO")
                else:
                    print("Ud. esta en VERANO")
            elif (mes == "Marzo" and dia >= 21) or mes == "Abril" or mes == "Mayo" or (mes == "Junio" and dia <=20):
                if hemisferio == "N":
                    print("Ud. esta en PRIMAVERA")
                else:
                    print("Ud. esta en OTOÑO")
            elif (mes == "Junio" and dia >= 21) or mes == "Julio" or mes == "Agosto" or (mes == "Septiembre" and dia <=20):
                if hemisferio == "N":
                    print("Ud. esta en VERANO")
                else:
                    print("Ud. esta en INVIRNO")
            elif (mes == "Septiembre" and dia >= 21) or mes == "Octubre" or mes == "Noviembre" or (mes == "Diciembre" and dia <=20):
                if hemisferio == "N":
                    print("Ud. esta en OTOÑO")
                else:
                    print("Ud. esta en PRIMAVERA")
        else:
            print("Error en la carga del día")
    else:
        print("Mes mal ingresado, verifique")
else:
    print("Hemisferio mal ingresado, ingrese N para Norte o S para Sur")