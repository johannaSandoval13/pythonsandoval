def alimentar(diccionario):
    while True:
        palabra1 = input("Ingrese una palabra en español o ingrese 'salir' para terminar: ")
        if palabra1 == "salir":
            break
        palabra2 = input("Ingrese la traducción de la palabra en ingles: ")
        diccionario[palabra1] = palabra2
def usar(diccionario):
    while True:
        palabra = input("Ingrese clave a Usar o 'salir' para terminar: ")
        if palabra == "salir":
            break
        if palabra in diccionario:
                trad = diccionario[palabra]
                print("Traduccion de la palabra:", trad)
        else:
                print("La palabra no esta en el diccionario")

espaIng = {}
ingEspa = {}
print("♥Alimentar diccionario Español-Inglés♥")
alimentar(espaIng)
print("♥Alimentar diccionario Inglés-Español♥")
alimentar(ingEspa)
print("♥Usar Diccionario Español-Inglés♥")
usar(espaIng)
print("♥Usar Diccionario Inglés-Español♥")
usar(ingEspa)



