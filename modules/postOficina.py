import json
import requests
import os
import re
from tabulate import tabulate

import modules.getOficina as getOfi
import modules.updateOficina as upOfi

# def postOficina():
#     oficina = {
#         "codigo_oficina": input("Ingrese el codigo de la oficina: "),
#         "ciudad": input("Ingrese la ciudad de la oficina: "),
#         "pais": input("Ingrese el pais de la oficina: "),
#         "region": input("Ingrese la region de la oficina: "),
#         "codigo_postal": input("Ingrese el codigo postal de la oficina: "),
#         "telefono": input("Ingrese el numero de telefono de la oficina: "),
#         "linea_direccion1": input("Ingrese la linea de direccion 1: "),
#         "linea_direccion2": input("Ingrese la linea de direccion 2: ")
#         }
    
   
#     #json-server storage/oficina.json -b 5501
#     peticion = requests.post("http://154.38.171.54:5005/oficinas", data = json.dumps(oficina, indent =4).encode("UTF-8"))
#     res=peticion.json()
#     res["mensaje"] = "Producto Guardado"
#     return [res]


def agregarDatosOficina():
    oficinas={}
    while True:
        try:
            # expresion regular que tenga en cuenta escribir un numero solamente
            if not oficinas.get("codigo_oficina"):
                codigoOficina=input("Ingresa el código de la oficina(AAA-AAA): ")
                if(re.match(r'^[A-Z]+-[A-Z]+$',codigoOficina)is not None):
                    Data=getOfi.getCodeOfficeCode(codigoOficina)
                    if(Data):
                        print(tabulate(Data, headers="keys",tablefmt="grid"))
                        raise Exception("El código de la oficina ya es existente")
                        #break #solo para el ultimo modulo sino se rompe
                    else:
                        oficinas["codigo_oficina"]=codigoOficina
                        print("El dato cumple con el estandar,OK")

                else:
                    raise Exception("El dato no cumple con el estandar establecido")


            # expresion regular que tenga en cuenta una palabra con mayuscula al principio,o  que pueda ser toda mayuscula, o que pueda tener un guion, que puedan ser varias palabras, que pueda tener numeros ni caracteres especiales
            if not oficinas.get("ciudad"):
                ciudad =input("Ingresa la ciudad de la oficina: ")
                if(re.match(r'^([A-ZÁÉÍÓÚÜ][a-záéíóúü]*-?)+[A-ZÁÉÍÓÚÜ]?[a-záéíóúü]*$',ciudad)is not None):
                    oficinas["ciudad"]=ciudad
                    print("El dato cumple con el estandar,OK")
                    #break #solo para el ultimo modulo sino se rompe
                else:
                    raise Exception("El dato no cumple con el estandar establecido")



            if not oficinas.get("pais"):
                pais =input("Ingresa el país de la oficina: ")
                if(re.match(r'^([A-ZÁÉÍÓÚÜ][a-záéíóúü]*-?)+[A-ZÁÉÍÓÚÜ]?[a-záéíóúü]*$',pais)is not None):
                    oficinas["pais"]=pais
                    print("El dato cumple con el estandar,OK")
                    #break #solo para el ultimo modulo sino se rompe
                else:
                    raise Exception("El dato no cumple con el estandar establecido")



            if not oficinas.get("region"):
                region =input("Ingresa la región de la oficina: ")
                if(re.match(r'^([A-ZÁÉÍÓÚÜ][a-záéíóúü]*-?)+[A-ZÁÉÍÓÚÜ]?[a-záéíóúü]*$',region)is not None):
                    oficinas["region"]=region
                    print("El dato cumple con el estandar,OK")
                    #break #solo para el ultimo modulo sino se rompe
                else:
                    raise Exception("El dato no cumple con el estandar establecido")



            #expresion regular que tenga en cuenta la escritura de numeros solamente, o que escriba unas letras(obligatorio en mayuscula) junto con numeros separados por un espacio, o que pueda ser un numero seguido de un guión y luego más numeros todo pegado
            if not oficinas.get("codigo_postal"):
                codigoPostal =input("Ingresa el código postal de la oficina: ")
                if(re.match(r'^(\d+|[A-Z]+\s\d+|\d+-\d+)$',codigoPostal)is not None):
                    oficinas["codigo_postal"]=codigoPostal
                    print("El dato cumple con el estandar,OK")
                    #break #solo para el ultimo modulo sino se rompe
                else:
                    raise Exception("El dato no cumple con el estandar establecido")
                


            # expresion que tenga en cuenta la escritura de un telefono de oficina, debe ser 11 numeros en total pueden llevar espacios, es obligatorio que tenga un  +de primero, un numero pegado y un espacio, separado del resto de numeros
            if not oficinas.get("telefono"):
                telefono=input("Ingresa el teléfono de la oficina(+00 000 0000 000): ")
                if(re.match(r'^\+\d{1,2} \d{1,3} \d{1,4} \d{1,4}$',telefono)is not None):
                    Data=getOfi.getTelFromTel(telefono)
                    if(Data):
                        print(tabulate(Data, headers="keys",tablefmt="grid"))
                        raise Exception("El telefono de la oficina ya existe")
                        #break #solo para el ultimo modulo sino se rompe
                    else:
                        oficinas["telefono"]=telefono
                        print("El dato cumple con el estandar,OK")

                else:
                    raise Exception("El dato no cumple con el estandar establecido")




            # expresion que tenga en cuenta la escritura de una direccion 
            if not oficinas.get("linea_direccion1"):
                direcion1=input("Ingresa la primera direccion de la oficina: ")
                if(re.match(r'\w+',direcion1)is not None):
                    Data=getOfi.getDireccion1FromDireccion(direcion1)
                    if(Data):
                        print(tabulate(Data, headers="keys",tablefmt="grid"))
                        raise Exception("la dirección de la oficina ya existe")
                        #break #solo para el ultimo modulo sino se rompe
                    else:
                        oficinas["linea_direccion1"]=direcion1
                        print("El dato cumple con el estandar,OK")

                else:
                    raise Exception("El dato no cumple con el estandar establecido")
                


            if not oficinas.get("linea_direccion2"):
                direccion2=input("Ingresa la segunda direccion de la oficina: ")
                if(re.match(r'\w+',direccion2)is not None):
                    Data=getOfi.getDireccion2FromDireccion(direccion2)
                    if(Data):
                        print(tabulate(Data, headers="keys",tablefmt="grid"))
                        raise Exception("La dirección de la oficina ya existe")
                        #break #solo para el ultimo modulo sino se rompe
                    else:
                        oficinas["linea_direccion2"]=direccion2
                        print("El dato cumple con el estandar,OK")

                else:
                    raise Exception("El dato no cumple con el estandar establecido")


        except Exception as error:
            print(error)
   

        headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
        peticion = requests.post("http://154.38.171.54:5005/oficinas/",headers=headers, data=json.dumps(oficinas, indent=4).encode("UTF-8"))
        res = peticion.json()
        res["Mensaje"] = "Producto Guardado"
        return [res]





def deleteoficina(id):
    data = getOfi.getOficinaId(id)
    if(len(data)):
        peticion = requests.delete(f"http://154.38.171.54:5005/oficinas/{id}")
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
       __        __                    _____      _                                       
  ____/ /__     / /___ ______   ____  / __(_)____(_)___  ____ ______                      
 / __  / _ \   / / __ `/ ___/  / __ \/ /_/ / ___/ / __ \/ __ `/ ___/                      
/ /_/ /  __/  / / /_/ (__  )  / /_/ / __/ / /__/ / / / / /_/ (__  )                       
\__,_/\___/  /_/\__,_/____/   \____/_/ /_/\___/_/_/ /_/\__,_/____/                        
                                                                                          


                                 1. Guardar un nuevo dato de oficina
                                 2. Eliminar un dato de oficina
                                 3. Actualizar datos de oficina
                                 0. Salir
""")

    opcion= int(input("\nSeleccione una de las opciones: "))
    if(opcion == 1):
        print(tabulate(agregarDatosOficina(), headers="keys", tablefmt="github"))
        input("Presione Enter para continuar... ")
        
    elif(opcion == 2):
        idOficina = input(("Ingrese el id del cliente que deseas eliminar: "))
        print(tabulate(deleteoficina(idOficina)["body"], headers="keys", tablefmt="github"))

    elif(opcion == 3):
        
        upOfi.menu()

    elif(opcion==0):
       break
    else:
       print("Elija una opcion correcta: ")
