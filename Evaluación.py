#EVALUACIÓN 1

#==== PARTE A ====

#Respuesta 1:
# a) Tipos de datos:
# nombre -> str
# edad -> int
# promedio -> float
# cursos -> list

# b) Salida en pantalla:
# <class "str">
# <class "int">
# <class "float">
# <class "list">
# 5

# c) El len(nombre) indica la cantidad de caracteres que tiene "Lucía" que incluye letras y símbolos.


# Respuesta 2:
# a) Print muestra información en pantalla, mientras que Input permite ingresar datos por el teclado
# b) Porque input() siempre devuelve un texto (string) y si se usa en cálculos sin convertirlo a int() o a float() puede causar error.
# c) / es división normal mientras que // es división entera sin los decimales y % devuelve solo el residuo
# d) print(sys.version)
# e) help("keywords")

# ===== PARTE B =====

# Código corregido

ancho = float(input("Ingrese el ancho del terreno: "))
largo = float(input("Ingrese el largo del terreno: "))
precio = float(input("Ingrese el precio por metro cuadrado: "))

area = ancho * largo
costo = area * precio

print("Área total:", area)
print("Costo estimado:", costo)

# a) Errores principales:
# input() devuelve texto y no números
# No se pueden multiplicar variables str toca convertirlas
# Para unir textos con numeros no se usa el +

# b) La corrección sirve porque:
# Se convierten los datos a float
# Se usan operaciones matemáticas válidas
# Se hace el print correctamente con el uso de la coma


# Construcción breve

frase = "Tecnología para todos"

print(frase.upper())
print(len(frase))
print("Python" in frase)
print(frase.replace("Tecnología", "Programación"))
print(frase.split())

# ===== PARTE C =====

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
pais = input("Ingrese su país: ")
ancho = float(input("Ingrese el ancho de la pared: "))
alto = float(input("Ingrese el alto de la pared: "))
precio = float(input("Ingrese el precio por metro cuadrado: "))

area = ancho * alto
costoTotal = area * precio
espacio= " "

nombreCompleto = nombre + espacio + apellido

print("---REPORTE FINAL---")
print(f"Nombre Completo: {nombreCompleto} ")
print(f"País: {pais}")
print(f"Area de la pared: {area} m2")
print(f"Costo Total: ${costoTotal}")

print("---INFORMACIÓN EXTRA---")
print(f"Nombre en mayusculas: {nombreCompleto.upper()}")
print(f"Longitud del nombre completo: {len(nombreCompleto)}")
print(f"Contiene letra a: {"a" in nombreCompleto.lower()}")
print(f"Costo total es mayor a 100: {costoTotal > 100}")

#22/4/2026