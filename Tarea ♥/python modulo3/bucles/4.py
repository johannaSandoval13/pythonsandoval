cantidad=int(input("Escriba la cantidad de números a sumar: "))
suma=0
for variable in range(cantidad):
   numero=int(input("Número: "))
   suma+=numero
print("Total de la suma:", suma)