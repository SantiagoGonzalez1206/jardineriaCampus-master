import os
from tabulate import tabulate
import requests
import math

# Devuelve un listado con todos los productos que pertenecen a la gama Ornamentales 
# y que tienen más de 100 unidades en stock. El listado deberá estar ordenado por su precio de venta, 
# mostrando en primer lugar los de mayor precio.
def getAllData():
    # json-server storage/producto.json -b 5503
    peticion = requests.get("http://154.38.171.54:5008/productos")
    data = peticion.json()
    return data


def getProductoId(id):
    peticion = requests.get(f"http://154.38.171.54:5008/productos/{id}")
    return[peticion.json()] if peticion.ok else []


def getProductoCodigos(codigo):
    peticion = requests.get(f"http://154.38.171.54:5008/productos/{codigo}")
    return[peticion.json()] if peticion.ok else []

def getProductoCodigos2(codigo):
    peticion = requests.get(f"http://154.38.171.54:5008/productos?codigo_producto={codigo.upper()}")
    data = peticion.json()
    if(data)== 0:
        data=None
    return data

def getAllStocksPriceGama(gama, stock):
    condiciones = []
    for val in getAllData():
        if(val.get("gama") == gama and val.get("cantidad_en_stock") >= stock):
            condiciones.append(val)
    def price(val):
        return val.get("precio_venta")    
    condiciones.sort(key=price, reverse=True)
    for i, val in enumerate(condiciones):
        condiciones[i] = {
                "codigo": val.get("codigo_producto"),
                "venta": val.get("precio_venta"),
                "nombre": val.get("nombre"),
                "gama": val.get("gama"),
                "dimensiones": val.get("dimensiones"),
                "proveedor": val.get("proveedor"),
                "descripcion": f'{val.get("descripcion")[:5]}...' if condiciones[i].get("descripcion") else None,
                "stock": val.get("cantidad_en_stock"),
                "base": val.get("precio_proveedor")
            }
    return condiciones

def menu():
    while True:
        os.system("clear")
        print("""  
    ____                        __                   __                             __           __            
   / __ \___  ____  ____  _____/ /____  _____   ____/ /__     ____  _________  ____/ /_  _______/ /_____  _____
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / __  / _ \   / __ \/ ___/ __ \/ __  / / / / ___/ __/ __ \/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  __/  / /_/ / /  / /_/ / /_/ / /_/ / /__/ /_/ /_/ (__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/____/   \__,_/\___/  / .___/_/   \____/\__,_/\__,_/\___/\__/\____/____/  
          /_/                                             /_/                                                  

            1. Obtener todos los productos de una categoría ordenando sus precios de venta, también que su cantidad de inventario sea superior
            0. Atras
          
          """)        
        try:
            opcion = int(input("\nSelecione una de las opciones: "))
            if(opcion == 1):
                gama = input("Ingrese la gama que deseas filtrar: ")
                stock = int(input("Ingrese las unidades que quiera mostrar: "))
                print(tabulate(getAllStocksPriceGama(gama, stock), headers="keys", tablefmt="github"))
                input("Escriba alguna tecla para continuar... ")
            elif(opcion == 0):
                break
            else:
                print("elija una opcion valida")

        except ValueError: 
         print("Caracteres incorrectos, elija una opcion del 0 al 1")