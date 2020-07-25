from grupoDAO import grupoDAO


class ControladorGrupo:
    def __init__(self,informacion=None):
        self.informacion=informacion


    def Consultar(self,buscar):
        objDao=grupoDAO()
        return objDao.Consultar(buscar)

    def Ingresar(self,informacion):
        objDao=grupoDAO()
        return objDao.Ingresar(informacion)

    def Modificar(self,informacion):
        objDao=grupoDAO()
        return objDao.Modificar(informacion)

    def Eliminar(self,informacion):
        objDao=grupoDAO()
        return objDao.Eliminar(informacion)
