import random
u=int(input("Adivina un numero entre 1 y 20: "))
n = random.randint(1, 20)
while u != n:
    if n > u:
        print('No, es mayor')
    else:
        print('No, es menor')
    u=int(input("Adivina un numero entre 1 y 20: "))
print (f"Si, el numero es {n}!")