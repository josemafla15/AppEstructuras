from Usuarios import conexion
from datetime import datetime

conectar = conexion.conectar()
dataBase = conectar[0] 
cursor = conectar[1]

class Producto:

    def __init__(self, id_usuario, id_tipo, cantidad):
        self.id_usuario = id_usuario
        self.id_tipo = id_tipo
        self.cantidad = cantidad

    def anadir(self):

        



        fecha = datetime.now()
        
        sql = "INSERT INTO productos VALUES (null, %s, %s, %s, %s)"
        producto = ()

    def traerTipos(self):
            sql = "SELECT nombre FROM tipoProductos"
            cursor.execute(sql)
            resultado = cursor.fetchall()
            
            return resultado


