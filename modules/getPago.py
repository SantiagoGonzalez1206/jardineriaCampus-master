import storage.pago as pag


def getFechaPago():
    clientesPagos= []
    for val in pag.pago:
        fechaPagos = val.get("fecha_pago")
        if fechaPagos.startswith("2008"):
            clientesPagos.append

    return clientesPagos

