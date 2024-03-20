import json
import requests
import os
from tabulate import tabulate
import modules.getGamaProductos as getGamPro

def postGamaProducto():
    gama = {
            "gama": input("Ingrese el codigo de empleado: "),
            "descripcion_texto": input("Ingrese la descripcion en texto: "),
            "descripcion_html": input("Ingrese la descripcion en html: "),
            "imagen":input("Ingrese : "),
        }
   
   
     # json-server storage/empleado.json -b 5504
    peticion = requests.post("http://154.38.171.54:5004/gama", data = json.dumps(gama, indent =4).encode("UTF-8"))
    res=peticion.json()
    res["mensaje"] = "Gama de producto Guardada"
    return [res]


#if(__name__ == "__main__"):
#        with open("storage/empleado.json", "r") as f:
#            fichero = f.read()
#            data = json.loads(fichero)
#            for i, val in enumerate(data):
#                data[i]["id"] = (i+1)
#            data=json.dumps(data, indent=4).encode("utf-8")
#            with open("storage/empleado.json", "wb+") as f1:
#                f1.write(data)
#                f1.close()

def deletegamaproducto(id):
    data = getGamPro.getGamaProductoId(id)
    if(len(data)):
        peticion= requests.delete(f"http://154.38.171.54:5004/gama/{id}")
        if(peticion.status_code == 204):
            data.append({"message": "info de Gama Producto eliminada correctamente"})
            return{
                "body" : data,
                "status": peticion.status_code
            }
        
        else:
            return{
                "body": [{
                    "mesagge": "Info no encontrada",
                    "id": id
                }],
                "status": 400
            }


def menu():
  while True:
    os.system("clear")
    print("""


    ___       __          _       _      __                     ____        __            
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______   / __ \____ _/ /_____  _____
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/  / / / / __ `/ __/ __ \/ ___/
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /     / /_/ / /_/ / /_/ /_/ (__  ) 
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/__   /_____/\__,_/\__/\____/____/  
  ____/ /__     / /___  _____   / ____/___ ___  ____  / /__  ____ _____/ /___  _____      
 / __  / _ \   / / __ \/ ___/  / __/ / __ `__ \/ __ \/ / _ \/ __ `/ __  / __ \/ ___/      
/ /_/ /  __/  / / /_/ (__  )  / /___/ / / / / / /_/ / /  __/ /_/ / /_/ / /_/ (__  )       
\__,_/\___/  /_/\____/____/  /_____/_/ /_/ /_/ .___/_/\___/\__,_/\__,_/\____/____/        
                                            /_/                                           
                                 
            

                                 1. Guardar un nuevo de la gama de los productos
                                 2. Eliminar algun dato de la gama de los productos
                                 0. Salir
""")

    opcion= int(input("\nSeleccione una de las opciones: "))
    if(opcion == 1):
        print(tabulate(postGamaProducto(), headers="keys", tablefmt="github"))
        input("Presione Enter para continuar... ")
    elif(opcion == 2):
        idEmpleado = input(("Ingrese el id del cliente que deseas eliminar: "))
        print(tabulate(deletegamaproducto(idEmpleado)["body"], headers="keys", tablefmt="github"))

    elif(opcion==0):
       break
    else:
       print("Elija una opcion correcta: ")
