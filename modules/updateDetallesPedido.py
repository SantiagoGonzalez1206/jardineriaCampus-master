import json
import requests
import modules.getProducto as getPro
from tabulate import tabulate

def updateProductoNombre(codigo):
    while True:
        if(codigo != None):
            producto= getPro.getProductoCodigos2((codigo))
            if (producto):
                print(tabulate(producto, headers="keys", tablefmt="github"))
                opc=int(input("""
                    ¿Este es el producto que desea actualizar?
                            1. Si
                            2. No
                """))
                if(opc):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    producto[0]["nombre"] = input("ingrese el nuevo nombre del producto: ")
                    peticion = requests.put(f'http://154.38.171.54:5008/productos/{producto[0].get("id")}', headers= headers, data= json.dumps(producto[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el producto {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del producto")
        
