import os
os.system('cls')

cant_autosInt = 0
total_autosInt = 0
cant_motosInt = 0
total_motosInt = 0
cant_bicisInt = 0
total_bicisInt = 0
cant_patinetasInt = 0
total_patinetasInt = 0
controlBln = True
while controlBln == True:
    os.system('cls')
    op_vehiculoStr = input('---MENÚ DE OPCIONES---\n\n1. Motos\n2. Autos\n3. Bicicletas\n4. Patinetas\n5.Reporte\n ->  ')

    if op_vehiculoStr == '1':
        movimientoStr =  input('1. Entrada 2. Salida-> ')
        cantidadInt = int(input("Ingrese la cantidad de vehículos que desea ingresar: "))
        if movimientoStr == '1':
            cant_motosInt += cantidadInt
            
        if movimientoStr == '2':
            if cant_motosInt >= cantidadInt:
                cant_motosInt -= cantidadInt
        
            else:
                print('La cantidad de vehiculo a sacar no puede ser mayor a la cantidad de vehiculos actual')
                
    if op_vehiculoStr == '2':
        movimientoStr =  input('1. Entrada 2. Salida-> ')
        cantidadInt = int(input("Ingrese la cantidad de vehículos que desea ingresar: "))
        if movimientoStr == '1':
            cant_autosInt += cantidadInt
            
        if movimientoStr == '2':
            if cant_autosInt >= cantidadInt:
                cant_autosInt -= cantidadInt
        
            else:
                print('La cantidad de vehiculo a sacar no puede ser mayor a la cantidad de vehiculos actual')
                
    if op_vehiculoStr == '3':
        movimientoStr =  input('1. Entrada 2. Salida-> ')
        cantidadInt = int(input("Ingrese la cantidad de vehículos que desea ingresar: "))
        if movimientoStr == '1':
            cant_bicisInt += cantidadInt
            
        if movimientoStr == '2':
            if cant_bicisInt >= cantidadInt:
                cant_bicisInt -= cantidadInt
        
            else:
                print('La cantidad de vehiculo a sacar no puede ser mayor a la cantidad de vehiculos actual')
                
            
    if op_vehiculoStr == '4':
        movimientoStr =  input('1. Entrada 2. Salida-> ')
        cantidadInt = int(input("Ingrese la cantidad de vehículos que desea ingresar: "))
        if movimientoStr == '1':
            cant_patinetasInt += cantidadInt
            
        if movimientoStr == '2':
            if cant_patinetasInt >= cantidadInt:
                cant_patinetasInt -= cantidadInt
        
            else:
                print('La cantidad de vehiculo a sacar no puede ser mayor a la cantidad de vehiculos actual')
                
    if  op_vehiculoStr == '5' :
        print('Cantidad actual de motos es: ',cant_motosInt)
        print('Cantidad actual de autos es: ',cant_autosInt)
        print('Cantidad actual de bicicletas es: ',cant_bicisInt)
        print('Cantidad actual de patinetas es: ',cant_patinetasInt)
        
        controlBln = False