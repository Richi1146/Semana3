def greeting(name):
    print(f"¡Hola {name.title()}, Bienvenido!")
greeting("riCardo cArmona")

def sum(num1,num2):
    print(num1+num2)
sum(10,45)

def even_odd(num):
    if num % 2 == 0:
        print(f"El numero {num} es par")
    else:
        print(f"El numero {num} es impar")
even_odd(3)

def major(num):
    if num >= 18:
        print("Es mayor de edad")
    else:
        print("No es mayor de edad")
major(15)

def celsius_to_fahrenheit(celsius):
    print ((celsius * 9/5) + 32)
celsius_to_fahrenheit(45)

def triangle(base, height):
    print(base*height)
triangle(10,12)

def listM(list):
    list1 = max(list)
    print(list1)
list = [1,88,5]
listM(list)

def cont_letters(letter):
    contador = 0
    for x in letter:
        if letter.count(x) > 1:
            contador += 1
    print(f"la letra {x}, se repite {contador} veces")       
cont_letters("koala")

