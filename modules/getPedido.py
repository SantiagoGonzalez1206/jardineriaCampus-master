from tabulate import tabulate 
import time
from datetime import datetime, timedelta
import requests


def getAllPedido():
    # json-server storage/pedido.json -b 5506
    peticion = requests.get("http://154.38.171.54:5007/pedidos")
    data = peticion.json()
    return data


def getPedidoId(id):
    peticion = requests.get(f"http://154.38.171.54:5007/pedidos/{id}")
    return[peticion.json()] if peticion.ok else []


def getPedidoCodigos2(codigo):
    peticion = requests.get(f"http://154.38.171.54:5007/pedidos?codigo_pedido={codigo.upper()}")
    data = peticion.json()
    if(data)== 0:
        data=None
    return data


def getCodeByCode(codigo):
        AllproductsProducts=[]
        for val in getAllPedido():
                if val.get("codigo_pedido")==codigo:
                        return [val]



def getEstadoPedido():
    estadosPedido = set()
    for val in getAllPedido():
       estado_pedido = val.get('estado')
       estadosPedido.add(estado_pedido)
    return estadosPedido


def getAllPedidosEntregadosAtrasados():
    pedidosEntregados=[] 
    for val in getAllPedido():
        if val.get("estado") == "Entregado" and val.get("fecha_entrega")is None:
            val["fecha_entrega"] = val.get("fecha_esperada")
        if val.get("estado") == "Entregado":
            date1= "/".join(val.get("fecha_entrega").split("-")[::-1])
            date2= "/".join(val.get("fecha_esperada").split("-")[::-1])
            start = datetime.strptime(date1, "%d/%m/%Y")
            end = datetime.strptime(date2, "%d/%m/%Y")
            diff= end.date() - start.date()
            if(diff.days < 0):
                pedidosEntregados.append({
                    "codigo_de_pedido": val.get ("codigo_pedido"),
                    "codigo_de_cliente": val.get ("codigo_cliente"),
                    "fecha_esperada": val.get ("fecha_esperada"),
                    "fecha_de_entrega": val.get ("fecha_entrega")
                })

    return pedidosEntregados

def getPedidosDosDias():
    pedidosEntregados=[] 
    for val in getAllPedido():
        if val.get("estado") == "Entregado" and val.get("fecha_entrega")is None:
            val["fecha_entrega"] = val.get("fecha_esperada")
        if val.get("estado") == "Entregado":
            date1= "/".join(val.get("fecha_entrega").split("-")[::-1])
            date2= "/".join(val.get("fecha_esperada").split("-")[::-1])
            start = datetime.strptime(date1, "%d/%m/%Y")
            end = datetime.strptime(date2, "%d/%m/%Y")
            diff= end.date() - start.date()
            if(diff.days == 2):
                pedidosEntregados.append({
                    "codigo_de_pedido": val.get ("codigo_pedido"),
                    "codigo_de_cliente": val.get ("codigo_cliente"),
                    "fecha_esperada": val.get ("fecha_esperada"),
                    "fecha_de_entrega": val.get ("fecha_entrega")
                })

    return pedidosEntregados


def getPedidosDosDias():
    pedidosEntregados=[] 
    for pedido in getAllPedido():
        
        fechaEntregaInicial=(pedido.get("fecha_entrega"))
        fechaEsperadaInicial=(pedido.get("fecha_esperada"))

        if fechaEntregaInicial is not None and fechaEsperadaInicial is not None:
            fechaEntrega= datetime.strptime(fechaEntregaInicial, "%Y-%m-%d")
            fechaEsperada= datetime.strptime(fechaEsperadaInicial, "%Y-%m-%d")

            diferenciaDias=(fechaEsperada-fechaEntrega)

            dos_dias = timedelta(days=2)

            if diferenciaDias == dos_dias:
                pedidosEntregados.append(
                {
                    "codigoPedido": pedido.get("codigo_pedido"),
                    "codigoCliente": pedido.get("codigo_cliente"),
                    "fechaEsperada": pedido.get("fecha_esperada"),
                    "fechaEntrega": pedido.get("fecha_entrega")
                }
                )

    return pedidosEntregados


def getRechazos2009():
    pedidosRechazados2009 = []
    for val in getAllPedido():
        fechaRechazo = val.get("fecha_esperada")
        if val.get("estado") == "Rechazado" and fechaRechazo.startswith("2009"):
            pedidosRechazados2009.append(val)
    return pedidosRechazados2009


def getEntregadosEneri():
    pedidosEntregadoEnero = []
    for val in getAllPedido():
        mesEntrega = val.get("fecha_entrega")
        if val.get("estado") == "Entregado" and mesEntrega.startswith("01"):
            pedidosEntregadoEnero.append(val)
    return pedidosEntregadoEnero

def getEntregadosEnero():
    PedidosDeEnero = list()
    for val in getAllPedido():
        if (val.get("estado") == "Entregado" and val.get("fecha_entrega") != None):
            FechaEntregada = "/".join(val.get("fecha_entrega").split("-")[::-1])
            start = datetime.strptime(FechaEntregada, "%d/%m/%Y")
            if val.get("estado") == "Entregado" and start.month == 1:
                PedidosDeEnero.append(val)
    return PedidosDeEnero

def menu():
    while True:
        print("""

    ____                        __                   __        __                             ___     __          
   / __ \___  ____  ____  _____/ /____  _____   ____/ /__     / /___  _____   ____  ___  ____/ (_)___/ /___  _____
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / __  / _ \   / / __ \/ ___/  / __ \/ _ \/ __  / / __  / __ \/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  __/  / / /_/ (__  )  / /_/ /  __/ /_/ / / /_/ / /_/ (__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/____/   \__,_/\___/  /_/\____/____/  / .___/\___/\__,_/_/\__,_/\____/____/  
          /_/                                                             /_/                                     

        1. Los distintos estados por los que pasa un pedido
        2. Codigo de pedido, codigo de cliente, fecha esperada y fecha de entrega de los pedidos NO entregados a tiempo
        3. Codigo de pedido, codigo de cliente, fecha esperada y fecha de entrega de los pedidos con entrega 2 dias antes
        4. Todos los pedidos rechazados en 2009
        5. Pedidos entregados en Enero de cualquier año
        0. Salir
""")
        try:
            opcion= int(input("\nSeleccione una de las opciones: "))
            if(opcion == 1):
                print(tabulate(getEstadoPedido(), headers="keys", tablefmt="github"))
            elif(opcion == 2):
                print(tabulate(getAllPedidosEntregadosAtrasados(), headers="keys", tablefmt="github"))
            elif(opcion == 3):
                print(tabulate(getPedidosDosDias(), headers="keys", tablefmt="github"))
            elif(opcion == 4):
                print(tabulate(getRechazos2009(), headers="keys", tablefmt="github"))    
            elif(opcion == 5):
                print(tabulate(getEntregadosEnero(), headers="keys", tablefmt="github"))
            elif(opcion == 0):
                break
            else:
                print("elija una opcion valida")
        except ValueError: 
            print("Caracteres incorrectos, elija una opcion del 0 al 5")
            time.sleep(3)