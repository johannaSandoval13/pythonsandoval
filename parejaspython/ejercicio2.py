a=int(input("Ingrese un numero: "))
cont=0
if a>1:
 for i in range(2,a):
  if i%a==0:
   print(f"{a} No es un numero primo")
  else:
   print(f"{a} Es un numero primo")

    
