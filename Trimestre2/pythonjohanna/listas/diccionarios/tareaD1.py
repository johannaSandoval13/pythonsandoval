def valorTipo(diccionario, clave):
    if clave in diccionario:
        valor = diccionario[clave]
        tipoDato = type(valor)
        return valor, tipoDato
    else:
        return None, None
datos = {
    "mariposa": "Las mariposas son un tipo de insecto muy popular por los llamativos colores",
    'pi': 3.1416
}

print(datos)
buscar = input("Ingrese la clave a buscar: ")

valEncontrado, tipoDato = valorTipo(datos,buscar)

if valEncontrado is not None:
    print("Valor:", valEncontrado)
    print("Tipo de dato:", tipoDato)
else:
    print("La clave no existe en el diccionario.")
