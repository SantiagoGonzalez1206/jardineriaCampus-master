import storage.pago as pag


def getFechaPago():
    clientesPagos= set()
    for val in pag.pago:
        fechaPagos = val.get("fecha_pago")
        if fechaPagos.startswith("2008"):
            clientesPagos.add(val.get("codigo_cliente"))

    return clientesPagos

