from Estudiantes import *
import csv
estudiantes=[]
with open('C:\\Jojo\\pythonsandoval\\csvejercicios\\Saber_11__2019-2.csv') as csvDataFile:
    csvReader=csv.reader(csvDataFile)
    for row in csvReader:
        print(row[-1],row[])
        break
        #obj=Estudiantes(row[6],row[3],row[-7],row[-1])
        #print(obj.verDatos())
        #estudiantes.append(obj)
#for ap in estudiantes:
#    print(ap.getNombre())