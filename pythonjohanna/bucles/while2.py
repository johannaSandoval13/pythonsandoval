x,y=3,5
#Aqui se asignaron dos valores a las variables x e y respectivamente
cont=1
#Aqui se comienza un contador desde uno
while not(x%y==0 or y%x==0):
#Mientras que: el residuo de los numeros asignados en la variable x e y sea diferente de cero haga: 
    print(f'intento numero {cont}')
#Se impimira el numero de intentos por cada vez que el While no se cumpla
    x=int(input('ingrese numero'))
    y=int(input('ingrese numero'))
#El usuario debe asignar valores a las variables x e y respectivamente
    cont+=1
#Mientras se relicen iteraciones se aumentara el numero de intentos con el contador
print(f'{x} y {y} son factor')
#Cuando el usuario ingrese dos numeros cuyo modulo sea cero, se imprimira el anterior mensaje