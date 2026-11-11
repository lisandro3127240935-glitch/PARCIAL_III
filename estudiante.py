from conexionBD import cursor,conexion

class Estudiantes:
    def __init__(self,nombre,nota):
        self._nombre=nombre
        self._nota=nota
    @property
    def nombre(self):
        return self._nombre
    @property
    def nota(self):
        return self.nota 
    @nombre.setter
    def nombre(self,nombre):
        self._nombre=nombre
    @nota.setter
    def nota(self,nota):
        self.nota=nota

    def insertar(self):
        try:
            cursor.execute("INSERT into estudiante values (null,%s,%s)",(self._nombre,self._nota))
            conexion.commit()
            return True
        except:
            return False
    @staticmethod
    def consultar():
        try:
            cursor.execute("select * from estudiante")
            return cursor.fetchall()
        except:
            return []
    @staticmethod
    def eliminar(id):
        try:
            cursor.execute("delete from estudiante where id=%s", (id,))
            conexion.commit()
            return True
        except:
            return False
        
    def actualizar(self, id):
        try:
            # Quitamos la coma extra antes de WHERE
            sql = "UPDATE estudiante SET nombre = %s, nota = %s WHERE id = %s"
            valores = (self._nombre, self._nota, id)
            cursor.execute(sql, valores)
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar: {e}")
            return False
            return True
        except:
            return False