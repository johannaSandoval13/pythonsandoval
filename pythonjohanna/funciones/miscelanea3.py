def crear_fibo():
    n = int(input("Ingrese la cantidad de numeros de la serie que desea conocer: "))
    while n <= 0:
        print("El numero no puede ser cero")
        n = int(input("Ingrese la cantidad de numeros de la serie que desea conocer: "))
    fibo = [0, 1]
    for i in range(2, n):
        fibo.append(fibo[i-1] + fibo[i-2])

    limite = int(input("Ingrese el numero hasta el que quiere que vaya la lista: "))

    for num in fibo:
        if num > n:
            break
        print(num)
crear_fibo()