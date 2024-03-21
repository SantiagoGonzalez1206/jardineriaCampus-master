import json
import requests
import modules.getOficina as getOfi
from tabulate import tabulate
import os
import time


def updateOficinaCiudad(codigo):
    while True:
        if(codigo != None):
            oficina= getOfi.getOficinaCodigos2((codigo))
            if (oficina):
                print(tabulate(oficina, headers="keys", tablefmt="github"))
                opc=int(input("""
                    ¿Esta es la oficina que desea actualizar la ciudad?
                            1. Si
                            2. No
                """))
                if(opc):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    oficina[0]["ciudad"] = input("ingrese la nueva ciudad de la oficina: ")
                    peticion = requests.put(f'http://154.38.171.54:5005/oficinas/{oficina[0].get("id")}', headers= headers, data= json.dumps(oficina[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"la oficina {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo de la oficina")
        

def updateOficinaPais(codigo):
    while True:
        if(codigo != None):
            oficina= getOfi.getOficinaCodigos2((codigo))
            if (oficina):
                print(tabulate(oficina, headers="keys", tablefmt="github"))
                opc=int(input("""
                    ¿Esta es la oficina en el que desea actualizar el pais?
                            1. Si
                            2. No
                """))
                if(opc):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    oficina[0]["pais"] = input("Ingrese el nuevo pais de la oficina")
                    
                    peticion = requests.put(f'http://154.38.171.54:5005/oficinas/{oficina[0].get("id")}', headers= headers, data= json.dumps(oficina[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"la oficina {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo de la oficina")


def updateOficinaRegion(codigo):
    while True:
        if(codigo != None):
            oficina= getOfi.getOficinaCodigos2((codigo))
            if (oficina):
                print(tabulate(oficina, headers="keys", tablefmt="github"))
                opc=int(input("""
                    ¿Esta es la oficina que desea actualizar la region?
                            1. Si
                            2. No
                """))
                if(opc):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    oficina[0]["region"] = input("ingrese la nueva region de la oficina: ")
                    peticion = requests.put(f'http://154.38.171.54:5005/oficinas/{oficina[0].get("id")}', headers= headers, data= json.dumps(oficina[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"la oficina {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo de la oficina")



def updateOficinaCodigoPostal(codigo):
    while True:
        if(codigo != None):
            oficina= getOfi.getOficinaCodigos2((codigo))
            if (oficina):
                print(tabulate(oficina, headers="keys", tablefmt="github"))
                opc=int(input("""
                    ¿Esta es la oficina que desea actualizar el codigo postal?
                            1. Si
                            2. No
                """))
                if(opc):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    oficina[0]["codigo_postal"] = input("ingrese el nuevo codigo postal de la oficina: ")
                    peticion = requests.put(f'http://154.38.171.54:5005/oficinas/{oficina[0].get("id")}', headers= headers, data= json.dumps(oficina[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"la oficina {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo de la oficina")


def updateOficinaTelefono(codigo):
    while True:
        if(codigo != None):
            oficina= getOfi.getOficinaCodigos2((codigo))
            if (oficina):
                print(tabulate(oficina, headers="keys", tablefmt="github"))
                opc=int(input("""
                    ¿Esta es la oficina que desea actualizar el telefono?
                            1. Si
                            2. No
                """))
                if(opc):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    oficina[0]["telefono"] = input("ingrese el nuevo telefono de la oficina: ")
                    peticion = requests.put(f'http://154.38.171.54:5005/oficinas/{oficina[0].get("id")}', headers= headers, data= json.dumps(oficina[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"la oficina {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo de la oficina")


def updateOficinaLineaDireccion1(codigo):
    while True:
        if(codigo != None):
            oficina= getOfi.getOficinaCodigos2((codigo))
            if (oficina):
                print(tabulate(oficina, headers="keys", tablefmt="github"))
                opc=int(input("""
                    ¿Esta es la oficina que desea actualizar la linea de direccion 1?
                            1. Si
                            2. No
                """))
                if(opc):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    oficina[0]["linea_direccion1"] = input("ingrese la nueva linea de direccion 1 de la oficina: ")
                    peticion = requests.put(f'http://154.38.171.54:5005/oficinas/{oficina[0].get("id")}', headers= headers, data= json.dumps(oficina[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"la oficina {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo de la oficina")


def updateOficinaLineaDireccion2(codigo):
    while True:
        if(codigo != None):
            oficina= getOfi.getOficinaCodigos2((codigo))
            if (oficina):
                print(tabulate(oficina, headers="keys", tablefmt="github"))
                opc=int(input("""
                    ¿Esta es la oficina que desea actualizar la linea de direccion 2?
                            1. Si
                            2. No
                """))
                if(opc):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    oficina[0]["linea_direccion2"] = input("ingrese la nueva linea de direccion 2: ")
                    peticion = requests.put(f'http://154.38.171.54:5005/oficinas/{oficina[0].get("id")}', headers= headers, data= json.dumps(oficina[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"la oficina {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo de la oficina")



def menu():
  while True:
    os.system("clear")
    print("""


    ______    ___ __                _       ____                                _   __           
   / ____/___/ (_) /_____ ______   (_)___  / __/___  _________ ___  ____ ______(_)_/_/ ____      
  / __/ / __  / / __/ __ `/ ___/  / / __ \/ /_/ __ \/ ___/ __ `__ \/ __ `/ ___/ / __ \/ __ \     
 / /___/ /_/ / / /_/ /_/ / /     / / / / / __/ /_/ / /  / / / / / / /_/ / /__/ / /_/ / / / /     
/_____/\__,_/_/\__/\__,_/_/     /_/_/ /_/_/_ \____/_/  /_/ /_/ /_/\__,_/\___/_/\____/_/ /_/      
  ____/ /__     / /___ ______   / __ \/ __(_)____(_)___  ____ ______                             
 / __  / _ \   / / __ `/ ___/  / / / / /_/ / ___/ / __ \/ __ `/ ___/                             
/ /_/ /  __/  / / /_/ (__  )  / /_/ / __/ / /__/ / / / / /_/ (__  )                              
\__,_/\___/  /_/\__,_/____/   \____/_/ /_/\___/_/_/ /_/\__,_/____/                               
                                                                                                 
                                  


                                 1. Ciudad de la Oficina
                                 2. Pais de la oficina
                                 3. Region de la oficina
                                 4. Codigo postal de la oficina
                                 5. Telefono de la oficina
                                 6. Linea de direccion 1 de la oficina
                                 7. Linea de direccion 2 de la oficina
                                 
                                 0. Salir
""")

    try:
        opcion= int(input("\nSeleccione el dato que quiera editar: "))
        codigooficina = input(("Ingrese el codigo de la oficina al que deseas actualizar los datos: "))
        if (opcion == 1):
            print(tabulate(updateOficinaCiudad(codigooficina), headers="keys", tablefmt="github"))
        elif (opcion ==2):
            print(tabulate(updateOficinaPais(codigooficina), headers="keys", tablefmt="github"))
        elif (opcion ==3):
            print(tabulate(updateOficinaRegion(codigooficina), headers="keys", tablefmt="github"))
        elif (opcion ==4):
            print(tabulate(updateOficinaCodigoPostal(codigooficina), headers="keys", tablefmt="github"))
        elif (opcion ==5):
            print(tabulate(updateOficinaTelefono(codigooficina), headers="keys", tablefmt="github"))
        elif (opcion ==6):
            print(tabulate(updateOficinaLineaDireccion1(codigooficina), headers="keys", tablefmt="github"))
        elif (opcion ==7):
            print(tabulate(updateOficinaLineaDireccion2(codigooficina), headers="keys", tablefmt="github"))
        elif (opcion ==0):
            break    
        else:
                print("Elija algun número disponible del 0 al 7 ")
                time.sleep(3)
    except ValueError: 
         print("Caracteres incorrectos, elija una opcion del 0 al 7")
         time.sleep(3)
