import json
import requests
import modules.getPago as getPag
from tabulate import tabulate
import os
import time


def updatePagoFormaPago(codigo):
    while True:
        if(codigo != None):
            pago= getPag.getPagoCodigos2((codigo))
            if (pago):
                print(tabulate(pago, headers="keys", tablefmt="github"))
                opc=int(input("""
                    ¿Este es el pago que desea actualizar la forma de ?
                            1. Si
                            2. No
                """))
                if(opc):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    pago[0]["forma_pago"] = input("ingrese la nueva forma de pago: ")
                    peticion = requests.put(f'http://154.38.171.54:5006/pagos/{pago[0].get("id")}', headers= headers, data= json.dumps(pago[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el pago {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del pago")
        

def updatePagoIdTransaccion(codigo):
    while True:
        if(codigo != None):
            pago= getPag.getPagoCodigos2((codigo))
            if (pago):
                print(tabulate(pago, headers="keys", tablefmt="github"))
                opc=int(input("""
                    ¿Este es el pago en el que desea actualizar el id de la transaccion?
                            1. Si
                            2. No
                """))
                if(opc):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    pago[0]["id_transaccion"] = input("Ingrese el nuevo id de transaccion")
                    
                    peticion = requests.put(f'http://154.38.171.54:5006/pagos/{pago[0].get("id")}', headers= headers, data= json.dumps(pago[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el pago {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del pago")


def updatePagoFecha(codigo):
    while True:
        if(codigo != None):
            pago= getPag.getPagoCodigos2((codigo))
            if (pago):
                print(tabulate(pago, headers="keys", tablefmt="github"))
                opc=int(input("""
                    ¿Este es el pago que desea actualizar la fecha de pago?
                            1. Si
                            2. No
                """))
                if(opc):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    pago[0]["fecha_pago"] = input("ingrese la nueva fecha del pago: ")
                    peticion = requests.put(f'http://154.38.171.54:5006/pagos/{pago[0].get("id")}', headers= headers, data= json.dumps(pago[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el pago {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del pago")



def updatePagoTotal(codigo):
    while True:
        if(codigo != None):
            pago= getPag.getPagoCodigos2((codigo))
            if (pago):
                print(tabulate(pago, headers="keys", tablefmt="github"))
                opc=int(input("""
                    ¿Este es el pago que desea actualizar total del pago?
                            1. Si
                            2. No
                """))
                if(opc):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    pago[0]["total"] = int(input("ingrese el nuevo total del pago: "))
                    peticion = requests.put(f'http://154.38.171.54:5006/pagos/{pago[0].get("id")}', headers= headers, data= json.dumps(pago[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el pago {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del pago")



def menu():
  while True:
    os.system("clear")
    print("""


    ______    ___ __                _       ____                                _   __           
   / ____/___/ (_) /_____ ______   (_)___  / __/___  _________ ___  ____ ______(_)_/_/ ____      
  / __/ / __  / / __/ __ `/ ___/  / / __ \/ /_/ __ \/ ___/ __ `__ \/ __ `/ ___/ / __ \/ __ \     
 / /___/ /_/ / / /_/ /_/ / /     / / / / / __/ /_/ / /  / / / / / / /_/ / /__/ / /_/ / / / /     
/_____/\__,_/_/\__/\__,_/_/     /_/_/ /_/_/  \____/_/  /_/ /_/ /_/\__,_/\___/_/\____/_/ /_/      
  ____/ /__     / /___  _____   / __ \____ _____ _____  _____                                    
 / __  / _ \   / / __ \/ ___/  / /_/ / __ `/ __ `/ __ \/ ___/                                    
/ /_/ /  __/  / / /_/ (__  )  / ____/ /_/ / /_/ / /_/ (__  )                                     
\__,_/\___/  /_/\____/____/  /_/    \__,_/\__, /\____/____/                                      
                                         /____/                                                  


                                 1. Forma de pago
                                 2. Id de la transaccion
                                 3. Fecha del pago
                                 4. Total de compra
                                 
                                 0. Salir
""")

    try:
        opcion= int(input("\nSeleccione el dato que quiera editar: "))
        codigopago = input(("Ingrese el codigo del pago al que deseas actualizar los datos: "))
        if (opcion == 1):
            print(tabulate(updatePagoFormaPago(codigopago), headers="keys", tablefmt="github"))
        elif (opcion ==2):
            print(tabulate(updatePagoIdTransaccion(codigopago), headers="keys", tablefmt="github"))
        elif (opcion ==3):
            print(tabulate(updatePagoFecha(codigopago), headers="keys", tablefmt="github"))
        elif (opcion ==4):
            print(tabulate(updatePagoTotal(codigopago), headers="keys", tablefmt="github"))
        elif (opcion ==0):
            break    
        else:
                print("Elija algun número disponible del 0 al 8 ")
                time.sleep(3)
    except ValueError: 
         print("Caracteres incorrectos, elija una opcion del 0 al 8")
         time.sleep(3)