#Este programa trata solicita al usuario 3 numeros diferentes* y despues calcula el mayor entre estos: 
x=int(input('ingrese numero'))
y=int(input('ingrese numero'))
z=int(input('ingrese numero'))
#para esto, no usaremos operadores logicos (and, or, not), pero si if y else
#al usar estos, debemos de tomar en cuenta su indentación (limitacion de bloques de codigo)
if x>y:
#La primera opcion es si x es mayor que y, en caso diferente, pasaremos a otro if
    if x>z:
    #La segunda opcion es si x es mayor que z, en caso sea cierto se impirmirá el texto de la siguiente linea
        print(f'el mayor es {x}')
    #en caso contratio, se  efectuara la siguiente linea:
    else:
        print(f'el mayor es {z}')
else:
#Si el primer if de alla ariba no es "verdadero" no se efactuara el que esta adentro de este, por ende se efectuaran una de las dos siguientes lineas:  
    if y>z:
    #En caso y sea mayor que y
        print(f'el mayor es {y}')
    else:
    #o por el contrario, z sea mayor que y
        print(f'el mayor es {z}')