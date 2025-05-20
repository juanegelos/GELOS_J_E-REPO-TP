"""
1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función 
para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número
que indique el usuario
"""

def factorial(num):
    return 1 if num == 0 else num * factorial(num-1)

print("\nCalcularemos el factorial de todos los numeros entre 1 y el numero por Ud. ingrresado")
num = int(input("Ingrese un numero entero positivo: "))

for i in range(1, num+1):
    print(f" El factorial de {i} es: {factorial(i)}")


"""
2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.
"""    

def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1 
    else: 
        return fibonacci(pos-1) + fibonacci(pos-2)

pos = int(input("\nIngrese la posición de la serie sobre la cual desea conocer su valor: "))

fibo = []
for i in range(pos+1):
    fibo.append(fibonacci(i))


print(f"\nEl valor que corresponde en la serie a la posición {pos} es: {fibonacci(pos)}")
print(f"\nLa serie completa hasta la posición indicada es: {fibo}")

"""
3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, 
utilizando la fórmula 𝑛𝑚= 𝑛∗𝑚(𝑚−1). Prueba esta función en un algoritmo general.
"""

def potencia(base, exp):
    if exp == 0:
        return 1
    else:
        return base * potencia(base, exp-1)
    
print("\nEleve cualquier numero a cualquier potencia\n")

base = float(input("Ingrese el numero a elevar: "))
exp = float(input("Ingrese el exponenete: "))

print(f"\nEl numero {base} elevado al exponente {exp}, nos da : {potencia(base,exp):.2f}")


"""
4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación 
en binario como una cadena de texto.
Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y unos (1), en base 2. 
Para convertir un número decimal a binario, se puede seguir este procedimiento:
1. Dividir el número por 2.
2. Guardar el resto (0 o 1).
3. Repetir el proceso con el cociente hasta que llegue a 0.
4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.

"""

def convertir_dec_bin(num):
    
    if num == 0:
        return ""
    else:
        if num % 2 == 0:
            binario = "0"
            return convertir_dec_bin(num//2) + binario
        else:
            binario = "1"
            return convertir_dec_bin(num//2) + binario
print("\nRepresentamos un numero en base 10 (decimal), en un numero en base 2 (binario)\n")
num=int(input("Ingrese el número que desea representar en base 2: "))
print(f"\nEl número {num} en base 10, se representa como {convertir_dec_bin(num)} en base 2")
        

"""
5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto 
sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
Requisitos:
La solución debe ser recursiva.
No se debe usar [::-1] ni la función reversed().
"""

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])
print("\nEs un políndromo?\n")
palabra = input("Ingrese una palabra o frase sin espacios ni tildes: ")
print(f"\nEs {es_palindromo(palabra)} que la palabra '{palabra}' es un palíndromo")


"""
6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y 
devuelva la suma de todos sus dígitos.
Restricciones:
No se puede convertir el número a string.
Usá operaciones matemáticas (%, //) y recursión.
Ejemplos:
suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
suma_digitos(9) → 9
suma_digitos(305) → 8 (3 + 0 + 5)

"""

def suma_digitos(num):
    
    if num % 10 == 0 and (num //10) < 1:
        return num
    else:
        suma=0
        suma += num % 10
        
    return suma + suma_digitos(num//10)
print("\nSumando los digitos de un numero entero positivo\n")
num=int(input("Ingrese un numero entero positivo: "))    
print(f"\nLa suuma de los dígitos del nmumero '{num}' es: {suma_digitos(num)}")


"""
7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, 
en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque.
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva 
el total de bloques que necesita para construir toda la pirámide.
Ejemplos:
contar_bloques(1) → 1 (1)
contar_bloques(2) → 3 (2 + 1)
contar_bloques(4) → 10 (4 + 3 + 2 + 1)
"""

def contar_bloques(num):
    if num == 1:
        return 1
    else:
        suma = 0
        suma += num
        return suma + contar_bloques(num-1)
    
print("\nCalculamos la cantidad de cubos de una pirámite, a partir de la cantidad de cubos de su base\n")
base = int(input("Ingrese la cantidad de cubos de la base de la pirámide: "))
print(f"\nPara hacer una pirámide con {base} cubos de base, Ud. necesitará {contar_bloques(base)} cubos en total")


"""
8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo
(numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.
Ejemplos:
contar_digito(12233421, 2) → 3
contar_digito(5555, 5) → 4
contar_digito(123456, 7) → 0
"""

def contar_digito(num,dig):
    if num % 10 == dig and (num // 10) < 1:
        return 1
    elif num // 10 < 1:
        return 0 
    else:
        contar = 0
        if num % 10 == dig:
             contar += 1
        
    return contar + contar_digito(num//10,dig)

print("\nBuscamos cuantas veces se repite un digito dado, en un numero entero positivo especificado\n")
num = int(input("Ingrese un numero entero positivo: "))
dig = int(input("Ingrese el digito a verificar: "))
print(f"\nEl dígito '{dig}' aparece {contar_digito(num,dig)} veces en el número {num}")
