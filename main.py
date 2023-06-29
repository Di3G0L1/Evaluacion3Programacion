from funciones import *

menu = True
while menu:   

    import os
    os.system("cls")
    print("********BIENVENIDO AUTO SEGURO, POR FAVOR ELIJA UNA OPCION********")
    print("1. GRABAR ")
    print("2. BUSCAR")
    print("3. IMPRIMIR EN CERTIFICADOS")
    print("4. SALIR ")
    try:
        op = int(input("INGRESE OPCIÓN :\n"))
        if (op > 0 and op < 5):
            if (op == 1):
                agregar_auto()
            if (op == 2):
                buscarauto()
                if encontrado == True:
                    print([auto])
        
        else:
            print("OPCION NO VALIDA")
            time.sleep(1)
            
    except:
        print("TIPO DE OPCION NO PERMITIDA")
        time.sleep(1)