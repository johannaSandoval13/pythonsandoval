import random
lista=[]
suma=0
tam=random.randint(20,30)
for j in range(tam):
    num=random.random()*5
    num=round(num,1)
    lista.append(num)
    suma += num
print(lista)
#lista aprobados
aprobados=[]
aprobados=[x for x in lista if x>3]
#lista reprobados
reprobados=[x for x in lista if x<3]
#ordenar lista aprobados
for i in range (1,len(aprobados)):
    for j in range(len(aprobados)-i):
            if aprobados[j] > aprobados[j+1]:
                aux1=aprobados[j]
                aprobados[j]=aprobados[j+1]
                aprobados[j+1]=aux1
#print(aprobados)
print(f"Los aprobados fueron: {len(aprobados)}, con las calificaciones: ",aprobados)
#ordenar lista reprobados
for k in range (1,len(reprobados)):
    for l in range(len(reprobados)-k):
            if reprobados[l] > reprobados[l+1]:
                aux2=reprobados[l]
                reprobados[l]=reprobados[l+1]
                reprobados[l+1]=aux2
#print(reprobados)
print(f"Los aprobados fueron: {len(reprobados)}, con las calificaciones: ",reprobados)
#promedio
prom=suma / len(lista)

grupo1=[reprobados[i:i+1] for i in range (1,2)]
grupo2=[reprobados[i:i+2] for i in range (2,3)]
grupo3=[aprobados[i:i+3] for i in range (4,5)]
grupo4=[aprobados[i:i+4] for i in range (5,6)]

print("El grupo 1 es: ",grupo1)
print("El grupo 2 es: ",grupo2)
print("El grupo 3 es: ",grupo3)
print("El grupo 4 es: ",grupo4)

print("El promedio es: ",prom)


