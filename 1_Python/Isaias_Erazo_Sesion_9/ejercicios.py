# //////////////////////////  Aplicacion de Conocimiento  /////////////////////////

#1
def suma(a, b):
    return a + b

y = int(input("Primer dato a Sumar: "))
z = int(input("Segundo dato a Sumar: "))

resultado = suma(y, z)
print(f"El resultado es: {resultado} ")


#2
def area_triangulo(a, b):
    return (a * b) / 2

y = int(input("Dime la Base del triangulo: "))
z = int(input("Dime la altura del triangulo: "))

resultado = area_triangulo(y, z)
print(f"El area del triangulo es: {resultado} ")