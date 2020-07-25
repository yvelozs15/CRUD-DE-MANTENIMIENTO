def menu(opciones,titulo):
    print('*'*20)
    print('{}'.format(titulo))
    print('*'*20)
    for op in range(0,len(opciones)):
        print("{}){}".format(op+1, opciones[op]))
    op= input('ELIJA UNA OPCIÓN[1...{}]: '.format(len(opciones)))
    return op
