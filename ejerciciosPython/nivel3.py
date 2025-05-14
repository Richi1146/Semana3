# 🔴 Nivel Avanzado

#     Validar contraseña segura
#     Escribe una función que valide si una contraseña cumple con requisitos de seguridad (mayúsculas, minúsculas, números y símbolos).
#     Simular dado
#     Crea una función que simule el lanzamiento de un dado de 6 caras.

#     Suma de elementos únicos
#     Escribe una función que reciba una lista de números y devuelva la suma de los elementos únicos.

#     Generador de contraseñas
#     Crea una función que genere una contraseña aleatoria de una longitud dada.

#     Composición de funciones
#     Escribe una función que reciba otra función como parámetro y aplique una composición de funciones.
import random
import re

def validarcontraseña(contraseña):
    if (len(contraseña) >= 8 and
        re.search(r"[A-Z]", contraseña) and
        re.search(r"[a-z]", contraseña) and
        re.search(r"\d", contraseña) and
        re.search(r"[!@#$%^&*()-=+{};:,<.>]", contraseña)):
        return True
    else:
        return False

if validarcontraseña("Hola123*"):
    print("Contraseña segura.")
else:
    print("La contraseña no cumple con los requisitos de seguridad.")

def list_num(list):
    list2 = []
    for x in list:
        if list.count(x) == 1:
            list2.append(x)
            suma = sum(list2)
    print(suma)

list1 = [2,4,6,8,1,1,2,2]
list_num(list1)

def dados():
    return random.randint(1,6)
print(dados())

def compose(func1, func2, valor):
    return func1+func2+valor
 
def func1():
    return 1+1

def func2():
    return 2

print(compose(func1(),func2(),4))