print("Ingrese dos numeros por favor: ")
a=int(input("a= "))
b=int(input("b= "))
while b>0:
    c= a/b
    print(c)
    break
else: 
    ("lo siento, la operacion no puede ser dada")

try:
    print("Ingrese dos numeros por favor: ")
    a=int(input("a= "))
    b=int(input("b= "))
    c= a/b
    print(c) 
except ZeroDivisionError:
    print("No pongas cero en ningun numero, por favor, intenta de nuevo")
    a=int(input("a= "))
    b=int(input("b= "))
    c= a/b
    print(c) 

