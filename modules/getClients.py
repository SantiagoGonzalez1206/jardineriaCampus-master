import storage.cliente as cli

def getAllClientesName():
    clienteNames = list()
    for val in cli.clientes:
        codigoNames = dict({
            "codigo_cliente": val.get('codigo_cliente'),
            "nombre_cliente": val.get('nombre_cliente')
        })
        clienteNames.append(codigoNames)
    return clienteNames

def getOneClientCodigo(codigo):
    for val in cli.clientes:
            if (val.get('codigo_cliente') == codigo):
                return {
                    "codigo_cliente": val.get('codigo_cliente'),
                    "nombre_cliente": val.get('nombre_cliente')
        }

def getAllClientCreditCiudad(limiteCredit, ciudad):
    clienteCredit = list()
    for val in cli.clientes:
        if(val.get('limite_credito') >= limiteCredit and val.get('ciudad') == ciudad):
            clienteCredit.append(val)
    return clienteCredit

def getAllClientPaisRegionCiudad(pais, region=None, ciudad=None):
    clientZone = list()
    for val in cli.clientes:
        if(
            val.get('pais') == pais and 
            (val.get('region') == region or val.get('region') == None) or 
            (val.get('ciudad') == ciudad or val.get('ciudad') == None)
        ):
        
            clientZone.append(val)
    return clientZone