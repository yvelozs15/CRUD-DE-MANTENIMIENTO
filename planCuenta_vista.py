import os
from ctr_planCuenta import  *
from planCuenta_modelo import planCuenta_modelo
from funciones import menu
ctr= ControladorPlanCuenta()

def Eliminar():
    id = input('INGRESE ID: ')
    if id.isdigit():
        datos = planCuenta_modelo(id=id)
        if ctr.Eliminar(datos):
            print("REGISTRO ELIMINADO CORRECTAMENTE")
        else:
            print("ERROR AL ELIMINAR REGISTRO")
    else:
        print("Digite el id en forma numerica")


def Consultar():
    buscar = input('INGRESE NOMBRE A BUSCAR: ')
    datos = ctr.Consultar(buscar)
    print("ID   CODIGO  GRUPO  DESCRIPCION  NATURALEZA   ESTADO")
    for registo in datos:
        print('{:2}  {:5}  {:8}   {:9}  {:14}  {:3}'.format(registo[0], registo[1], registo[2], registo[3],
                                                            registo[4], registo[5]))
   

def Insertar(rango):
    for i in range(int(rango)):
        codigo= input('INGRESE CODIGO:  ')
        grupo = input('INGRESE ID DEL GRUPO:  ')
        descripcion = input('INGRESE DESCRIPCION:  ')
        naturaleza = input("INGRESE NATURALEZA [D/A]:  ") 
        estado = input("Ingrese  ESTADO 1/0:  ") #1=true 0=false
        if codigo.isdigit() and grupo.isdigit() and naturaleza.isalpha() and estado.isdigit():
            datos = planCuenta_modelo(codigo=codigo, grupo=grupo, desc=descripcion, naturaleza=naturaleza,
                                      estado=estado)
            if ctr.Ingresar(datos):
                print("REGISTRO GUARDADO CORRECTAMENTE...")
            else:
                print("ERROR AL GUARDAR REGISTRO...")
        else:
            print("Digite correctamenta cada campo")

def Modificar():
    id = input('Ingrese Id: ')
    codigo = input('INGRESE CODIGO A MODIFICAR: ')
    grupo = input('INGRESE GRUPO A MODIFICAR: ')
    descripcion = input('INGRESE DESCRIPCION A MODIFICAR: ')
    naturaleza = input("INGRESE NATURALEZA D/A A MODIFICAR: ")
    estado = input("INGRESE ESTADO 1/0 a MODIFICAR: ")
    if id.isdigit() and codigo.isdigit() and grupo.isdigit() and naturaleza.isalpha() and estado.isdigit():
        datos = planCuenta_modelo(id=id, codigo=codigo, grupo=grupo, desc=descripcion, naturaleza=naturaleza,
                                  estado=estado)
        if ctr.Modificar(datos):
            print("REGISTO MODIFICADO CORRECTAMENTE...")
        else:
            print("ERROR AL MODIFICAR REGISTRO...")
    else:
        print("Digite correctamenta cada campo")


def ejecutarPlanCuenta():
    while True:
        opc = str(menu(('INGRESAR', 'CONSULTAR','MODIFICAR','ELIMINAR', 'RETORNAR AL MENU PRINCIPAL'), 'MENÚ PLAN CUENTA'))
        if opc=='1':
            print('<<<INSERTAR>>>')
            valor=input('INGRESE CANTIDAD TOTAL DE DATOS A DIGITAR:   ')
            try:
                Insertar(valor)
            except:
                print("Digite valor numerico")
        elif opc=='2':
            print('<<<CONSULTAR>>>')
            Consultar()
        elif opc=='3':
            print('<<<MODIFICAR>>>')
            Modificar()
        elif opc=='4':
            print('<<<ELIMINAR>>>')
            Eliminar()
        elif opc=='5':
            break
        elif opc!='5':
            print('<<<SELECCIONE UNA OPCION CORRECTA... >>>')
        input("PRECIONE UNA TECLA PARA CONTINUAR...")
        os.system('cls')

