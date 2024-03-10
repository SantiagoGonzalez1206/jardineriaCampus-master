import storage.pedido as ped
from datetime import datetime
from tabulate import tabulate 

def getEstadoPedido():
    estadosPedido = set()
    for val in ped.pedido:
       estado_pedido = val.get('estado')
       estadosPedido.add(estado_pedido)
    return estadosPedido


def getAllPedidosEntregadosAtrasados():
    pedidosEntregados=[] 
    for val in ped.pedido:
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
    for val in ped.pedido:
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
    for val in ped.pedido:
        if val.get("estado") == "Rechazado":
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


def getRechazos2009():
    pedidosRechazados2009 = []
    for val in ped.pedido:
        fechaRechazo = val.get("fecha_esperada")
        if val.get("estado") == "Rechazado" and fechaRechazo.startswith("2009"):
            pedidosRechazados2009.append(val)
    return pedidosRechazados2009


def getEntregadosEneri():
    pedidosEntregadoEnero = []
    for val in ped.pedido:
        mesEntrega = val.get("fecha_entrega")
        if val.get("estado") == "Entregado" and mesEntrega.startswith("01"):
            pedidosEntregadoEnero.append(val)
    return pedidosEntregadoEnero

def getEntregadosEnero():
    PedidosDeEnero = list()
    for val in ped.pedido:
        if (val.get("estado") == "Entregado" and val.get("fecha_entrega") != None):
            FechaEntregada = "/".join(val.get("fecha_entrega").split("-")[::-1])
            start = datetime.strptime(FechaEntregada, "%d/%m/%Y")
            if val.get("estado") == "Entregado" and start.month == 1:
                PedidosDeEnero.append(val)
    return PedidosDeEnero

def menu():
    print("""

    ____                        __                   __        __                             ___     __          
   / __ \___  ____  ____  _____/ /____  _____   ____/ /__     / /___  _____   ____  ___  ____/ (_)___/ /___  _____
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / __  / _ \   / / __ \/ ___/  / __ \/ _ \/ __  / / __  / __ \/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  __/  / / /_/ (__  )  / /_/ /  __/ /_/ / / /_/ / /_/ (__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/____/   \__,_/\___/  /_/\____/____/  / .___/\___/\__,_/_/\__,_/\____/____/  
          /_/                                                             /_/                                     

                1. Los distintos estados por los que pasa un pedido
                2. Codigo de pedido, codigo de cliente, fecha esperada y fecha de entrega de los pedidos NO entregados a tiempo
                3. Codigo de pedido, codigo de cliente, fecha esperada y fecha de entrega de los pedidos con entrega 2 dias antes de la fecha esperada
                4. Todos los pedidos rechazados en 2009
                5. Pedidos entregados en Enero de cualquier año
""")
    
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
    else:
        print("elija una opcion valida")