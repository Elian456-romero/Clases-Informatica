# 1
edad = 25  # entero

# 2
estatura = 1.75  # float

# 3
base = float(input("Base del triángulo: "))
altura = float(input("Altura del triángulo: "))
areaTriangulo = 0.5 * base * altura
print("Área del triángulo:", areaTriangulo)

# 5
print("Ingresa los 3 lados del triangulo")
a = float(input("Lado a: "))
b = float(input("Lado b: "))
c = float(input("Lado c: "))
perimetroTriangulo = a + b + c
print("Perímetro del triángulo:", perimetroTriangulo)

# 6
print("Ingresa la longitud y el ancho de un rectangulo")
longitud = float(input("Longitud del rectángulo: "))
ancho = float(input("Ancho del rectángulo: "))
area_rectangulo = longitud * ancho
perimetro_rectangulo = 2 * (longitud + ancho)
print("Área:", area_rectangulo)
print("Perímetro:", perimetro_rectangulo)

# 7
radio = float(input("Radio del círculo: "))
pi = 3.14
area_circulo = pi * radio**2
circunferencia = 2 * pi * radio
print("Área:", area_circulo)
print("Circunferencia:", circunferencia)

# 9
x1, y1 = 2, 2
x2, y2 = 6, 10
pendiente = (y2 - y1) / (x2 - x1)
distancia = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print("Pendiente:", pendiente)
print("Distancia:", distancia)

# 11
x = float(input("Valor de x: "))
y = x**2 + 6*x + 9
print("y =", y)
# Para que y = 0 → x = -3

# 12
import math
longitud = math.sqrt(2**2 + 3**2 + 6**2)
print("Longitud:", longitud)

# 13
print("python" in "python y dragón")
print("dragón" in "python y dragón")

# 14
oracion = "Espero que este curso no esté lleno de jerga."
print("jerga" in oracion)

# 15
texto = "python y dragón"
print("python" in texto and "dragón" in texto)

# 16
longitud = len("python")
valor_float = float(longitud)
valor_str = str(valor_float)
print(valor_float, valor_str)

# 18
print(7 / 3 == 2.7)  # False

# 19
print(type("10") == type(10))  # False

# 20
print(int("9.8") == 10)  # Esto dará error
# Corrección:
print(int(float("9.8")) == 10)  # False