import storage.cliente as cli

def getAllEmpleadosName():
    empleadoNames = list()
    for val in cli.clientes:
        codigoNames = dict({
            "codigo_empleado": val.get('codigo_empleado'),
            "nombre_cliente": val.get('nombre')
        })
        empleadoNames.append(codigoNames)
    return empleadoNames