class planCuenta_modelo:
    def __init__(self, id=0, codigo=0,grupo=0, desc='',naturaleza='',estado=True):
        self.id = id
        self.codigo=codigo
        self.grupo=grupo
        self.descripcion = desc
        self.naturaleza=naturaleza
        self.estado=estado
