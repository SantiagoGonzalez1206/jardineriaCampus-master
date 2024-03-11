import storage.cliente as cli
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


def menu():
  while True:  
    print("""
    ____                        __                   __        __                   ___            __           
   / __ \___  ____  ____  _____/ /____  _____   ____/ /__     / /___  _____   _____/ (_)__  ____  / /____  _____
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / __  / _ \   / / __ \/ ___/  / ___/ / / _ \/ __ \/ __/ _ \/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  __/  / / /_/ (__  )  / /__/ / /  __/ / / / /_/  __(__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/____/   \__,_/\___/  /_/\____/____/   \___/_/_/\___/_/ /_/\__/\___/____/  
          /_/                                                                                                   


                                 1.Obtener todos los clientes de España
                                 2.Salir
""")
    
    opcion= int(input("\nSeleccione una de las opciones: "))
    if(opcion == 1):
        print(tabulate(getNombreClientesEspaña(), headers="keys", tablefmt="github"))
    elif(opcion == 2):
       break
    else:
        print("elija una opcion valida")
    