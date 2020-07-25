from planCuentaDAO import planCuentaDAO


class ControladorPlanCuenta:
    def __init__(self,informacion=None):
        self.informacion=informacion


    def Consultar(self,buscar):
        objDao=planCuentaDAO()
        return objDao.Consultar(buscar)

    def Ingresar(self,informacion):
        objDao=planCuentaDAO()
        return objDao.Ingresar(informacion)

    def Modificar(self,informacion):
        objDao=planCuentaDAO()
        return objDao.Modificar(informacion)

    def Eliminar(self,informacion):
        objDao=planCuentaDAO()
        return objDao.Eliminar(informacion)
