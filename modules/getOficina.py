import storage.oficina as ofi
from tabulate import tabulate 

def getCodigoOfiCiudadName():
    CodigoOfiCiudad = list()
    for val in ofi.oficina:
        codigoNames = dict({
            "codigo_oficina": val.get('codigo_oficina'),
            "ciudad": val.get('ciudad')
        })
        CodigoOfiCiudad.append(codigoNames)
    return CodigoOfiCiudad

def getCiudadTelefonoEspaña():
    ciudadTelefonoEspaña = []
    for val in ofi.oficina:
        if val.get('pais') == "España" :
            ciudadTelefonoEspaña.append(
                {
                    "ciudad": val.get("ciudad"),
                    "telefono": val.get("telefono")
                }
            )  
    return ciudadTelefonoEspaña

def menu():
    print("""

    ____                        __                   __        __               _____      _            
   / __ \___  ____  ____  _____/ /____  _____   ____/ /__     / /___ _   ____  / __(_)____(_)___  ____ _
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / __  / _ \   / / __ `/  / __ \/ /_/ / ___/ / __ \/ __ `/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  __/  / / /_/ /  / /_/ / __/ / /__/ / / / / /_/ / 
/_/ |_|\___/ .___/\____/_/   \__/\___/____/   \__,_/\___/  /_/\__,_/   \____/_/ /_/\___/_/_/ /_/\__,_/  
          /_/                                                                                           


                                 1. Codigo de oficina y ciudad donde hay oficinas
                                 2. Ciudad y telefono de las oficinas de España
""")
    
    opcion= int(input("\nSeleccione una de las opciones: "))
    if(opcion == 1):
        print(tabulate(getCodigoOfiCiudadName(), headers="keys", tablefmt="github"))
    elif(opcion == 2):
        print(tabulate(getCiudadTelefonoEspaña(), headers="keys", tablefmt="github"))
    else:
        print("elija una opcion valida")