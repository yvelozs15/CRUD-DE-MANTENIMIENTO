from Conexion import Conector


class grupoDAO(Conector):
    def __init__(self):
        super().__init__()

    def Consultar(self,buscar):
        result=False
        try:
            sql="select * from tb_grupo where descripcion like '%"+ str(buscar) + "%' order by id"
            self.conectar()
            self.conector.execute(sql)
            result=self.conector.fetchall()
            self.conn.commit()
        except Exception as e:
            print("Error en la consulta de grupo",e)
            self.conn.rollback()
        finally:
            self.cerrar()
        return result

    def Ingresar(self, datos):
        correcto = True
        try:
            sql = "insert into tb_grupo(descripcion) values(%s)"
            self.conectar()
            self.conector.execute(sql, (datos.descripcion))
            self.conn.commit()
        except Exception as e:
            print("Error en insertar grupo", e)
            correcto = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto

    def Modificar(self, datos):
        correcto = True
        try:
            sql = "update tb_grupo set descripcion = %s where id = %s"
            self.conectar()
            self.conector.execute(sql, (datos.descripcion, datos.id))
            self.conn.commit()
        except Exception as e:
            print("Error en Modificar grupo", e)
            correcto = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto

    def Eliminar(self, datos):
        correcto = True
        try:
            sql = 'delete from tb_grupo where id= %s'
            self.conectar()
            self.conector.execute(sql, (datos.id))
            self.conn.commit()
        except Exception as e:
            print("Error en  Eliminar grupo", e)
            correcto = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto



