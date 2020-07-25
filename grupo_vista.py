import os
from ctr_grupo import *
from grupo_modelo import grupo_modelo
from funciones import menu
ctr= ControladorGrupo()

def eliminar():
    id = input('Ingrese Id:  ')
    if id.isdigit():
        datos = grupo_modelo(id=id)
        if ctr.Eliminar(datos):
            print("REGISTRO ELIMINADO CORRECTAMENTE")
        else:
            print("ERROR AL ELIMINAR REGISTRO")
    else:
        print("Digite correctamente el valor numerico")


def consultar():
    buscar = input('INGRESE NOMBRE A BUSCAR: ')
    if  buscar== "" or buscar.isalpha():
        datos = ctr.Consultar(buscar)
        print("ID   GRUPO")
        for registo in datos:
            print('{:5}  {:5}'.format(registo[0], registo[1]))
    else:
        print("Ingrese el valor a buscar correctamente")

def insertar(rango):
    for i in range(int(rango)):
        descripcion= input('INGRESE NOMBRE:  ')
        if descripcion.isalpha():
            modelo = grupo_modelo(descripcion=descripcion)
            if ctr.Ingresar(modelo):
                print("REGISTRO GUARDADO CORRECTAMENTE")
            else:
                print("ERROR AL GUARDAR REGISTRO")
        else:
            print("Digite la Descripcion tipo string")

def modificar():
    id = input('Ingrese Id: ')
    descripcion = input('INGRESE NOMBRE A MODIFICAR:  ')
    if descripcion.isalpha() and id.isdigit():
        modelo = grupo_modelo(id=id, descripcion=descripcion)
        if ctr.Modificar(modelo):
            print("REGISTO MODIFICADO CORRECTAMENTE")
        else:
            print("ERROR AL  MODIFICAR REGISTRO")
    else:
        print("Ingrese correctamente los datos")




def ejecutarGrupo():
    while True:
        opc = str(menu(('INGRESAR', 'CONSULTAR','MODIFICAR','ELIMINAR', 'RETORNAR AL MENU PRINCIPAL'), 'MENÚ GRUPO'))
        if opc=='1':
            print('<<<---INSERTAR DATOS--->>>')
            valor=input('INGRESE CANTIDAD TOTAL DE DATOS A DIGITAR:  ')
            try:
                insertar(valor)
            except:
                print("Ingrese valor numerico")
        elif opc=='2':
            print('<<<---CONSULTAR--->>>')
            consultar()
        elif opc=='3':
            print('<<<---MODIFICAR--->>>')
            modificar()
        elif opc=='4':
            print('<<<---ELIMINAR--->>>')
            eliminar()
        elif opc=='5':
            break
        elif opc!='5':
            print('<<<SELECCIONE UNA OPCION CORRECTA...   >>>')
        input("<<---PRESIONE UNA TECLA PARA CONTINUAR--->>")
        os.system('cls')


