import csv

def suma_columna_csv(ruta_csv):
    columna_minus_7 = []

    with open(ruta_csv) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        next(csvReader)

        for row in csvReader:
            valor_columna_minus_7 = row[-7]
            if valor_columna_minus_7.isdigit():
                columna_minus_7.append(int(valor_columna_minus_7))

    suma_columna_minus_7 = sum(columna_minus_7)
    return suma_columna_minus_7

# Ejemplo de uso de la función:
ruta_csv = 'C:\\Jojo\\pythonsandoval\\csvejercicios\\Saber_11__2019-2.csv'
resultado_suma = suma_columna_csv(ruta_csv)
print("La suma de los valores en la columna -7 es:", resultado_suma)
