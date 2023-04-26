#Aqui se asignaron dos numeros a las variables num1 y num2 respectivamente
num1,num2=100,50
#Aqui, de la linea 4 a la 8 se impirmira un "Menu de opciones" ,
print('1-sumar')
print('2-restar')
print('3-multiplicar')
print('4-dividir')
print('5-residuo')
#de el cual el usuario debe seleccionar una opcion
op=int(input('que operacion?'))
#Dependiendo de el numero que digite el usuario se efectuara una de las opciones mencionadas en el "menu de opciones"
match op:
    case 1:
        print(num1+num2)
    case 2:
        print(num1-num2)
    case 3:
        print(num1*num2)
    case 4:
        print(num1/num2)# //  /
    case 5:    
        print(num1%num2)
#Si bien en estructura no son muy similares, en funcion los condicionales Matchcase e If son muy similares