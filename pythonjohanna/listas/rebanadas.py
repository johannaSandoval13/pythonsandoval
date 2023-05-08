import random
lista=[]
tam=random.randint(10,20)
for j in range(tam):
    num=random.random()*5
    num=round(num,1)
    lista.append(num)
print(lista)
aprobados=[x for x in lista if x>3]
print(f"Los aprobados fueron: {len(aprobados)}, con las calificaciones: ",aprobados)
reprobados=[x for x in lista if x<3]
print(f"Los aprobados fueron: {len(reprobados)}, con las calificaciones: ",reprobados)

