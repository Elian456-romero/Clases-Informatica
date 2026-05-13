"""opcion = ""
while opcion != "c":
    print("Menú de opciones:")
    print("a. Opción 1")
    print("b. Opción 2")
    print("c. Salir")
    opcion = input("Seleccione una opción: ")       
    print (opcion)
    if opcion == "a":
        print ("Hola Bienvenido")
    elif opcion == "b":
        print ("Estamos aprendiendo python")
    elif opcion == "c":
        print("Saliendo del programa...")
    else:
        print("Opcion no valida")

numbers = [0,1,2,3,4,5]
for number in numbers:
    print (f"Su iterador es {number}")

notas=[8,7,9,10]
suma=0
for nota in notas:
    suma=suma+nota
promedio=suma/len(notas)
print(promedio)

notas=[8,7,9,10]
suma=0
contador=0

for nota in notas:
    suma=suma+nota
    contador+=1
promedio=suma/contador
print(f"El promedio es {promedio}")

language= "P y t h o n"
for letter in language:
    print(letter)

palabra = input ("Ingrese una palabra: ").lower()
vocales = 0

for letra in palabra:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        vocales = vocales + 1
print(f"La cantidad de vocales en la palabra es: {vocales}")
print(f"La cantidad de consonantes en la palabra es: {len(palabra) - vocales}")
print(f"El total de letras: {len(palabra)}")

itCompanies = {"Facebook", "Google", "Apple", "Facebook"}
for company in itCompanies:
    print(company)

numbers= ["1", "2", "4", "3" , "5"]
for number in numbers:
    print (number)
    if number == "3":
        print("Numero Encontrado")
        break
    else: 
        print("Numero no existe")"""


lista=[1,2,3,4,5,6,7]
numbers=int(input("Ingrese un numero: "))
for i in lista:
    if i == numbers:
        print("Numero Encontrado")
        break
else:        
    print("Numero no existe")

cedulaLimpia=""
cedula= input("Ingrese su numero de cedula: ")
for caracter in cedula:
    if caracter == "-" or caracter == " ":
        continue
    cedulaLimpia= cedulaLimpia + caracter
print(f"Su cedula sin espacios ni guiones es: {cedulaLimpia}")

