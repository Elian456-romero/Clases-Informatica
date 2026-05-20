numero= int(input("Ingrese un numero: "))
limiteSuperior= int(input("Ingrese limite superior: "))
limiteInferior= int(input("Ingrese limite inferior: "))
for number in range (limiteInferior,limiteSuperior+1):
    resultado = numero*number
    print (f"{numero} x {number} = {resultado}") 

notas= [5, 8, 9, 7, 10]
suma=0
cantidad=0
for i in range (1,4):
    suma= suma + notas[i]
    cantidad=cantidad +1
promedio= suma / cantidad
print("Promedio de notas parciales: ", promedio)
