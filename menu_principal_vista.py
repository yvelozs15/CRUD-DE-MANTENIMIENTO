import os
from funciones import menu
from planCuenta_vista import ejecutarPlanCuenta
from grupo_vista import ejecutarGrupo

def ejecutarMenuPrincipal():
    while True:
        opc = str(menu(('GRUPO DE CUENTAS', 'PLAN DE CUENTAS', 'SALIR'), 'MENÚ PRINCIPAL'))
        if opc=='1':
            ejecutarGrupo()

        elif opc=='2':
            ejecutarPlanCuenta()
        elif opc=='3':
            print('<<<GRACIAS POR USAR EL SISTEMA....>>>')
            input("PRESIONE UNA TECLA PARA CONTINUAR...")
            break
        elif opc!='3':
            print('<<<SELECCIONE UNA OPCION CORRECTA >>>')
        input("PRESIONE UNA TECLA PARA CONTINUAR...")
        os.system('cls')

ejecutarMenuPrincipal()