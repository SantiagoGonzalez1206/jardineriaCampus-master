import json
import requests
import os
from tabulate import tabulate
import re
import time

import modules.getPago as getpag
import modules.updatePago as upPag


# def postPago():
#     pago = {
#             "codigo_cliente": int(input("Ingrese el codigo del cliente: ")),
#             "forma_pago": input("Ingrese la forma de pago: "),
#             "id_transaccion": input("Ingrese el id de la transaccion: "),
#             "fecha_pago": input("Ingrese la fecha de pago (Año/Mes/dia): "),
#             "total": int(input("Ingrese el total: ")),
#         }

#      # json-server storage/pago.json -b 5505
#     peticion = requests.post("http://154.38.171.54:5006/pagos", data = json.dumps(pago, indent =4).encode("UTF-8"))
#     res=peticion.json()
#     res["mensaje"] = "Producto Guardado"
#     return [res]

def agregarDatosPago():
    pagos={}
    while True:
        try:

            
            if not pagos.get("codigo_cliente"):
                codigoCliente=input("Ingresa el codigo del cliente: ")
                if (re.match(r'^\d+$',codigoCliente)is not None):
                        codigoCliente= int(codigoCliente)
                        pagos["codigo_cliente"]=codigoCliente
                        print("El codigo del cliente cumple con el estandar, OK")
                        
                else:
                    raise Exception("El código del cliente no cumple con el estandar establecido")  


           
            if not pagos.get("forma_pago"):
                formaPago =input("Ingresa el metodo de pago (ejemplo: PayPal): ")
                if(re.match(r'[A-Z][a-z]*(?:\s[A-Z][a-z]*)*(?:\s\d*)*',formaPago)is not None):
                    pagos["forma_pago"]=formaPago
                    print("La forma de pago cumple con el estandar,OK")
                   
                else:
                    raise Exception("La forma de pago no cumple con el estandar establecido")



            if not pagos.get("id_transaccion"):
                idTransaccion=input("Ingresa id de la transacción(ak-std-000000): ")
                if(re.match(r'ak-std-\d{6}',idTransaccion)is not None):
                    Data=getpag.getAllIdTransactions(idTransaccion)
                    if(Data):
                        print(tabulate(Data, headers="keys",tablefmt="grid"))
                        raise Exception("El id ya existe")
                      
                    else:
                        pagos["id_transaccion"]=idTransaccion
                        print("El id cumple con el estandar, OK")
                else:
                    raise Exception("El id no cumple con el estandar establecido")


           
            if not pagos.get("fecha_pago"):
                fechaPago =input("Ingresa la fecha del pago(año-mes-día): ")
                if(re.match(r'^\d{4}-\d{2}-\d{2}$',fechaPago)is not None):
                    pagos["fecha_pago"]=fechaPago
                    print("la fecha del pago cumple con el estandar,OK")
                   
                else:
                    raise Exception("La fecha del pago no cumple con el estandar establecido")



            
            if not pagos.get("total"):
                pagototal=input("Ingresa el valor del total(entero): ")
                if (re.match(r'^\d+$',pagototal)is not None):
                        pagototal= int(pagototal)
                        pagos["total"]=pagototal
                        print("El dato cumple con el estandar, OK")
                        break 
                raise Exception("El dato no cumple con el estandar establecido")  



        except Exception as error:
            print(error)
   

    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post("http://154.38.171.54:5006/pagos",headers=headers, data=json.dumps(pagos, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]





def deletepago(id):
    data = getpag.getPagoId(id)
    if(len(data)):
        peticion = requests.delete(f"http://154.38.171.54:5006/pagos/{id}")
        if(peticion.status_code == 204):
            data.append({"message": "cliente eliminado correctamente"})
            return {
                "body": data, 
                "status": peticion.status_code,
            }
    else:
        return {
            "body":[{
                "message":"cliente no encontrado",
                "id": id
            }],
            "status": 400,
        }


def menu():
  while True:
    os.system("clear")
    print("""


    ___       __          _       _      __                     ____        __            
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______   / __ \____ _/ /_____  _____
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/  / / / / __ `/ __/ __ \/ ___/
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /     / /_/ / /_/ / /_/ /_/ (__  ) 
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/     /_____/\__,_/\__/\____/____/  
  ____/ /__     / /___  _____   / __ \____ _____ _____  _____                             
 / __  / _ \   / / __ \/ ___/  / /_/ / __ `/ __ `/ __ \/ ___/                             
/ /_/ /  __/  / / /_/ (__  )  / ____/ /_/ / /_/ / /_/ (__  )                              
\__,_/\___/  /_/\____/____/  /_/    \__,_/\__, /\____/____/                               
                                         /____/                                           
       
                                 
            

                                 1. Guardar un nuevo registro de pago
                                 2. Eliminar un registro de pago
                                 3. Actualizar informacion de los pagos
                                 0. Salir
""")

    try:
        opcion= int(input("\nSeleccione una de las opciones: "))
        if(opcion == 1):
            print(tabulate(agregarDatosPago(), headers="keys", tablefmt="github"))
            input("Presione Enter para continuar... ")

        elif(opcion == 2):
            idPago = input(("Ingrese el id del cliente que deseas eliminar: "))
            print(tabulate(deletepago(idPago)["body"], headers="keys", tablefmt="github"))
        
        elif(opcion == 3):
            
            upPag.menu()
        
        elif(opcion==0):
            break
        else:
            print("Elija una opcion correcta: ")
    except ValueError:
        print("Seleccione una opcion valida del 0 al 3")
        time.sleep(3)

