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

def validate_password(password):pass

def list_num(list):
    list2 = []
    for x in list:
        if list.count(x) == 1:
            list2.append(x)
            suma = sum(list2)
    print(suma)




list1 = [2,4,6,8,1,1,2,2]
list_num(list1)