import json
import requests
import modules.getClientes as getCli
from tabulate import tabulate
import os
import time


def updateClienteNombre(codigo):
    while True:
        if(codigo != None):
            cliente= getCli.getClienteCodigos2((codigo))
            if (cliente):
                print(tabulate(cliente, headers="keys", tablefmt="github"))
                opc=int(input("""
                    ¿Este es el cliente que desea actualizar el nombre?
                            1. Si
                            2. No
                """))
                if(opc):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    cliente[0]["nombre_cliente"] = input("ingrese el nuevo nombre del cliente: ")
                    peticion = requests.put(f'http://154.38.171.54:5001/cliente/{cliente[0].get("id")}', headers= headers, data= json.dumps(cliente[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el cliente {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del cliente")
        

def updateClienteNombreContacto(codigo):
    while True:
        if(codigo != None):
            cliente= getCli.getClienteCodigos2((codigo))
            if (cliente):
                print(tabulate(cliente, headers="keys", tablefmt="github"))
                opc=int(input("""
                    ¿Este es el cliente en el que desea actualizar el nombre de contacto?
                            1. Si
                            2. No
                """))
                if(opc):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    cliente[0]["nombre_contacto"] = input("Ingrese el nuevo nombre de contacto")
                    
                    peticion = requests.put(f'http://154.38.171.54:5001/cliente/{cliente[0].get("id")}', headers= headers, data= json.dumps(cliente[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el cliente {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del cliente")


def updateClienteApellidoContacto(codigo):
    while True:
        if(codigo != None):
            cliente= getCli.getClienteCodigos2((codigo))
            if (cliente):
                print(tabulate(cliente, headers="keys", tablefmt="github"))
                opc=int(input("""
                    ¿Este es el cliente que desea actualizar el apellido de contacto?
                            1. Si
                            2. No
                """))
                if(opc):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    cliente[0]["apellido_contacto"] = input("ingrese el nuevo apellido del contacto del cliente: ")
                    peticion = requests.put(f'http://154.38.171.54:5001/cliente/{cliente[0].get("id")}', headers= headers, data= json.dumps(cliente[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el cliente {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del cliente")



def updateClienteTelefono(codigo):
    while True:
        if(codigo != None):
            cliente= getCli.getClienteCodigos2((codigo))
            if (cliente):
                print(tabulate(cliente, headers="keys", tablefmt="github"))
                opc=int(input("""
                    ¿Este es el cliente que desea actualizar el telefono?
                            1. Si
                            2. No
                """))
                if(opc):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    cliente[0]["telefono"] = input("ingrese el nuevo telefono del cliente: ")
                    peticion = requests.put(f'http://154.38.171.54:5001/cliente/{cliente[0].get("id")}', headers= headers, data= json.dumps(cliente[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el cliente {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del cliente")


def updateClienteFax(codigo):
    while True:
        if(codigo != None):
            cliente= getCli.getClienteCodigos2((codigo))
            if (cliente):
                print(tabulate(cliente, headers="keys", tablefmt="github"))
                opc=int(input("""
                    ¿Este es el cliente que desea actualizar el fax?
                            1. Si
                            2. No
                """))
                if(opc):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    cliente[0]["fax"] = input("ingrese el nuevo fax del cliente: ")
                    peticion = requests.put(f'http://154.38.171.54:5001/cliente/{cliente[0].get("id")}', headers= headers, data= json.dumps(cliente[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el cliente {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del cliente")


def updateClienteLineaDireccion1(codigo):
    while True:
        if(codigo != None):
            cliente= getCli.getClienteCodigos2((codigo))
            if (cliente):
                print(tabulate(cliente, headers="keys", tablefmt="github"))
                opc=int(input("""
                    ¿Este es el cliente que desea actualizar la linea de direccion 1?
                            1. Si
                            2. No
                """))
                if(opc):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    cliente[0]["linea_direccion1"] = input("ingrese la nueva linea de direccion 1 del cliente: ")
                    peticion = requests.put(f'http://154.38.171.54:5001/cliente/{cliente[0].get("id")}', headers= headers, data= json.dumps(cliente[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el cliente {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del cliente")


def updateClienteLineaDireccion2(codigo):
    while True:
        if(codigo != None):
            cliente= getCli.getClienteCodigos2((codigo))
            if (cliente):
                print(tabulate(cliente, headers="keys", tablefmt="github"))
                opc=int(input("""
                    ¿Este es el cliente que desea actualizar la linea de direccion 2?
                            1. Si
                            2. No
                """))
                if(opc):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    cliente[0]["linea_direccion2"] = input("ingrese la nueva linea de direccion 2 del cliente: ")
                    peticion = requests.put(f'http://154.38.171.54:5001/cliente/{cliente[0].get("id")}', headers= headers, data= json.dumps(cliente[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el cliente {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del cliente")


def updateClienteCiudad(codigo):
    while True:
        if(codigo != None):
            cliente= getCli.getClienteCodigos2((codigo))
            if (cliente):
                print(tabulate(cliente, headers="keys", tablefmt="github"))
                opc=int(input("""
                    ¿Este es el cliente que desea actualizar la ciudad?
                            1. Si
                            2. No
                """))
                if(opc):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    cliente[0]["ciudad"] = input("ingrese la nueva ciudad del cliente: ")
                    peticion = requests.put(f'http://154.38.171.54:5001/cliente/{cliente[0].get("id")}', headers= headers, data= json.dumps(cliente[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el cliente {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del cliente")



def updateClienteRegion(codigo):
    while True:
        if(codigo != None):
            cliente= getCli.getClienteCodigos2((codigo))
            if (cliente):
                print(tabulate(cliente, headers="keys", tablefmt="github"))
                opc=int(input("""
                    ¿Este es el cliente que desea actualizar la region?
                            1. Si
                            2. No
                """))
                if(opc):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    cliente[0]["region"] = input("ingrese la nueva region del cliente: ")
                    peticion = requests.put(f'http://154.38.171.54:5001/cliente/{cliente[0].get("id")}', headers= headers, data= json.dumps(cliente[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el cliente {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del cliente")


def updateClientePais(codigo):
    while True:
        if(codigo != None):
            cliente= getCli.getClienteCodigos2((codigo))
            if (cliente):
                print(tabulate(cliente, headers="keys", tablefmt="github"))
                opc=int(input("""
                    ¿Este es el cliente que desea actualizar el pais?
                            1. Si
                            2. No
                """))
                if(opc):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    cliente[0]["pais"] = input("ingrese el nuevo pais del cliente: ")
                    peticion = requests.put(f'http://154.38.171.54:5001/cliente/{cliente[0].get("id")}', headers= headers, data= json.dumps(cliente[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el cliente {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del cliente")
            

def updateClienteCodigoPostal(codigo):
    while True:
        if(codigo != None):
            cliente= getCli.getClienteCodigos2((codigo))
            if (cliente):
                print(tabulate(cliente, headers="keys", tablefmt="github"))
                opc=int(input("""
                    ¿Este es el cliente que desea actualizar el codigo postal?
                            1. Si
                            2. No
                """))
                if(opc):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    cliente[0]["codigo_postal"] = input("ingrese el nuevo codigo postal del cliente: ")
                    peticion = requests.put(f'http://154.38.171.54:5001/cliente/{cliente[0].get("id")}', headers= headers, data= json.dumps(cliente[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el cliente {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del cliente")



def updateClienteCodigoEmpVentas(codigo):
    while True:
        if(codigo != None):
            cliente= getCli.getClienteCodigos2((codigo))
            if (cliente):
                print(tabulate(cliente, headers="keys", tablefmt="github"))
                opc=int(input("""
                    ¿Este es el cliente que desea actualizar el codigo del representante de ventas?
                            1. Si
                            2. No
                """))
                if(opc):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    cliente[0]["codigo_empleado_rep_ventas"] = int(input("ingrese el nuevo codigo del representante de ventas del cliente: "))
                    peticion = requests.put(f'http://154.38.171.54:5001/cliente/{cliente[0].get("id")}', headers= headers, data= json.dumps(cliente[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el cliente {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del cliente")


def updateClienteLimiteCredito(codigo):
    while True:
        if(codigo != None):
            cliente= getCli.getClienteCodigos2((codigo))
            if (cliente):
                print(tabulate(cliente, headers="keys", tablefmt="github"))
                opc=int(input("""
                    ¿Este es el cliente que desea actualizar el limite de credito?
                            1. Si
                            2. No
                """))
                if(opc):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    cliente[0]["limite_credito"] = int(input("ingrese el nuevo limite de credito del cliente: "))
                    peticion = requests.put(f'http://154.38.171.54:5001/cliente/{cliente[0].get("id")}', headers= headers, data= json.dumps(cliente[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el cliente {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del cliente")






def menu():
  while True:
    os.system("clear")
    print("""


    ______    ___ __                _       ____                                _   __           
   / ____/___/ (_) /_____ ______   (_)___  / __/___  _________ ___  ____ ______(_)_/_/ ____      
  / __/ / __  / / __/ __ `/ ___/  / / __ \/ /_/ __ \/ ___/ __ `__ \/ __ `/ ___/ / __ \/ __ \     
 / /___/ /_/ / / /_/ /_/ / /     / / / / / __/ /_/ / /  / / / / / / /_/ / /__/ / /_/ / / / /     
/_____/\__,_/_/\__/\__,_/_/     /_/_/ /_/_/  \____/_/__/_/ /_/ /_/\__,_/\___/_/\____/_/ /_/      
  ____/ /__     / /___  _____   _____/ (_)__  ____  / /____  _____                               
 / __  / _ \   / / __ \/ ___/  / ___/ / / _ \/ __ \/ __/ _ \/ ___/                               
/ /_/ /  __/  / / /_/ (__  )  / /__/ / /  __/ / / / /_/  __(__  )                                
\__,_/\___/  /_/\____/____/   \___/_/_/\___/_/ /_/\__/\___/____/                                 
                                                                                                 
                


                                 1. Nombre del cliente
                                 2. Nombre del contacto
                                 3. Apellido del contacto
                                 4. Telefono
                                 5. Fax
                                 6. Linea direccion 1
                                 7. Linea direccion 2
                                 8. Ciudad
                                 9. Region
                                 10. Pais
                                 11. Codigo Postal
                                 12. Codigo del empleado representante de ventas del cliente 
                                 13. Limite del credito
                                 
                                 0. Salir
""")

    try:
        opcion= int(input("\nSeleccione el dato que quiera editar: "))
        codigocliente = input(("Ingrese el codigo del cliente al que deseas actualizar los datos: "))
        if (opcion == 1):
            print(tabulate(updateClienteNombre(codigocliente), headers="keys", tablefmt="github"))
        elif (opcion ==2):
            print(tabulate(updateClienteNombreContacto(codigocliente), headers="keys", tablefmt="github"))
        elif (opcion ==3):
            print(tabulate(updateClienteApellidoContacto(codigocliente), headers="keys", tablefmt="github"))
        elif (opcion ==4):
            print(tabulate(updateClienteTelefono(codigocliente), headers="keys", tablefmt="github"))
        elif (opcion ==5):
            print(tabulate(updateClienteFax(codigocliente), headers="keys", tablefmt="github"))
        elif (opcion ==6):
            print(tabulate(updateClienteLineaDireccion1(codigocliente), headers="keys", tablefmt="github"))
        elif (opcion ==7):
            print(tabulate(updateClienteLineaDireccion2(codigocliente), headers="keys", tablefmt="github"))
        elif (opcion ==8):
            print(tabulate(updateClienteCiudad(codigocliente), headers="keys", tablefmt="github"))
        elif (opcion ==9):
            print(tabulate(updateClienteRegion(codigocliente), headers="keys", tablefmt="github"))
        elif (opcion ==10):
            print(tabulate(updateClientePais(codigocliente), headers="keys", tablefmt="github"))
        elif (opcion ==11):
            print(tabulate(updateClienteCodigoPostal(codigocliente), headers="keys", tablefmt="github"))
        elif (opcion ==12):
            print(tabulate(updateClienteCodigoEmpVentas(codigocliente), headers="keys", tablefmt="github"))
        elif (opcion ==13):
            print(tabulate(updateClienteLimiteCredito(codigocliente), headers="keys", tablefmt="github"))
        elif (opcion ==0):
            break
        else:
                print("Elija algun número disponible del 0 al 13 ")
                time.sleep(3)
    except ValueError: 
         print("Caracteres incorrectos, elija una opcion del 0 al 13")
         time.sleep(3)