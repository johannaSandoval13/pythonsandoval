n=int(input('ingrese numero'))
#El usuario debe ingresar un numero
i=1
#aqui se crea un contador, que empezara en 1
while i<n:
#mientras que el contador sea menor que el numero dado por el usuario:
    if i%7==0:
    #Si, el modulo entre el contador y 7 es cero imprima el mensaje de la linea 9
        print(f'{i} es multiplo de 7')
    else:
    #Si no, simplemente imprima el numero que este en el contador
        print(i)
    i+=1
    #El contador debe ir aumentando e iteracion en iteracion