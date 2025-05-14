# 🟡 Nivel Intermedio

#     Filtrar pares
#     Crea una función que reciba una lista de números y devuelva solo los pares.

#     Palíndromo
#     Escribe una función que determine si un texto es un palíndromo.

#     Factorial
#     Crea una función que calcule el factorial de un número entero positivo.

#     Eliminar duplicados
#     Escribe una función que reciba una lista y devuelva una nueva sin elementos repetidos.

#     FizzBuzz
#     Crea una función que reciba un número y devuelva "Fizz", "Buzz" o "FizzBuzz" según las reglas del juego.

#     Contar vocales
#     Escribe una función que reciba una cadena y devuelva la cantidad de vocales.

#     Invertir texto
#     Crea una función que invierta una cadena de texto.

# list = [1,88,5,24,33]
# def pair(list):
#     list1 = []
#     for num in list:
#         if num % 2 == 0:
#             list1.append(num)
#     print(list1)       
# pair(list)

# def palindromo(palabra):
#     if palabra == palabra[::-1]:
#         print("Es un palindromo")
#     else:
#         print("No es un palindromo")
# nombre = "ana"
# palindromo(nombre)

# nombre1 = "carlos"
# palindromo(nombre1)

# def factorial(n):
#   if n == 0:
#     return 1  # Caso base: el factorial de 0 es 1
#   else:
#     return n * factorial(n-1)  # Caso recursivo: n! = n * (n-1)!
# # Ejemplo de uso:
# numero = 5
# resultado = factorial(numero)
# print(f"El factorial de {numero} es: {resultado}") 



# def duplicate_list(list):
#     for x in list:
#         if list.count(x) > 1:
#             list.remove(x)       
#     print(list)   

# list1 = [1,2,3,3,3,4,4,5,6,8]
# duplicate_list(list1)




# def fizz_buzz(numero):
#     if numero % 3 == 0 and numero % 5 ==0:
#         print("FIZZBUZZ")
#     elif numero % 3 == 0:
#         print("FIZZ")
#     elif numero % 5 == 0:
#         print("BUZZ")

# fizz_buzz(int(input("Ingresa un numero: ")))

# def vocales(cadena):
#     vocales = "aeiou"
#     contador = 0
#     for letters in cadena:
#             if letters in vocales:
#                 contador += 1
#     print(contador)
# vocales("bellotaaa")

# def invert_text(text):
#         print(text[::-1])
# invert_text("hola")



