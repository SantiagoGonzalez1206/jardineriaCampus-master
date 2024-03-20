import json
import requests
import modules.getEmpleado as getEmp
from tabulate import tabulate
import os
import time


def updateEmpleadoNombre(codigo):
    while True:
        if(codigo != None):
            empleado= getEmp.getEmpleadoCodigos2((codigo))
            if (empleado):
                print(tabulate(empleado, headers="keys", tablefmt="github"))
                opc=int(input("""
                    ¿Este es el empleado que desea actualizar el nombre?
                            1. Si
                            2. No
                """))
                if(opc):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    empleado[0]["nombre"] = input("ingrese el nuevo nombre del empleado: ")
                    peticion = requests.put(f'http://154.38.171.54:5003/empleados/{empleado[0].get("id")}', headers= headers, data= json.dumps(empleado[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el empleado {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del empleado")
        

def updateEmpleadoApellido1(codigo):
    while True:
        if(codigo != None):
            empleado= getEmp.getEmpleadoCodigos2((codigo))
            if (empleado):
                print(tabulate(empleado, headers="keys", tablefmt="github"))
                opc=int(input("""
                    ¿Este es el empleado en el que desea actualizar el apellido 1?
                            1. Si
                            2. No
                """))
                if(opc):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    empleado[0]["apellido1"] = input("Ingrese el nuevo apellido 1 del empleado")
                    
                    peticion = requests.put(f'http://154.38.171.54:5003/empleados/{empleado[0].get("id")}', headers= headers, data= json.dumps(empleado[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el empleado {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del empleado")


def updateEmpleadoApellido2(codigo):
    while True:
        if(codigo != None):
            empleado= getEmp.getEmpleadoCodigos2((codigo))
            if (empleado):
                print(tabulate(empleado, headers="keys", tablefmt="github"))
                opc=int(input("""
                    ¿Este es el empleado que desea actualizar el apellido 2?
                            1. Si
                            2. No
                """))
                if(opc):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    empleado[0]["apellido2"] = input("ingrese el nuevo apellido 2 del empleado: ")
                    peticion = requests.put(f'http://154.38.171.54:5003/empleados/{empleado[0].get("id")}', headers= headers, data= json.dumps(empleado[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el empleado {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del empleado")



def updateEmpleadoExtension(codigo):
    while True:
        if(codigo != None):
            empleado= getEmp.getEmpleadoCodigos2((codigo))
            if (empleado):
                print(tabulate(empleado, headers="keys", tablefmt="github"))
                opc=int(input("""
                    ¿Este es el empleado que desea actualizar la extension?
                            1. Si
                            2. No
                """))
                if(opc):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    empleado[0]["extension"] = input("ingrese la nueva extension del empleado: ")
                    peticion = requests.put(f'http://154.38.171.54:5003/empleados/{empleado[0].get("id")}', headers= headers, data= json.dumps(empleado[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el empleado {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del empleado")


def updateEmpleadoEmail(codigo):
    while True:
        if(codigo != None):
            empleado= getEmp.getEmpleadoCodigos2((codigo))
            if (empleado):
                print(tabulate(empleado, headers="keys", tablefmt="github"))
                opc=int(input("""
                    ¿Este es el empleado que desea actualizar el email?
                            1. Si
                            2. No
                """))
                if(opc):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    empleado[0]["email"] = input("ingrese el nuevo email del empleado: ")
                    peticion = requests.put(f'http://154.38.171.54:5003/empleados/{empleado[0].get("id")}', headers= headers, data= json.dumps(empleado[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el empleado {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del empleado")


def updateEmpleadoCodigoOficina(codigo):
    while True:
        if(codigo != None):
            empleado= getEmp.getEmpleadoCodigos2((codigo))
            if (empleado):
                print(tabulate(empleado, headers="keys", tablefmt="github"))
                opc=int(input("""
                    ¿Este es el empleado que desea actualizar el codigo de oficina?
                            1. Si
                            2. No
                """))
                if(opc):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    empleado[0]["codigo_oficina"] = input("ingrese el nuevo codigo de oficina: ")
                    peticion = requests.put(f'http://154.38.171.54:5003/empleados/{empleado[0].get("id")}', headers= headers, data= json.dumps(empleado[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el empleado {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del empleado")


def updateEmpleadoCodigoJefe(codigo):
    while True:
        if(codigo != None):
            empleado= getEmp.getEmpleadoCodigos2((codigo))
            if (empleado):
                print(tabulate(empleado, headers="keys", tablefmt="github"))
                opc=int(input("""
                    ¿Este es el empleado que desea actualizar el codigo de jefe?
                            1. Si
                            2. No
                """))
                if(opc):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    empleado[0]["codigo_jefe"] = int(input("ingrese el nuevo codigo de jefe: "))
                    peticion = requests.put(f'http://154.38.171.54:5003/empleados/{empleado[0].get("id")}', headers= headers, data= json.dumps(empleado[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el empleado {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del empleado")


def updateEmpleadoPuesto(codigo):
    while True:
        if(codigo != None):
            empleado= getEmp.getEmpleadoCodigos2((codigo))
            if (empleado):
                print(tabulate(empleado, headers="keys", tablefmt="github"))
                opc=int(input("""
                    ¿Este es el empleado que desea actualizar el puesto?
                            1. Si
                            2. No
                """))
                if(opc):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    empleado[0]["puesto"] = input("ingrese el nuevo puesto del empleado: ")
                    peticion = requests.put(f'http://154.38.171.54:5003/empleados/{empleado[0].get("id")}', headers= headers, data= json.dumps(empleado[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el empleado {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del empleado")





def menu():
  while True:
    os.system("clear")
    print("""


    ______    ___ __                _       ____                                _   __           
   / ____/___/ (_) /_____ ______   (_)___  / __/___  _________ ___  ____ ______(_)_/_/ ____      
  / __/ / __  / / __/ __ `/ ___/  / / __ \/ /_/ __ \/ ___/ __ `__ \/ __ `/ ___/ / __ \/ __ \     
 / /___/ /_/ / / /_/ /_/ / /     / / / / / __/ /_/ / /  / / / / / / /_/ / /__/ / /_/ / / / /     
/_____/\__,_/_/\__/\__,_/_/     /_/_/_/_/_/  \____/_/  /_/ /_/ /_/\__,_/\___/_/\____/_/ /_/      
  ____/ /__     / /___  _____   / ____/___ ___  ____  / /__  ____ _____/ /___  _____             
 / __  / _ \   / / __ \/ ___/  / __/ / __ `__ \/ __ \/ / _ \/ __ `/ __  / __ \/ ___/             
/ /_/ /  __/  / / /_/ (__  )  / /___/ / / / / / /_/ / /  __/ /_/ / /_/ / /_/ (__  )              
\__,_/\___/  /_/\____/____/  /_____/_/ /_/ /_/ .___/_/\___/\__,_/\__,_/\____/____/               
                                            /_/                                                  


                                 1. Nombre del empleado
                                 2. Apellido 1 del empleado
                                 3. Apellido 2 del empleado
                                 4. Extension del empleado
                                 5. Email del empleado
                                 6. Codigo de oficina del empleado
                                 7. Codigo de jefe del empleado
                                 8. Puesto del empleado
                                 
                                 0. Salir
""")

    try:
        opcion= int(input("\nSeleccione el dato que quiera editar: "))
        codigoempleado = input(("Ingrese el codigo del empleado al que deseas actualizar los datos: "))
        if (opcion == 1):
            print(tabulate(updateEmpleadoNombre(codigoempleado), headers="keys", tablefmt="github"))
        elif (opcion ==2):
            print(tabulate(updateEmpleadoApellido1(codigoempleado), headers="keys", tablefmt="github"))
        elif (opcion ==3):
            print(tabulate(updateEmpleadoApellido2(codigoempleado), headers="keys", tablefmt="github"))
        elif (opcion ==4):
            print(tabulate(updateEmpleadoExtension(codigoempleado), headers="keys", tablefmt="github"))
        elif (opcion ==5):
            print(tabulate(updateEmpleadoEmail(codigoempleado), headers="keys", tablefmt="github"))
        elif (opcion ==6):
            print(tabulate(updateEmpleadoCodigoOficina(codigoempleado), headers="keys", tablefmt="github"))
        elif (opcion ==7):
            print(tabulate(updateEmpleadoCodigoJefe(codigoempleado), headers="keys", tablefmt="github"))
        elif (opcion ==8):
            print(tabulate(updateEmpleadoPuesto(codigoempleado), headers="keys", tablefmt="github"))
        elif (opcion ==0):
            break    
        else:
                print("Elija algun número disponible del 0 al 8 ")
                time.sleep(3)
    except ValueError: 
         print("Caracteres incorrectos, elija una opcion del 0 al 8")
         time.sleep(3)