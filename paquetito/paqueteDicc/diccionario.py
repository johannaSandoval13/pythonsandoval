print("Hola, vamos a crear un directorio juntos!")
def ingresar_contactos():
    contactos = {}
    while True:
        nombre = input("Ingrese el NOMBRE del contacto (o 'salir' para terminar): ")
        if nombre.lower() == "salir":
            break
        numero = input("Ingrese el NUMERO de contacto: ")
        contactos[nombre] = numero
    return contactos

mis_contactos = ingresar_contactos()
print("Contactos ingresados:")
for nombre, numero in mis_contactos.items():
    print(nombre + ": " + numero)
