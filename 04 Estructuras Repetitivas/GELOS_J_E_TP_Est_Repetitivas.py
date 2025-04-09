"""
1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
"""

for i in range (101):
    print(i)

"""
2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene.
"""

contador_digitos = 1 
numero_ingresado = int(input("Ingrese un número entero: "))
numero = numero_ingresado

if numero < 0:
    numero *=-1

while numero > 10:
    numero = numero // 10
    contador_digitos +=1

print("El numero",numero_ingresado, " tiene ",contador_digitos, " digitos")


"""
3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores.
"""

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))
suma = 0

if num1 < num2:
    for i in range(num1 + 1 , num2):
        suma += i
elif num1 > num2:
    for i in range(num2 + 1, num1):
        suma += i
else:
    print("Los numeros ingresados son iguales, no hay numeros entre ellos para sumar")

if num1 != num2:
    print("La suma de los numeros enteros entre", num1, " y ", num2, " es: ", suma)



"""
4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0.
"""

suma = 0
CORTE = "0"
contador = 0
numero = int(input("Ingrese un numero entero, o escriba "+CORTE+" para salir: "))


while numero != int(CORTE):
    suma += numero
    numero = int(input("Ingrese otro numero entero, o escriba "+CORTE+" para salir: "))
    contador +=1

if suma == 0  and contador == 0:
    print("No ha ingresado numeros a sumar")
else: 
    print("La suma de los números ingresados es: ", suma)



"""
5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
"""

from random import randint

contador = 1
numero_alea = randint(0,9)

print("\nAdivine el numero entre 0 y 9\n")
numero = int(input("Ingrese un numero: "))

while numero != numero_alea:
    numero = int(input("Ingrese un numero: "))
    contador +=1

print(f"\nFelicitacines, el numero buscado era {numero_alea}, Ud lo ha adivinado en {contador} intentos")


"""
6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente.
"""

for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i, end= " ")


"""
7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario.
"""

suma = 0

numero = int(input("Ingrese un numero entero positivo: "))

if numero <= 0:
    print(f"El numero {numero}, no es un entero positivo")
else:
    for i in range(1, numero + 1): # Arranco en 1 porque el 0 no modifica mi suma
        suma +=i
    print(f"La suma de los números comprendidos entre el 0 y el {numero}, es: {suma}")


"""
8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio).
"""

cont_pares = 0
cont_imp = 0
cont_pos = 0
cont_neg = 0
cont_cero = 0
TOPE = 5 # Modifique este valor si desea probar el programa con mas o menos números
contador = 0

print("\n***   Ingrese",TOPE,"numeros enteros   ***\n")
while contador < TOPE:
    num = int(input("Ingrese el " +str(contador + 1)+"º  numero entero: "))
    if num % 2 == 0:
        cont_pares +=1
    else:
        cont_imp +=1
    if num < 0:
        cont_neg +=1
    elif num > 0:
        cont_pos +=1
    else:
        cont_cero +=1
    contador +=1

print(f"""\nUd. ha ingresado: 
      {cont_pares} números pares;
      {cont_imp} números impares;
      {cont_pos} números positivos;
      {cont_neg} numeros negativos;
      {cont_cero} numeros cero.""") 


"""
9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor).
"""

TOPE = 5 # Modifique este valor si desea probar el programa con mas o menos números
suma = 0
contador = 0

print(f"\nIngrese {TOPE} números enteros para calcular su media\n")
while contador < TOPE:
    num = int(input(f"Ingrese el {contador + 1}º número entero: "))
    suma += num
    contador +=1

media = suma / TOPE
print(f"\nLa media de los números ingresados es: {media}")

# Este código cumple con lo visto hasta acà en la materia, pero le falta poder incorporar el manejo de errores 
# para el caso en que el usuario ingrese un valor distinto a un entero.  



"""
10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
"""

numero_inv = ""
num = input("Ingrese un número: ")
contador = 1

while contador < len(num)+1:
    numero_inv += num[contador*-1]
    contador +=1

print(f"El inverso del numero ingresado es: {numero_inv}")

# La desventaja de este codigo es que el usuario podría ingresar cadena de caracteres y no numeros 
# y el programa lo invertiría, diciendo al final que "El inverso del numero ingresado", cuando en realidad
# no se ingresó ningun numero