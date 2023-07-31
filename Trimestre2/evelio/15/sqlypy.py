import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="MiBaseDeDatos"
)

cursor = conexion.cursor()

id_persona = input("Ingrese el ID de la persona: ")
nombre = input("Ingrese el nombre de la persona: ")
apellido = input("Ingrese el apellido de la persona: ")
edad = input("Ingrese la edad de la persona: ")
departamento = input("Ingrese el departamento de la persona: ")

consulta = "INSERT INTO Personas (ID, Nombre, Apellido, Edad, Departamento) VALUES (%s, %s, %s, %s, %s)"
valores = (id_persona, nombre, apellido, edad, departamento)

cursor.execute(consulta, valores)

conexion.commit()

cursor.close()
conexion.close()
