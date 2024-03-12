import storage.cliente as cli
import storage.empleado as emp
import storage.pago as pag
from tabulate import tabulate 

def getNombreClientesEspaña():
    NombreClientesEspaña = []
    for val in cli.clientes:
        if val.get('pais') == "Spain" :
            NombreClientesEspaña.append(
                {
                    "nombre_cliente": val.get("nombre_cliente")
                }
            )  
    return NombreClientesEspaña

def getClienteCiudadMadrid1130():
    ClienteCiudadDeMadrid = []
    for val in cli.clientes:
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
    for val1 in cli.clientes:
        for val2 in emp.empleado:
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
    for val1 in pag.pago:
        for val2 in cli.clientes:
            for val3 in emp.empleado:
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
    for val in cli.clientes:
        pagos = False
        for val2 in pag.pago:
                if val.get('codigo_cliente')== val2.get("codigo_cliente"):
                    pagos = True
                    break
        if not pagos:
            for val2 in emp.empleado:
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
    ____                        __                   __        __                   ___            __           
   / __ \___  ____  ____  _____/ /____  _____   ____/ /__     / /___  _____   _____/ (_)__  ____  / /____  _____
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / __  / _ \   / / __ \/ ___/  / ___/ / / _ \/ __ \/ __/ _ \/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  __/  / / /_/ (__  )  / /__/ / /  __/ / / / /_/  __(__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/____/   \__,_/\___/  /_/\____/____/   \___/_/_/\___/_/ /_/\__/\___/____/  
          /_/                                                                                                   


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
    