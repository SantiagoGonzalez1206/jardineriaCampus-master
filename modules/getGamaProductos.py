import tabulate
import requests

def getAllGamaProductos():
    # json-server storage/cliente.json -b 5501
    peticion = requests.get("http://154.38.171.54:5004/gama")
    data = peticion.json()
    return data

def getGamaProductoId(id):
    peticion = requests.get(f"http://154.38.171.54:5004/gama/{id}")
    return[peticion.json()] if peticion.ok else []

def getAllDescripcion():
    gamaDescripcionTexto= []
    for val in getAllGamaProductos:
        gamaDescripcionTexto.append(val.get("descripcion_texto"))
    return gamaDescripcionTexto


def menu():
  while True:  
    print("""


    ____                        __              __        __     
   / __ \___  ____  ____  _____/ /____     ____/ /__     / /___ _
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \   / __  / _ \   / / __ `/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __/  / /_/ /  __/  / / /_/ / 
/_/_|_|\___/ .___/\____/_/   \__/\___/__ \__,_/\___/  /_/\__,_/           
  / ____/_/_/_____ ___  ____ _   ____/ /__     / /___  _____     
 / / __/ __ `/ __ `__ \/ __ `/  / __  / _ \   / / __ \/ ___/     
/ /_/ / /_/ / / / / / / /_/ /  / /_/ /  __/  / / /_/ (__  )      
\____/\__,_/_/ /_/ /_/\__,_/   \__,_/\___/  /_/\____/____/       
    ____                 __           __                         
   / __ \_________  ____/ /_  _______/ /_____  _____             
  / /_/ / ___/ __ \/ __  / / / / ___/ __/ __ \/ ___/             
 / ____/ /  / /_/ / /_/ / /_/ / /__/ /_/ /_/ (__  )              
/_/   /_/   \____/\__,_/\__,_/\___/\__/\____/____/               
                                                                 


             1. Obtener toda la informacion de la gama de los productos
             2. Obtener todas las descripciones por texto
             0. Salir
""")
    
    opcion= int(input("\nSeleccione una de las opciones: "))
    if(opcion == 1):
        print(tabulate(getAllGamaProductos(), headers="keys", tablefmt="github"))
    elif(opcion == 2):
        print(tabulate(getAllDescripcion(), headers="keys", tablefmt="github"))
    elif(opcion == 0):
       break
    else:
        print("elija una opcion valida ")
    