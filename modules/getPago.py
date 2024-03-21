import requests
import time
from tabulate import tabulate 

def getAllPago():
    # json-server storage/pago.json -b 5505
    peticion = requests.get("http://154.38.171.54:5006/pagos")
    data = peticion.json()
    return data

def getPagoId(id):
    peticion = requests.get(f"http://154.38.171.54:5006/pagos/{id}")
    return[peticion.json()] if peticion.ok else []


def getPagoCodigos2(codigo):
    peticion = requests.get(f"http://154.38.171.54:5006/pagos?codigo_cliente={codigo.upper()}")
    data = peticion.json()
    if(data)== 0:
        data=None
    return data


def getAllIdTransactions(id):
    transaction=[]
    for val in getAllPago():
         if val.get("id_transaccion")==id:
            return [val]


def getFechaPago():
    clientesPagos= set()
    for val in getAllPago():
        fechaPagos = val.get("fecha_pago")
        if fechaPagos.startswith("2008"):
            clientesPagos.add(val.get("codigo_cliente"))

    return clientesPagos


def getPagoPaypal():
    pagoFecha = []
    for val in getAllPago():
        if("2008") in val.get("fecha_pago") and val.get("forma_pago") == ("PayPal"):
            pagoFecha.append({
                    "codigo_de_cliente": val.get("codigo_cliente"),
                    "fecha_pago": val.get("fecha_pago"),
                    "forma_pago": val.get("forma_pago"),
                    "total": val.get("total")
                })
    pagoFecha = sorted(pagoFecha, key=lambda x: x ["total"], reverse=True)

    return pagoFecha

def getFormaDePago():
    Paypal = set ()
    for val in getAllPago():
        FormaPago = val.get("forma_pago")
        if FormaPago not in Paypal:
            Paypal.add (FormaPago)
    return Paypal


def menu():
    while True:
        print("""

    ____                        __                   __        __                                          
   / __ \___  ____  ____  _____/ /____  _____   ____/ /__     / /___  _____   ____  ____ _____ _____  _____
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / __  / _ \   / / __ \/ ___/  / __ \/ __ `/ __ `/ __ \/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  __/  / / /_/ (__  )  / /_/ / /_/ / /_/ / /_/ (__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/____/   \__,_/\___/  /_/\____/____/  / .___/\__,_/\__, /\____/____/  
          /_/                                                             /_/          /____/              


                                 1. Codigo de cliente con algun pago en 2008
                                 2. Todos los pagos hechos en 2008 con Paypal (De mayor a menor)
                                 3. Todas las formas de pago (sin repetirse)
                                 0. Salir 
""")
        try:
            opcion= int(input("\nSeleccione una de las opciones: "))
            if(opcion == 1):
                print(getFechaPago())
            elif(opcion == 2):
                print(tabulate(getPagoPaypal(), headers="keys", tablefmt="github"))
            elif (opcion == 3):
                print(getFormaDePago())
            elif (opcion == 0):
                break
            else:
                print("elija una opcion valida")
        except ValueError: 
                print("Caracteres incorrectos, elija una opcion del 0 al 3")
                time.sleep(3)