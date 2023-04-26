#En este archivo se explica como hacer un bucle sencillo
i=1
sum=0
#Variable i es 1 y sum es 0, por ahora
while i<=5:
#Mientras que i sea menor que 5:
    print(i)
#Impirma en la terminal i (el cual ira aumentando en cada iteracion)
    sum=sum+i
#Aqui, se "actualiza" la variable y sum pasa a valer su mismo valor mas uno
    i+=1 
#Se ira sumando i=i+1 por cada iteracion 
print(f'la suma es ={sum}')
#Al finalizar cada iteracion se mostrara el resultado de las operaciones anteriores, generando asi una lista