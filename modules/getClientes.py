from tabulate import tabulate 
import requests




def getAllCliente():
    # json-server storage/cliente.json -b 5501
    peticion = requests.get("http://154.38.171.54:5001/cliente")
    data = peticion.json()
    return data

def getAllEmpleado():
    # json-server storage/empleado.json -b 5504
    peticion = requests.get("http://154.38.171.54:5003/empleados")
    data = peticion.json()
    return data

def getAllPago():
    # json-server storage/pago.json -b 5505
    peticion = requests.get("http://154.38.171.54:5006/pagos")
    data = peticion.json()
    return data


def getClienteId(id):
    peticion = requests.get(f"http://154.38.171.54:5001/cliente/{id}")
    return[peticion.json()] if peticion.ok else []


def getClienteCodigos(codigo):
    peticion = requests.get(f"http://154.38.171.54:5001/cliente/{codigo}")
    return[peticion.json()] if peticion.ok else []

def getClienteCodigos2(codigo):
    peticion = requests.get(f"http://154.38.171.54:5001/cliente?codigo_cliente={codigo.upper()}")
    data = peticion.json()
    if(data)== 0:
        data=None
    return data



def getTel(telefono):
     Officecode=[]
     for val in getAllCliente():
        if val.get("telefono")==telefono:
            return[val]
        
      
def getfax(fax):
     fax=[]
     for val in getAllCliente():
        if val.get("fax")==fax:
            return[val]

#obtener direcciones a partir de direcciones
def getDireccion1(direccion):
     linea1=[]
     for val in getAllCliente():
        if val.get("linea_direccion1")==direccion:
            return[val]
        
def getDireccion2(direccion):
     line2=[]
     for val in getAllCliente():
        if val.get("linea_direccion2")==direccion:
            return[val]






def getNombreClientesEspaña():
    NombreClientesEspaña = []
    for val in getAllCliente():
        if val.get('pais') == "Spain" :
            NombreClientesEspaña.append(
                {
                    "nombre_cliente": val.get("nombre_cliente")
                }
            )  
    return NombreClientesEspaña

def getClienteCiudadMadrid1130():
    ClienteCiudadDeMadrid = []
    for val in getAllCliente():
        if val.get("ciudad") == "Madrid":
            if val.get("codigo_empleado_rep_ventas") in [11, 30]:
                ClienteCiudadDeMadrid.append(
                    {
                        "codigoCliente": val.get("codigo_cliente"),
                        "nombreCliente": val.get("nombre_cliente"),
                        "ciudad": val.get("ciudad"),
                        "representante_de_ventas": val.get("codigo_empleado_rep_ventas")
                    }
                )
    return ClienteCiudadDeMadrid

def getClienteRepresentanteVenta():
    clienteRepre = []
    for val1 in getAllCliente():
        for val2 in getAllEmpleado():
            if val1.get("codigo_empleado_rep_ventas") == val2.get("codigo_empleado") and val2.get("puesto") == "Representante Ventas":
                clienteRepre.append(
                    {
                        "nombre": val1.get("nombre_cliente"),
                        "nombre_representante": val2.get("nombre"),
                        "apellido_representante": f"{val2.get('apellido1')}  {val2.get('apellido2')}"
                    }
                )
    return clienteRepre

def getclientePagos():
    clientePagos =[]
    for val1 in getAllPago():
        for val2 in getAllCliente():
            for val3 in getAllEmpleado():
                if val2.get("codigo_cliente") == val1.get("codigo_cliente") and val2.get("codigo_empleado_rep_ventas") == val3.get("codigo_empleado"): 

                    clientePagos.append(
                        {
                            "codigo_cliente":val1.get("codigo_cliente"),
                            "nombre":val2.get("nombre_cliente"),
                            "cod_representante": val2.get("codigo_empleado_rep_ventas"),
                            "nombre_empleado": val3.get("nombre")
                        }
                    )
    return  clientePagos

def getClienteNoPagos():
    ClienteNoPagos = []
    for val in getAllCliente():
        pagos = False
        for val2 in getAllPago():
                if val.get('codigo_cliente')== val2.get("codigo_cliente"):
                    pagos = True
                    break
        if not pagos:
            for val2 in getAllEmpleado():
                if val.get('codigo_empleado_rep_ventas') == val2.get("codigo_empleado"):
                    if val2.get('puesto') == "Representante Ventas":
                        ClienteNoPagos.append({

                                "codigo": val.get("codigo_cliente"),
                                "Nombre Cliente": val.get("nombre_cliente"),
                                "puesto": val2.get("puesto"),
                                "Representante de ventas": val2.get("nombre")
                            })
    return ClienteNoPagos


def menu():
  while True:  
    print("""

______                      _             _        _             _____ _ _            _            
| ___ \                    | |           | |      | |           /  __ \ (_)          | |           
| |_/ /___ _ __   ___  _ __| |_ ___    __| | ___  | | ___  ___  | /  \/ |_  ___ _ __ | |_ ___  ___ 
|    // _ \ '_ \ / _ \| '__| __/ _ \  / _` |/ _ \ | |/ _ \/ __| | |   | | |/ _ \ '_ \| __/ _ \/ __|
| |\ \  __/ |_) | (_) | |  | ||  __/ | (_| |  __/ | | (_) \__ \ | \__/\ | |  __/ | | | ||  __/\__ \
\_| \_\___| .__/ \___/|_|   \__\___|  \__,_|\___| |_|\___/|___/  \____/_|_|\___|_| |_|\__\___||___/
          | |                                                                                      
          |_|                                                                                      


             1. Obtener todos los clientes de España
             2. Obtener los clientes de Madrid cuyo codigo de representante de ventas sea 11 o 30
             3. Obtener nombre de cada cliente y nombre y apellido de su representante de ventas
             4. Obtener el nombre de los clientes que hayan realizado pagos y el nombre de sus representantes de ventas
             5. Obtener el nombre de los clientes que NO hayan realizado pagos y el nombre de sus representantes de ventas
             6. Salir
""")
    
    opcion= int(input("\nSeleccione una de las opciones: "))
    if(opcion == 1):
        print(tabulate(getNombreClientesEspaña(), headers="keys", tablefmt="github"))
    elif(opcion == 2):
        print(tabulate(getClienteCiudadMadrid1130(), headers="keys", tablefmt="github"))
    elif(opcion == 3):
        print(tabulate(getClienteRepresentanteVenta(), headers="keys", tablefmt="github"))
    elif(opcion == 4):
        print(tabulate(getclientePagos(), headers="keys", tablefmt="github"))
    elif(opcion == 5):
        print(tabulate(getClienteNoPagos(), headers="keys", tablefmt="github"))
    elif(opcion == 6):
       break
    else:
        print("elija una opcion valida ")
    