import storage.pago as pag
from tabulate import tabulate 

def getFechaPago():
    clientesPagos= set()
    for val in pag.pago:
        fechaPagos = val.get("fecha_pago")
        if fechaPagos.startswith("2008"):
            clientesPagos.add(val.get("codigo_cliente"))

    return clientesPagos


def getPagoPaypal():
    pagoFecha = []
    for val in pag.pago:
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
    for val in pag.pago:
        FormaPago = val.get("forma_pago")
        if FormaPago not in Paypal:
            Paypal.add (FormaPago)
    return Paypal


def menu():
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
""")
    
    opcion= int(input("\nSeleccione una de las opciones: "))
    if(opcion == 1):
        print(getFechaPago())
    elif(opcion == 2):
        print(tabulate(getPagoPaypal(), headers="keys", tablefmt="github"))
    elif (opcion == 3):
        print(getFormaDePago())
    else:
        print("elija una opcion valida")