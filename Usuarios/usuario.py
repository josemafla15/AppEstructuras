from Usuarios import conexion as conexion 
from datetime import datetime

conectar = conexion.conectar()
dataBase = conectar[0]
cursor = conectar[1]

class Usuario:

    def __init__(self, nombre, apellidos, correo, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.correo = correo
        self.password = password

    def registrarse(self):

        fecha = datetime.now()
        sql = "INSERT INTO usuarios VALUES (null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellidos, self.correo, self.password, fecha)

        try:
            cursor.execute(sql, usuario)
            dataBase.commit()
            resultado = [cursor.rowcount, self]

        except:
            resultado = [0, self]

        return resultado


    def loguearse(self):
        
        sql = "SELECT * FROM usuarios WHERE correo = %s AND password = %s"
        usuario = (self.correo, self.password)

        cursor.execute(sql, usuario)
        resultado = cursor.fetchone()

        return resultado
