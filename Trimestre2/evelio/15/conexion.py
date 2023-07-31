import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="distribuidora_sena"
)

cursor = conexion.cursor()

codigo = input("Ingrese el código del cliente: ")
id_cliente = input("Ingrese el ID del cliente: ")
primer_apellido = input("Ingrese el primer apellido del cliente: ")
segundo_apellido = input("Ingrese el segundo apellido del cliente (opcional): ")
nombres = input("Ingrese los nombres del cliente: ")
correo = input("Ingrese el correo del cliente: ")

consulta = "INSERT INTO clientes (codigo, id, primer_apellido, segundo_apellido, nombres, correo) VALUES (%s, %s, %s, %s, %s, %s)"
valores = (codigo, id_cliente, primer_apellido, segundo_apellido, nombres, correo)

cursor.execute(consulta, valores)

conexion.commit()

cursor.close()
conexion.close()
