nota=int(input("Ingrese su nota: "))
if nota < 1 or nota > 7:
  print("Error en el numero ingresado!")
else:
  if nota < 4 :
    print("Reprobado")
  elif nota >= 4 and nota < 5:
    print("Regular")
  elif nota >= 5 and nota < 6:
    print("Ok")
  else:
    print("Bien!")