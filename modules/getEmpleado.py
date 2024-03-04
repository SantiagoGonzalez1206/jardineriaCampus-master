import storage.empleado as emp

def getAllEmpleadosName():
    empleadoNames = list()
    for val in emp.empleado:
        codigoNames = dict({
            "codigo_empleado": val.get('codigo_empleado'),
            "nombre_cliente": val.get('nombre')
        })
        empleadoNames.append(codigoNames)
    return empleadoNames

def getAllEmpleadosCode(codigo_jefe, nombre = None):
    empleadosZone = list()
    for val in emp.empleado:
        if val.get('codigo_jefe') == codigo_jefe :
            if (val.get('nombre') == nombre) or val.get('nombre') == None: 
                empleadosZone.append(val)

            else:
             empleadosZone.append(val)       
                
              
    return empleadosZone

def getOneEmpleadoNombreApellidos(nombre, apellido1 = None, apellido2 = None):
    empleadosZone = list()
    for val in emp.empleado:
        if val.get('nombre') == nombre :
            if (val.get('apellido1') == apellido1) or val.get('region') == None: 
                if (val.get('apellido2') == apellido2) or val.get('ciudad') == None:
        
                    empleadosZone.append(val)
    return empleadosZone


def getOneEmpleadoCodeNombre(codigo_empleado, nombre = None):
    empleadosZone = list()
    for val in emp.empleado:
        if val.get('codigo_empleado') == codigo_empleado :
            if (val.get('nombre') == nombre) or val.get('nombre') == None: 
                empleadosZone.append(val)

            else:
             empleadosZone.append(val)       
                
              
    return empleadosZone


def getOneEmpleadoExtension(puesto, nombre = None):
    empleadosZone = list()
    for val in emp.empleado:
        if val.get('puesto') == puesto :
            if (val.get('nombre') == nombre) or val.get('nombre') == None: 
                empleadosZone.append(val)

        else:
            empleadosZone.append(val)       
              
              
    return empleadosZone