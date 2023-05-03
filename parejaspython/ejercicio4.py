max= 0
while True:
    numero = int(input("Introduce numeros positivos, el programa acabara si se ingresa uno negativo: "))
    if numero < 0:
        break
    if numero > max:
        max = numero

print("El numero con mayor valor fue: ", max)