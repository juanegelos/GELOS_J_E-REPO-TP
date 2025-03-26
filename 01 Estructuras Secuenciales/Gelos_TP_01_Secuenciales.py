# 1.- Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola Mundo!")

"""
2.- Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo 
usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa 
debe imprimir por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas 
print(f…) para realizar la impresión por pantalla."
"""

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

"""
3.- Crear un programa que pida al usuario su nombre, apellido, edad y lugar de 
residencia e imprima por pantalla una oración con los datos ingresados. Por ejemplo: 
si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir 
“Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. Consejo: esto será más sencillo 
si utilizas print(f…) para realizar la impresión por pantalla.
"""

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


"""
4.- Crear un programa que pida al usuario el radio de un círculo e imprima 
por pantalla su área y su perímetro.
"""

from math import pi
radio = float(input("ingrese el radio del círculo: "))
area = pi * radio * radio
perimetro = 2 * pi * radio
print(f"El área del circulo es {area}")
print(f"El perímetro del circulo es {perimetro}")


"""
5.- Crear un programa que pida al usuario una cantidad de segundos e 
imprima por pantalla a cuántas horas equivale.
"""

segundos = int(input("Ingrese la cantidad de segundos a convertir en horas: "))
horas = segundos / 3600
print(f"{segundos} segundos, equivalen a {horas} horas")


"""
6.- Crear un programa que pida al usuario un número e imprima por pantalla la 
tabla de multiplicar de dicho número.
"""

numero = int(input("Ingrese un numero: "))
for i in range(1, 11):
    print(f"{i} x {numero} = {i*numero}")
    

"""
7.- Crear un programa que pida al usuario dos números enteros distintos 
del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, 
multiplicarlos y restarlos.
"""

num1 = int(input("Ingrese un numero ENTERO distinto de 0: "))
num2 = int(input("Ingrese otro numero ENTERO distinto de 0: "))

if num1 == 0 or num2 == 0:
    print("Uno o ambos numeros ingresados no son distintos de cero (0)")
else:
    print(f"{num1} + {num2} = {num1+num2}\n{num1} / {num2} = {num1/num2}"
          f"\n{num1} x {num2} = {num1*num2}\n{num1} - {num2} = {num1-num2}")


"""
8.- Crear un programa que pida al usuario su altura y su peso e imprima por 
pantalla su índice de masa corporal. Tener en cuenta que el índice de masa corporal 
se calcula del siguiente modo:
𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔(𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)2
"""

peso = float(input("Ingrese su peso en Kg.: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura ** 2)
print(f"Ud. pesa {peso} kilogramos, tiene una altura de {altura} metros"
      f" por lo que su indice de masa corporal es: {imc:.2f}")


"""
9.- Crear un programa que pida al usuario una temperatura en grados Celsius
e imprima por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la 
siguiente equivalencia:
𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 =9/5.𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32
"""

tempC = float(input("Ingrese la temperatura en grados Celsius: "))
tempF = (9/5)*tempC + 32
print(f"{tempC} grados celsius, equivalen a {tempF:.2f} grados fahrenheit")

"""
10.- Crear un programa que pida al usuario 3 números e imprima por pantalla 
el promedio de dichos números.
"""

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))

promedio = (num1+num2+num3)/3
print(f"El promedio de los numeros ingresados es {promedio:.3f}")
# Fin del Trabajo práctico
