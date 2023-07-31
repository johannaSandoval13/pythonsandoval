#ejemplo
import random
tup=()
tam=(random.randint(5,15))

for i in range(tam):
    n=random.randint(1,100)
    tup+=(n,)
print(tup)

#practica
tup1=()
tam1=(random.randint(5,20))
for i in range(tam1):
    n1=random.randint(50,100)
    tup1+=(n1,)

mitadTup = tup1[:len(tup1)//2]

print("lista original",tup1)
print("mitad de la lista",mitadTup)
    