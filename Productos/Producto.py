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
        producto = (self.id_usuario, self.id_tipo, self.cantidad, fecha)

        try:
            cursor.execute(sql, producto)
            dataBase.commit()

            resultado = [cursor.rowcount, self]
        except:

            resultado = [0, self]

        return resultado
    
    def ver(self):
        
        sql = "SELECT * FROM productos"

        cursor.execute(sql)
        resultado = cursor.fetchall()

        return resultado


    def sacar(self):
         
        sql = "DELETE FROM productos WHERE id = (SELECT id FROM (SELECT MIN(id) AS id FROM productos) AS subconsulta);"
        
        try:
            cursor.execute(sql)
            dataBase.commit()

            resultado = [cursor.rowcount]

        except:
             resultado = [0]
             
        return resultado
    
    def eliminar(self):
         
        sql = "DELETE FROM productos WHERE id = (SELECT id FROM (SELECT MAX(id) AS id FROM productos) AS subconsulta);"

        try:
            cursor.execute(sql)
            dataBase.commit()

            resultado = [cursor.rowcount]
            
        except:
            resultado = [0]

        return resultado
    
    def eliminarTodo(self, id):
        sql = f"DELETE FROM productos WHERE id = %s"
        
        try:
            cursor.execute(sql, (id,))
            dataBase.commit()

            resultado = [cursor.rowcount]

        except:
            resultado = [0]
        return resultado
    



        

    def traerTipos(self):
            sql = "SELECT nombre FROM tipoProductos"
            cursor.execute(sql)
            resultado = cursor.fetchall()
            
            return resultado



