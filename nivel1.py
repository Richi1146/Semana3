# Ejercicios

# A continuación se presentan 20 ejercicios que van desde un nivel básico hasta avanzado. Todos deben resolverse utilizando funciones.
# 🟢 Nivel Básico

#     Saludo personalizado
#     Crea una función que reciba un nombre y muestre un saludo personalizado.

#     Suma de dos números
#     Escribe una función que reciba dos números y devuelva su suma.

#     Número par o impar
#     Crea una función que determine si un número es par o impar.

#     Mayoría de edad
#     Escribe una función que reciba una edad y devuelva si es mayor o menor de edad.

#     Conversor de temperatura
#     Crea una función que convierta grados Celsius a Fahrenheit.

#     Área de un triángulo
#     Escribe una función que devuelva el área de un triángulo dado su base y altura.

#     Mayor de una lista
#     Crea una función que reciba una lista de números y devuelva el mayor.

#     Contar letras
#     Escribe una función que cuente cuántas veces aparece una letra en una palabra.

# def greeting(name):
#     print(f"¡Hola {name.title()}, Bienvenido!")
# greeting("riCardo cArmona")

# def sum(num1,num2):
#     print(num1+num2)
# sum(10,45)

# def even_odd(num):
#     if num % 2 == 0:
#         print(f"El numero {num} es par")
#     else:
#         print(f"El numero {num} es impar")
# even_odd(3)

# def major(num):
#     if num >= 18:
#         print("Es mayor de edad")
#     else:
#         print("No es mayor de edad")
# major(15)

# def celsius_to_fahrenheit(celsius):
#     print ((celsius * 9/5) + 32)
# celsius_to_fahrenheit(45)

# def triangle(base, height):
#     print(base*height)
# triangle(10,12)

# def listM(list):
#     list1 = max(list)
#     print(list1)
# list = [1,88,5]
# listM(list)

def cont_letters(letter):
    contador = 0
    for x in letter:
        if letter.count(x) > 1:
            contador += 1
    print(f"la letra {x}, se repite {contador} veces")       
cont_letters("koala")



