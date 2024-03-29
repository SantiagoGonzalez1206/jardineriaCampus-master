import json
import requests
import modules.getPedido as getPed
from tabulate import tabulate
import os
import time


def updatePedidoFecha(codigo):
    while True:
        if(codigo != None):
            pedido= getPed.getPedidoCodigos2((codigo))
            if (pedido):
                print(tabulate(pedido, headers="keys", tablefmt="github"))
                opc=int(input("""
                    ¿Esta es elpedido que desea actualizar la fecha?
                            1. Si
                            2. No
                """))
                if(opc):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    pedido[0]["fecha_pedido"] = input("ingrese la nueva fecha esperada del pedido: ")
                    peticion = requests.put(f'http://154.38.171.54:5007/pedidos/{pedido[0].get("id")}', headers= headers, data= json.dumps(pedido[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del pedido")
        

def updatePedidoFechaEsperada(codigo):
    while True:
        if(codigo != None):
            pedido= getPed.getPedidoCodigos2((codigo))
            if (pedido):
                print(tabulate(pedido, headers="keys", tablefmt="github"))
                opc=int(input("""
                    ¿Esta es el en el que desea actualizar la fecha esperada?
                            1. Si
                            2. No
                """))
                if(opc):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    pedido[0]["fecha_esperada"] = input("ingrese la nueva fecha esperada del pedido")
                    
                    peticion = requests.put(f'http://154.38.171.54:5007/pedidos/{pedido[0].get("id")}', headers= headers, data= json.dumps(pedido[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del pedido")


def updatePedidoFechaEntrega(codigo):
    while True:
        if(codigo != None):
            pedido= getPed.getPedidoCodigos2((codigo))
            if (pedido):
                print(tabulate(pedido, headers="keys", tablefmt="github"))
                opc=int(input("""
                    ¿Esta es el que desea actualizar la fecha de entrega?
                            1. Si
                            2. No
                """))
                if(opc):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    pedido[0]["fecha_entrega"] = input("ingrese la nueva fecha de entrega del pedido: ")
                    peticion = requests.put(f'http://154.38.171.54:5007/pedidos/{pedido[0].get("id")}', headers= headers, data= json.dumps(pedido[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del pedido")



def updatePedidoEstado(codigo):
    while True:
        if(codigo != None):
            pedido= getPed.getPedidoCodigos2((codigo))
            if (pedido):
                print(tabulate(pedido, headers="keys", tablefmt="github"))
                opc=int(input("""
                    ¿Esta es el que desea actualizar el estado?
                            1. Si
                            2. No
                """))
                if(opc):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    pedido[0]["estado"] = input("ingrese el nuevo estado del pedido: ")
                    peticion = requests.put(f'http://154.38.171.54:5007/pedidos/{pedido[0].get("id")}', headers= headers, data= json.dumps(pedido[0]))
                    data = peticion.json()
                    print(data)
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del pedido")


def updatePedidoComentario(codigo):
    while True:
        if(codigo != None):
            pedido= getPed.getPedidoCodigos2((codigo))
            if (pedido):
                print(tabulate(pedido, headers="keys", tablefmt="github"))
                opc=int(input("""
                    ¿Esta es el que desea actualizar el comentario?
                            1. Si
                            2. No
                """))
                if(opc):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    pedido[0]["comentario"] = input("ingrese el nuevo comentario del pedido: ")
                    peticion = requests.put(f'http://154.38.171.54:5007/pedidos/{pedido[0].get("id")}', headers= headers, data= json.dumps(pedido[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del pedido")


def updatePedidoCodigoCliente(codigo):
    while True:
        if(codigo != None):
            pedido= getPed.getPedidoCodigos2((codigo))
            if (pedido):
                print(tabulate(pedido, headers="keys", tablefmt="github"))
                opc=int(input("""
                    ¿Esta es el que desea actualizar el codigo del cliente?
                            1. Si
                            2. No
                """))
                if(opc):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    pedido[0]["codigo_cliente"] = int(input("ingrese el nuevo codigo del cliente del pedido: "))
                    peticion = requests.put(f'http://154.38.171.54:5007/pedidos/{pedido[0].get("id")}', headers= headers, data= json.dumps(pedido[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del pedido")




def menu():
  while True:
    #os.system("clear")
    print("""



    ______    ___ __                _       ____                                _   __           
   / ____/___/ (_) /_____ ______   (_)___  / __/___  _________ ___  ____ ______(_)_/_/ ____      
  / __/ / __  / / __/ __ `/ ___/  / / __ \/ /_/ __ \/ ___/ __ `__ \/ __ `/ ___/ / __ \/ __ \     
 / /___/ /_/ / / /_/ /_/ / /     / / / / / __/ /_/ / /  / / / / / / /_/ / /__/ / /_/ / / / /     
/_____/\__,_/_/\__/\__,_/_/     /_/_/ /_/_/  \____/_/  /_/ /_/ /_/\__,_/\___/_/\____/_/ /_/      
  ____/ /__     / /___ ______   / __ \___  ____/ (_)___/ /___  _____                             
 / __  / _ \   / / __ `/ ___/  / /_/ / _ \/ __  / / __  / __ \/ ___/                             
/ /_/ /  __/  / / /_/ (__  )  / ____/  __/ /_/ / / /_/ / /_/ (__  )                              
\__,_/\___/  /_/\__,_/____/  /_/    \___/\__,_/_/\__,_/\____/____/                               
                                                                                                 



                                 1. Fecha del pedido
                                 2. Fecha esperada del pedido
                                 3. Fecha de entrega del pedido
                                 4. Estado del pedido
                                 5. Comentario del pedido
                                 6. Codigo del cliente del pedido
                                 
                                 0. Salir
""")

    try:
        opcion= int(input("\nSeleccione el dato que quiera editar: "))
        codigopedido = input(("Ingrese el codigo del pedido al que deseas actualizar los datos: "))
        if (opcion == 1):
                print(tabulate(updatePedidoFecha(codigopedido), headers="keys", tablefmt="github"))
        elif (opcion ==2):
                print(tabulate(updatePedidoFechaEsperada(codigopedido), headers="keys", tablefmt="github"))
        elif (opcion ==3):
                print(tabulate(updatePedidoFechaEntrega(codigopedido), headers="keys", tablefmt="github"))
        elif (opcion ==4):
                print(tabulate(updatePedidoEstado(codigopedido), headers="keys", tablefmt="github"))
        elif (opcion ==5):
                print(tabulate(updatePedidoComentario(codigopedido), headers="keys", tablefmt="github"))
        elif (opcion ==6):
                print(tabulate(updatePedidoCodigoCliente(codigopedido), headers="keys", tablefmt="github"))
        elif (opcion ==0):
                break    
        else:
                    print("Elija algun número disponible del 0 al 6 ")
                    time.sleep(3)
    except ValueError:
        print("Seleccione una opcion valida del 0 al 6")
        time.sleep(3)
