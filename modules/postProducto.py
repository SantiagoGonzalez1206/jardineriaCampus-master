import json
import requests
import os
from tabulate import tabulate

import modules.getProducto as getpro
import modules.updateProducto as upPro

def postProducto():
    producto = {
            "codigo_producto": input("Ingrese el codigo del producto: "),
            "nombre": input("Ingrese el nombre del producto: "),
            "gama": input("Ingrese la gama del producto: "),
            "dimensiones": input("Ingrese las dimensiones del producto: "),
            "proveedor": input("Ingrese el proveedor del producto: "),
            "descripcion": input("Ingrese la descripcion del producto: "),
            "cantidad_en_stock": int(input("Ingrese la cantidad del producto: ")),
            "precio_venta": int(input("Ingrese el precio de venta del producto: ")),
            "precio_proveedor": int(input("Ingrese el precio de proveedor del producto: "))
       }
    
    
    
    peticion = requests.post("http://154.38.171.54:5008/productos", data = json.dumps(producto, indent =4).encode("UTF-8"))
    res=peticion.json()
    res["mensaje"] = "Producto Guardado"
    return [res]
#if(__name__ == "__main__"):
#        with open("storage/producto.json", "r") as f:
#            fichero = f.read()
#            data = json.loads(fichero)
#            for i, val in enumerate(data):
#                data[i]["id"] = (i+1)
#            data=json.dumps(data, indent=4).encode("utf-8")
#            with open("storage/producto.json", "wb+") as f1:
#                f1.write(data)
#                f1.close()


def deleteproducto(id):
    data = getpro.getProductoId(id)
    if(len(data)):
        peticion= requests.delete(f"http://154.38.171.54:5008/productos/{id}")
        if(peticion.status_code == 204):
            data.append({"message": "Producto eliminado correctamente"})
            return{
                "body" : data,
                "status": peticion.status_code
            }
        
        else:
            return{
                "body": [{
                    "mesagge": "producto no encontrado",
                    "id": id
                }],
                "status": 400
            }   


    #json-server storage/producto.json -b 5503
        
        
#    peticion = requests.post("http://172.16.100.142:5503", data = json.dumps(producto, indent =4).encode("UTF-8"))
#    res=peticion.json()
#    res["mensaje"] = "Producto Guardado"
#    return [res]

def menu():
  while True:
    os.system("clear")
    print("""


    ___       __          _       _      __                     ____        __                    __   
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______   / __ \____ _/ /_____  _____   ____/ /__ 
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/  / / / / __ `/ __/ __ \/ ___/  / __  / _ |
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /     / /_/ / /_/ / /_/ /_/ (__  )  / /_/ /  __/
/_/ _|_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/_    /_____/\__,_/\__/\____/____/   \__,_/\___/ 
   / /___  _____   / __ \_________  ____/ /_  _______/ /_____  _____                                   
  / / __ \/ ___/  / /_/ / ___/ __ \/ __  / / / / ___/ __/ __ \/ ___/                                   
 / / /_/ (__  )  / ____/ /  / /_/ / /_/ / /_/ / /__/ /_/ /_/ (__  )                                    
/_/\____/____/  /_/   /_/   \____/\__,_/\__,_/\___/\__/\____/____/                                     
                                                                                                       
            

                                 1. Guardar un nuevo producto
                                 2. Eliminar un producto
                                 3. Actualizar los datos de un producto
                                 0. Salir
""")

    opcion= int(input("\nSeleccione una de las opciones: "))
    if(opcion == 1):
        print(tabulate(postProducto(), headers="keys", tablefmt="github"))
        input("Presione Enter para continuar... ")

    elif(opcion == 2):
        idProducto = input(("Ingrese el id del producto que deseas eliminar: "))
        print(tabulate(deleteproducto(idProducto)["body"], headers="keys", tablefmt="github"))
    
    elif(opcion == 3):
        
        upPro.menu()

    elif(opcion==0):
       break
    else:
       print("Elija una opcion correcta: ")
