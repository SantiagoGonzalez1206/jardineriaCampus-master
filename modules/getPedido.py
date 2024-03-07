import storage.pedido as ped
from datetime import datetime

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
    pedidosEntregadoEnero = []
    for val in ped.pedido:
        fecha_entrega = val.get("fecha_entrega")
        estado = val.get("estado")

        # Parsear la fecha de entrega a datetime
        fecha_entrega = datetime.strptime(fecha_entrega, "%Y-%m-%d")

        # Verificar si el pedido fue entregado en enero
        if estado == "Entregado" and fecha_entrega.month == 1:
            pedidosEntregadoEnero.append(val)

    return pedidosEntregadoEnero
