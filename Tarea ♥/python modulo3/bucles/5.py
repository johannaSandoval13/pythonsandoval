palabra=input("ingrese una palabra: ")
print("Vocales que hay en la palabra:")
for x in "aeiou":
  if x in palabra:
    print(x)