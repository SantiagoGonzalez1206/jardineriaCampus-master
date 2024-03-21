import json
import requests
import os
import re
from tabulate import tabulate


import modules.getPedido as getPed
import modules.updatePedido as upPed

# def postPedido():
#     pedido = {
#         "codigo_pedido": int(input("Ingrese el codigo del pedido: ")),
#         "fecha_pedido": input("Ingrese la fecha del pedido: "),
#         "fecha_esperada": input("Ingrese la fecha esperada del pedido: "),
#         "fecha_entrega": input("Ingrese la fecha de entrega del pedido: "),
#         "estado": input("Ingrese el estado del pedido: "),
#         "comentario": input("Ingrese los comentarios acerca del pedido: "),
#         "codigo_cliente": int(input("Ingrese el codigo del cliente: "))
#         }
    
   
#     #json-server storage/pedido.json -b 5506
#     peticion = requests.post("http://154.38.171.54:5007/pedidos", data = json.dumps(pedido, indent =4).encode("UTF-8"))
#     res=peticion.json()
#     res["mensaje"] = "Producto Guardado"
#     return [res]



def agregarDatosPedidos():
    pedidos={}
    while True:
        try:

          

            if not pedidos.get("codigo_pedido"):
                codigoPedido=input("Ingresa el código del pedido: ")
                if(re.match(r'^\d+$',codigoPedido)is not None):
                    codigoPedido=int(codigoPedido)
                    Data=getPed.getCodeByCode(codigoPedido)
                    if(Data):
                        print(tabulate(Data, headers="keys",tablefmt="grid"))
                        raise Exception("El código ya existe")
                       
                    else:
                        pedidos["codigo_pedido"]=codigoPedido
                        print("El código cumple con el estandar, OK")
                else:
                    raise Exception("El código no cumple con el estandar establecido")

 
            
                
            if not pedidos.get("fecha_pedido"):
                fechaPedido =input("Ingresa la fecha del pedido(año-mes-día): ")
                if(re.match(r'^\d{4}-\d{2}-\d{2}$',fechaPedido)is not None):
                    pedidos["fecha_pedido"]=fechaPedido
                    print("la fecha del pedido cumple con el estandar,OK")
                    
                else:
                    raise Exception("La fecha del pedido no cumple con el estandar establecido")



            if not pedidos.get("fecha_esperada"):
                fechaEsperada =input("Ingresa la fecha de espera(año-mes-día): ")
                if(re.match(r'^\d{4}-\d{2}-\d{2}$',fechaEsperada)is not None):
                    pedidos["fecha_esperada"]=fechaEsperada
                    print("la fecha de espera cumple con el estandar,OK")
                   
                else:
                    raise Exception("La fecha de espera no cumple con el estandar establecido")



            if not pedidos.get("fecha_entrega"):
                fechaEntrega =input("Ingresa la fecha de entrega(año-mes-día): ")
                if(re.match(r'^\d{4}-\d{2}-\d{2}$',fechaEntrega)is not None):
                    pedidos["fecha_entrega"]=fechaEntrega
                    print("la fecha de entrega cumple con el estandar,OK")
                   
                else:
                    raise Exception("La fecha de entrega no cumple con el estandar establecido")
                

                
           

            if not pedidos.get("estado"):
                estado =input("Ingresa el estado del producto (ejemplos: Entregado, Pendiente, Rechazado): ")
                if(re.match(r'^[A-Z][a-z]+$',estado)is not None):
                    pedidos["estado"]=estado
                    print("El estado cumple con el estandar,OK")
                   
                else:
                    raise Exception("El estado no cumple con el estandar establecido")



        
            if not pedidos.get("comentario"):
                comentario =input("Ingresa un comentario sobre el pedido: ")
                if(re.match(r'\w+',comentario)is not None):
                    pedidos["comentario"]=comentario
                    print("El comentario cumple con el estandar,OK")
                   
                


           
            if not pedidos.get("codigo_cliente"):
                codigoCliente=input("Ingresa el codigo del cliente: ")
                if (re.match(r'^\d+$',codigoCliente)is not None):
                        codigoCliente= int(codigoCliente)
                        pedidos["codigo_cliente"]=codigoCliente
                        print("El codigo del cliente cumple con el estandar, OK")
                        break 
                else:
                    raise Exception("El código del cliente no cumple con el estandar establecido")  



        except Exception as error:
            print(error)
   

    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post("http://154.38.171.54:5007/pedidos",headers=headers, data=json.dumps(pedidos, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]







def deletepedido(id):
    data = getPed.getPedidoId(id)
    if(len(data)):
        peticion = requests.delete(f"http://154.38.171.54:5007/pedidos/{id}")
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
       __        __              ____           ___     __                                
  ____/ /__     / /___  _____   / __ \___  ____/ (_)___/ /___  _____                      
 / __  / _ \   / / __ \/ ___/  / /_/ / _ \/ __  / / __  / __ \/ ___/                      
/ /_/ /  __/  / / /_/ (__  )  / ____/  __/ /_/ / / /_/ / /_/ (__  )                       
\__,_/\___/  /_/\____/____/  /_/    \___/\__,_/_/\__,_/\____/____/                        
                                                                                          


                                 1. Guardar un nuevo pedido
                                 2. Eliminar un pedido
                                 3. Actualizar datos de los pedidos
                                 0. Salir
""")

    opcion= int(input("\nSeleccione una de las opciones: "))
    if(opcion == 1):
        print(tabulate(agregarDatosPedidos(), headers="keys", tablefmt="github"))
        input("Presione Enter para continuar... ")

    elif(opcion==2):
        idPedido = input(("Ingrese el id del cliente que deseas eliminar: "))
        print(tabulate(deletepedido(idPedido)["body"], headers="keys", tablefmt="github"))

    elif(opcion == 3):
        
        upPed.menu()

    elif(opcion==0):
       break
    else:
       print("Elija una opcion correcta: ")
