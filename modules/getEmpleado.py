from tabulate import tabulate
import requests


def getAllEmpleado():
    # json-server storage/empleado.json -b 5504
    peticion = requests.get("http://154.38.171.54:5003/empleados")
    data = peticion.json()
    return data

def getEmpleadoId(id):
    peticion = requests.get(f"http://154.38.171.54:5003/empleados/{id}")
    return[peticion.json()] if peticion.ok else []


def getEmpleadoCodigos2(codigo):
    peticion = requests.get(f"http://154.38.171.54:5003/empleados?codigo_empleado={codigo.upper()}")
    data = peticion.json()
    if(data)== 0:
        data=None
    return data


def getAllEmpleadosName():
    empleadoNames = list()
    for val in getAllEmpleado():
        codigoNames = dict({
            "codigo_empleado": val.get('codigo_empleado'),
            "nombre_cliente": val.get('nombre')
        })
        empleadoNames.append(codigoNames)
    return empleadoNames

def getAllEmpleadosCode(codigo_jefe, nombre = None):
    empleadosZone = list()
    for val in getAllEmpleado():
        if val.get('codigo_jefe') == codigo_jefe :
            if (val.get('nombre') == nombre) or val.get('nombre') == None: 
                empleadosZone.append(val)

            else:
             empleadosZone.append(val)       
                
              
    return empleadosZone

def getOneEmpleadoNombreApellidos(nombre, apellido1 = None, apellido2 = None):
    empleadosZone = list()
    for val in getAllEmpleado():
        if val.get('nombre') == nombre :
            if (val.get('apellido1') == apellido1) or val.get('region') == None: 
                if (val.get('apellido2') == apellido2) or val.get('ciudad') == None:
        
                    empleadosZone.append(val)
    return empleadosZone


def getOneEmpleadoCodeNombre(codigo_empleado, nombre = None):
    empleadosZone = list()
    for val in getAllEmpleado():
        if val.get('codigo_empleado') == codigo_empleado :
            if (val.get('nombre') == nombre) or val.get('nombre') == None: 
                empleadosZone.append(val)

            else:
             empleadosZone.append(val)       
                
              
    return empleadosZone


def getOneEmpleadoExtension(puesto, nombre = None):
    empleadosZone = list()
    for val in getAllEmpleado():
        if val.get('puesto') == puesto :
            if (val.get('nombre') == nombre) or val.get('nombre') == None: 
                empleadosZone.append(val)

        else:
            empleadosZone.append(val)       
              
              
    return empleadosZone



def getNombreApellidoEmailJefe():
    NombreApellidoEmailJefe = []
    for val in getAllEmpleado():
        if val.get('codigo_jefe') == 7 :
            NombreApellidoEmailJefe.append(
                {
                    "nombre": val.get("nombre"),
                    "apellidos": f'{val.get("apellido1")} {val.get("apellido2")}',
                    "email": val.get("email")
                }
            )  
    return NombreApellidoEmailJefe

def getAllJefesCode():
    nombreApellidoEmail = []
    for val in getAllEmpleado():
        if val.get('codigo_jefe') == None :
            nombreApellidoEmail.append(
                {
                    "nombre": val.get("nombre"),
                    "apellidos": f'{val.get("apellido1")} {val.get("apellido2")}',
                    "email": val.get("email"),
                    "jefe": val.get("codigo_jefe")
                }
            )  
    return nombreApellidoEmail


def getEmpleadosPuesto():
    nombreApellidoPuesto = []
    for val in getAllEmpleado():
        if val.get('puesto') != "Representante Ventas" :
            nombreApellidoPuesto.append(
                {
                    "nombre": val.get("nombre"),
                    "apellidos": f'{val.get("apellido1")} {val.get("apellido2")}',
                    "puesto": val.get("puesto")
                }
            )  
    return nombreApellidoPuesto


def menu():
    while True:
        print("""

    ____                        __                   __        __                                   __               __          
   / __ \___  ____  ____  _____/ /____  _____   ____/ /__     / /___  _____   ___  ____ ___  ____  / /__  ____ _____/ /___  _____
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / __  / _ \   / / __ \/ ___/  / _ \/ __ `__ \/ __ \/ / _ \/ __ `/ __  / __ \/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  __/  / / /_/ (__  )  /  __/ / / / / / /_/ / /  __/ /_/ / /_/ / /_/ (__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/____/   \__,_/\___/  /_/\____/____/   \___/_/ /_/ /_/ .___/_/\___/\__,_/\__,_/\____/____/  
          /_/                                                                            /_/                                     


                                 1. Nombre, apellido y email de los empleados con codigo de jefe 7
                                 2. Puesto, nombre, apellido y email del jefe de la empresa
                                 3. Nombre, apellidos y puesto de aquellos que no son representantes de ventas
                                 4. Salir
""")
    
        opcion= int(input("\nSeleccione una de las opciones: "))
        if(opcion == 1):
            print(tabulate(getNombreApellidoEmailJefe(), headers="keys", tablefmt="github"))
        elif(opcion == 2):
            print(tabulate(getAllJefesCode(), headers="keys", tablefmt="github"))
        elif(opcion == 3):
            print(tabulate(getEmpleadosPuesto(), headers="keys", tablefmt="github"))
        elif(opcion == 4):
            break
        else:
            print("elija una opcion valida")