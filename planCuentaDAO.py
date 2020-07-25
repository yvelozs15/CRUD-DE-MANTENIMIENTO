from Conexion import Conector


class planCuentaDAO(Conector):
    def __init__(self):
        super().__init__()

    def Consultar(self,buscar):
        result=False
        try:
            sql="select * from tb_plancuenta where descripcion like '%"+ str(buscar) + "%' order by id"
            self.conectar()
            self.conector.execute(sql)
            result=self.conector.fetchall()
            self.conn.commit()
        except Exception as e:
            print("Error en la consulta de planCuenta",e)
            self.conn.rollback()
        finally:
            self.cerrar()
        return result

    def Ingresar(self,planCuenta):
        correcto=True
        try:
            sql="insert into tb_plancuenta(codigo,grupo,descripcion,naturaleza,estado) values(%s,%s,%s,%s,%s)"
            self.conectar()
            self.conector.execute(sql,(planCuenta.codigo,planCuenta.grupo,planCuenta.descripcion,planCuenta.naturaleza,planCuenta.estado))
            self.conn.commit()
        except Exception as e:
            print("Error en insertar planCuenta", e)
            correcto=False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto

    def Modificar(self,planCuenta):
        correcto = True
        try:
            sql="update tb_plancuenta set codigo=%s,grupo =%s,descripcion =%s,naturaleza=%s,estado=%s where id = %s"
            self.conectar()
            self.conector.execute(sql,(planCuenta.codigo,planCuenta.grupo,planCuenta.descripcion,planCuenta.naturaleza,planCuenta.estado,planCuenta.id))
            self.conn.commit()
        except Exception as e:
            print("Error en la Modificar planCuenta", e)
            correcto = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto


    def Eliminar(self,planCuenta):
        correcto =True
        try:
            sql='delete from tb_plancuenta where id= %s'
            self.conectar()
            self.conector.execute(sql, (planCuenta.id))
            self.conn.commit()
        except Exception as e:
            print("Error en la Eliminación planCuenta", e)
            correcto = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto
