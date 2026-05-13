
# =========================
# ACTIVIDAD 7 - CICLOS
# =========================

# =========================
# EJERCICIO LISTA
# =========================

notas = [8.5, 6.0, 9.0, 7.0, 5.5]

suma = 0
aprobados = 0
reprobados = 0
cantidad = 0

for nota in notas:
    suma = suma + nota
    cantidad = cantidad + 1

    if nota >= 7:
        aprobados = aprobados + 1
    else:
        reprobados = reprobados + 1

promedio = suma / cantidad

print("=== EJERCICIO LISTAS ===")
print("Suma total:", suma)
print("Promedio:", promedio)
print("Aprobados:", aprobados)
print("Reprobados:", reprobados)


# ========================
# EJERCICIOS STRING
# ========================

contrasena = "Python2026"

letras = 0
numeros = 0
cantidad_o = 0

for caracter in contrasena:
    if caracter >= "A" and caracter <= "Z" or caracter >= "a" and caracter <= "z":
        letras = letras + 1

    if caracter >= "0" and caracter <= "9":
        numeros = numeros + 1

    if caracter == "o":
        cantidad_o = cantidad_o + 1

print("Cantidad de letras:", letras)
print("Cantidad de números:", numeros)
print("Cantidad de veces que aparece 'o':", cantidad_o)


# =========================================
# EJERCICIO CON SET
# =========================================

productos = {"teclado", "mouse", "monitor", "mouse", "impresora"}

contador_productos = 0
mas_6_letras = 0

for producto in productos:

    contador_productos = contador_productos + 1

    contador_letras = 0

    for letra in producto:
        contador_letras = contador_letras + 1

    if contador_letras > 6:
        mas_6_letras = mas_6_letras + 1

print("=== EJERCICIO SET ===")
print("Productos únicos:", contador_productos)
print("Productos con más de 6 letras:", mas_6_letras)


# ========================
# EJERCICIO CON BREAK
# ========================

correo = input("Ingrese su correo electrónico: ")

usuario = ""

for caracter in correo:

    if caracter == "@":
        break

    usuario = usuario + caracter

print("Nombre de usuario:", usuario)


# ===========================
# EJERCICIO CON CONTINUE
# ===========================

telefono = input("Ingrese su número de teléfono: ")

telefono_limpio = ""

for caracter in telefono:

    if caracter == " " or caracter == "-":
        continue

    telefono_limpio = telefono_limpio + caracter

print("Teléfono limpio:", telefono_limpio)



