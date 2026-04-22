stringVariasLineas = """
Elian Romero
Carlos Oñate
Quito Ecuador """

print(stringVariasLineas)

colegio = "ISM"
longitud =(len(colegio))
print(longitud)

print(len(colegio))

nombre = "Elian"
apellido = "Romero"
espacio= " "
nombreCompleto= nombre + espacio + apellido
print("mi nombre completo es: " + nombreCompleto)

#multiplicar la variable las veces que desea
print(nombreCompleto*4)

print("Python\nChallenge")

print("Days\tTopics")
print("nombre\tSema1\tSema2\tSema3")

print("Simbolo(\\)")
print("@")

print(f"Mi nombre es {nombre} y mi apellido es {apellido}")

letraPorLetra = "hola"
a ,b ,c ,d = letraPorLetra
print(d,a)

language = "Python"
primerosTres=language[0:3]
print(primerosTres)

ultimosTres=language[3:6]
print(ultimosTres)

ultimosTres=language[-3:]
print(ultimosTres)

#Invierte los caracteres
saludo= "Hola mundo"
print(saludo[::-1])

cambioMayuscula="treinta dias"
print(cambioMayuscula.capitalize())
print(cambioMayuscula.count("a"))

#  Nivel 1: Operaciones básicas

texto = "Programación Para Todos"  # 1. Crear variable
print(f"Contenido: {texto}")        # 2. Mostrar contenido
print(f"Longitud: {len(texto)}")    # 3. Cantidad de caracteres


# Nivel 2: Transformación de texto

print(f"Mayúsculas: {texto.upper()}")      # 4. Mayúsculas
print(f"Minúsculas: {texto.lower()}")      # 5. Minúsculas
print(f"Formato Título: {texto.title()}")  # 6. Cada palabra inicia en mayúscula
print(f"Capitalize: {texto.capitalize()}") # 7. Solo la primera letra de la frase


#  Nivel 3: Búsqueda y verificación

print(f"¿Empieza con Programación?: {texto.startswith("Programación")}")
print(texto[0:12]) # 8
print(f"¿Termina con Todos?: {texto.endswith("Todos")}")
print(texto[-5:])                 # 9
print(f"Posición de Para: {texto.find("Para")}")                         # 10
print(f"¿Contiene Python?: {'Python' in texto}")                        # 11


#  Nivel 4: Manipulación

nuevo_texto = texto.replace("Programación", "Python") # 12. Reemplazar
print(f"Reemplazo: {nuevo_texto}")

palabras = texto.split() # 13. Dividir en una lista
print(f"Split: {palabras}")

union = " - ".join(palabras) # 14. Unir con guiones
print(f"Unión: {union}")


#  Nivel 5: Índices

print(f"Primer carácter: {texto[0]}")  # 15. Índice 0
print(f"Último carácter: {texto[-1]}") # 16. Índice -1
print(f"Carácter posición 5: {texto[5]}") # 17. (Letra 'a')


#  Nivel 6: Aplicación simple

nombre_completo = "Elian Romero"
print(f"Hola, mi nombre es {nombre_completo}")

# 20. Crear acrónimo (Inciales)
# Explicación: Dividimos el nombre y tomamos la letra [0] de cada parte
acronimo = "".join([palabra[0] for palabra in nombre_completo.split()])
print(f"Acrónimo: {acronimo}")