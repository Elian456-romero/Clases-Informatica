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