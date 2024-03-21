import json
import requests
import os
import re
from tabulate import tabulate

import modules.getProducto as getPro
import modules.updateProducto as upPro

# def postProducto():
#     producto = {
#             "codigo_producto": input("Ingrese el codigo del producto: "),
#             "nombre": input("Ingrese el nombre del producto: "),
#             "gama": input("Ingrese la gama del producto: "),
#             "dimensiones": input("Ingrese las dimensiones del producto: "),
#             "proveedor": input("Ingrese el proveedor del producto: "),
#             "descripcion": input("Ingrese la descripcion del producto: "),
#             "cantidad_en_stock": int(input("Ingrese la cantidad del producto: ")),
#             "precio_venta": int(input("Ingrese el precio de venta del producto: ")),
#             "precio_proveedor": int(input("Ingrese el precio de proveedor del producto: "))
#        }
    
    
    
#     peticion = requests.post("http://154.38.171.54:5008/productos", data = json.dumps(producto, indent =4).encode("UTF-8"))
#     res=peticion.json()
#     res["mensaje"] = "Producto Guardado"
#     return [res]
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


def agregarDatosProductos():
    producto={}
    while True:
        try:

            # expresion regular que deje escribir un codigo tipo OR-123 que sea obligatorio los 2 primeros datos en mayusculas y que sean letras nada de simbolos o especiales, un guión pegado y por ultimo 3 numeros todo pegado
            if not producto.get("codigo_producto"):
                codigo=input("Ingresa el código del producto (ejemplo:OR-123): ")
                if(re.match(r'^[A-Z]{2}-[0-9]{3}$',codigo)is not None):
                    Data=getPro.getAllCodeByCode(codigo)
                    if(Data):
                        print(tabulate(Data, headers="keys",tablefmt="grid"))
                        raise Exception("El código del producto ya es existente")
                        #solo para el ultimo modulo sino se rompe
                    else:
                        producto["codigo_producto"]=codigo
                        print("El código cumple con el estandar, OK")

            else:
                raise Exception("El código del producto no cumple con el estandar establecido, DENEGADO")



            # expresion regular que tenga en cuenta la escritura de un nombre con la primera letra en mayusc, que se pueda escribir en una sola palabra o mas de una y respete espacios entre si
            if not producto.get("nombre"):
                nombre =input("Ingrese el nombre del producto: ")
                if(re.match(r'^[A-Z][a-z]*(?: [A-Z][a-z]*)*$',nombre)is not None):
                    producto["nombre"]=nombre
                    print("El nombre cumple con el estandar,OK")
                    #solo para el ultimo modulo sino se rompe
                else:
                    raise Exception("El nombre del producto no cumple con el estandar establecido")


            # expresion regular que tenga en cuenta la escritura de palabras primera letra en mayuscula seguidas de minusculas, una palabra única, nada más, sin numeros ni simbolos especiales
            if not producto.get("gama"):
                gama =input("Ingresa la gama del producto (ejemplos existentes: Herramientas, Ornamentales, Herbaceas, Aromáticas, Frutales): ")
                if(re.match(r'^[A-Z][a-z]+$',gama)is not None):
                    producto["gama"]=gama
                    print("El dato cumple con el estandar,OK")
                    #solo para el ultimo modulo sino se rompe
                else:
                    raise Exception("El dato no cumple con el estandar establecid")


            # expresion regular que tenga en cuenta la escritura de unas dimenciones, un numero seguido de una x y terminando con otro numero, estos deben ser enteros y un ejemplo debe quedar asi: 20x50
            if not producto.get("dimensiones"):
                dimenciones=input("Ingresa las dimenciones de tu producto (ejemplo: 20x50): ")
                if(re.match(r'^\d+x\d+$',dimenciones)is not None):
                        producto["dimensiones"]=dimenciones
                        print("El código cumple con el estandar, OK")
                        
                else:
                    raise Exception("La dimención no cumple con el estandar establecido")


            # expresion regular que tenga en cuenta la escritura de un nombre con primera en mayuscula,seguido de minusculas, que pueda tener mayusculas entremedio si es solo un nombre, que pueda tener más de una palabra nombre y separados con espacios 
            if not producto.get("proveedor"):
                dimenciones=input("Ingresa el nombre del proveedor: ")
                if(re.match(r'^[A-Z][a-zA-Z]*(\s[A-Z][a-z]*)*$',dimenciones)is not None):
                        producto["proveedor"]=dimenciones
                        print("El nombre cumple con el estandar, OK")
                        
                else:
                    raise Exception("El nombre no cumple con el estandar establecido")            


           
            if not producto.get("cantidad_en_stock"):
                stock=input("Ingresa la cantidad de producto en stock: ")
                if (re.match(r'^\d+$',stock)is not None):
                        stock= int(stock)  # SE DEBE TRANSFORMAR DE STRING A VALOR NUMERICO
                        producto["cantidad_en_stock"]=stock
                        print("El dato cumple con el estandar, OK")
                        
                else:
                    raise Exception("El dato no cumple con el estandar establecido")   


           
            if not producto.get("precio_venta"):
                precioVenta=input("Ingresa el valor del precio de venta en dolares (precio entero): ")
                if (re.match(r'^\d+$',precioVenta)is not None):
                        precioVenta= int(precioVenta)
                        producto["precio_venta"]=precioVenta
                        print("El dato cumple con el estandar, OK")
                        
                else:
                    raise Exception("El dato no cumple con el estandar establecido")  



           
            if not producto.get("precio_proveedor"):
                precioProveedor=input("Ingresa el valor del precio del proveedor en dolares (precio entero): ")
                if (re.match(r'^\d+$',precioProveedor)is not None):
                        precioProveedor= int(precioProveedor)
                        producto["precio_proveedor"]=precioProveedor
                        print("El dato cumple con el estandar, OK")
                        break 
                else:
                    raise Exception("El dato no cumple con el estandar establecido")  



        except Exception as error:
            print(error)

 
    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post("http://154.38.171.54:5008/productos",headers=headers, data=json.dumps(producto, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]




def deleteproducto(id):
    data = getPro.getProductoId(id)
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
        print(tabulate(agregarDatosProductos(), headers="keys", tablefmt="github"))
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
