import numpy as np
import time
import os

auto = []
autos = []
tipo = False
patente = 0
marca = False
precio = 0
valmulta = 0
fecmulta = 0
fecregistro = 0
nombre_propietario = " "
encontrado = False

#FUNCION PARA VALIDAR LA PATENTE DEL VEHICULO
def validar_patente(patente):
    if len(patente) < 6 or len(patente) > 6:
        return False
        print("PATENTE INVALIDA. PORFAVOR INGRESE DE NUEVO LA PATENTE.:")
    if len(patente) == 6:
        return True

#FUNCION PARA GRABAR DATOS DEL VEHICULO
def agregar_auto():
    tipo = input("POR FAVOR, INGRESE EL TIPO DE VEHICULO: ")
    patente = int(input("POR FAVOR INGRESE LOS 6 DIGITOS DE LA PATENTE: "))
    if validar_patente is True:
        print("SU PATENTE HA SIDO INGRESADA")        
    else:
        while not validar_patente(patente):
            print("PATENTE INVALIDA. PORFAVOR INGRESE DE NUEVO LA PATENTE")
            patente = int(input("POR FAVOR INGRESE LOS 6 DIGITOS DE LA PATENTE: "))
    marca = str(input("POR FAVOR INGRESE LA MARCA DEL VEHÍCULO: "))
    if len(marca) > 1 and len(marca) < 16:
        print(f'LA MARCA DEL VEHICULO ES {marca}')
    else:
        print("MARCA NO VALIDA, POR FAVOR INGRESE UNA MARCA QUE TENGA ENTRE 2 Y 15 CARACTERES")
        time.sleep(1)  

    precio = int(input("POR FAVOR INGRESE EL PRECIO DEL VEHICULO: "))
    fecmulta = int(input("POR FAVOR INGRESE EL VALOR DE LA MULTA: "))
    fecmulta = int(input("POR FAVOR INGRESE LA FECHA DE LA MULTA EN FORMATO AAMMDD: "))
    fecregistro = int(input("POR FAVOR INGRESE LA FECHA DEL REGISTRO EN FORMATO AAMMDD: "))
    nombre_propietario = str(input("POR FAVOR INGRESE EL NOMBRE DEL DUEÑO DEL VEHICULO: "))   

    autos.append(agregar_auto)
    print("SU REGISTRO SE HA HECHO CON EXITO")

auto = {
        'TIPO': tipo,
        'PATENTE': patente,
        'MARCA': marca,
        'PRECIO': precio,
        'VALOR DE LA MULTA': valmulta,
        'FECHA DE LA MULTA': fecmulta,
        'FECHA DE REGISTRO':fecregistro,
        'NOMBRE DEL PROPIETARIO':nombre_propietario,
    }

def buscarauto():
    patente = input("INGRESE LA PATENTE DEL VEHICULO A BUSCAR: ")
    encontrado = False
    for auto in autos:
        if auto['patente'] == patente:
            print("****INFORMACION DEL VEHICULO****")
            print("TIPO:", auto['TIPO'])    
            print("PATENTE:", auto['PATENTE'])
            print("MARCA:", auto['MARCA'])
            print("PRECIO:", auto['PRECIO'])
            print("VALOR DE LA MULTA:", auto['VALOR DE LA MULTA'])
            print("FECHA DE LA MULTA:", auto['FECHA DE LA MULTA'])
            print("FECHA DE REGISTRO:", auto['FECHA DE REGISTRO'])
            print("NOMBRE DEL PROPIETARIO:", auto['NOMBRE DEL PROPIETARIO'])                                  
            encontrado = True
            break
    if not encontrado:
        print("NO SE ENCONTRO NINGUN AUTO.")
        
certificados = []  