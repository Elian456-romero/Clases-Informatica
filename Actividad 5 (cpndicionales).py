nota= int(input("Ingresa tu nota: ")) 

if nota > 90:
    print("Tu nota es A")
else:
    if nota > 80:
        print("Tu nota es B")
    else:
        if nota > 70:
            print("Tu nota es C")
        else:
            if nota > 50:
                ("Tu nota es D")
            else:
                if nota < 49:
                    print("Reprobado")


print("Ingrese un número: ")
numero = int(input())

if numero == 0:
    print("El número es cero")
else:
    if numero > 0:
        if numero % 2 == 0:
            print("El número es positivo y par")
        else:
            print("El número es positivo e impar")
    else:
        if numero % 2 == 0:
            print("El número es negativo y par")
        else:
            print("El número es negativo e impar")
print("Fin del programa")


print ("Ingrese un número")
b = int(input())
if b > 0 and b % 2 == 0:
    print("El número es positivo y par")
elif b > 0 and b % 2 == 1:
    print("El número es positivo e impar")
elif b < 0 and b % 2 == 0:
    print("El número es negativo y par")
elif b < 0 and b % 2 == 1:
    print("El número es negativo e impar")
else:
    print("El numero es cero")

numero= int(input("Ingrese un número: "))
print("El numero es cero" if numero == 0 else print("El numero es par positivo" if numero > 0 and numero % 2 == 0 else print("El numero es impar positivo" if numero > 0 and numero % 2 == 1 else print("El numero es par negativo" if numero < 0 and numero % 2 == 0 else print("El numero es impar negativo")))))