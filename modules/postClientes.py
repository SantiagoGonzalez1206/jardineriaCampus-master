import json
import requests
import os
from tabulate import tabulate 
import re
import time

import modules.getClientes as getcli
import modules.updateClientes as upCli


def getAllCliente():
      peticion=requests.get("http://154.38.171.54:5001/cliente") 
      Informacion=peticion.json()  
      return Informacion   




#def postCliente():
#    cliente = {
#        "codigo_cliente": int(input("Ingrese el codigo del cliente: ")),
#        "nombre_cliente": input("Ingrese el nombre del cliente: "),
#        "nombre_contacto": input("Ingrese el nombre de contacto: "),
#        "apellido_contacto": input("Ingrese el apellido de contacto: "),
#        "telefono": input("Ingrese el telefono del cliente: "),
#        "fax": input("Ingrese el fax cliente: "),
#        "linea_direccion1": input("Ingrese la linea de direccion 1: "),
#        "linea_direccion2": input("Ingrese la linea de direccion 2: "),
#        "ciudad": input("Ingrese la ciudad del cliente: "),
#        "region": input("Ingrese la region del cliente: "),
#        "pais": input("Ingrese el pais del cliente: "),
#        "codigo_postal": input("Ingrese el codigo postal del cliente: "),
#        "codigo_empleado_rep_ventas": int(input("Ingrese el codigo del representante de ventas del cliente: ")),
#        "limite_credito": int(input("Ingrese el limite de credito del cliente: "))
#        }


def agregarDatosDeClientes():
    Clientes={}
    while True:
        try:


          
            if not Clientes.get("codigo_cliente"):
                codigoCliente=input("Ingresa el codigo del cliente: ")
                if (re.match(r'^\d$',codigoCliente)is not None):
                    codigoCliente= int(codigoCliente)
                    Data=getcli.getclientFormClient(codigoCliente)
                    if(Data):
                        print(tabulate(Data, headers="keys",tablefmt="grid"))
                        raise Exception("El código ya existe")
                     
                else:
                    Clientes["codigo_cliente"]=codigoCliente
                    print("El codigo del cliente cumple con el estandar, OK")



           

            if not Clientes.get("nombre_cliente"):
                nombreCliente =input("Ingresa el nombre del cliente: ")
                if(re.match(r'\w+',nombreCliente)is not None):
                    Clientes["nombre_cliente"]=nombreCliente
                    print("El dato es valido")
                   
                


            

            if not Clientes.get("nombre_contacto"):
                nombreCliente =input("Ingresa el nombre del representante de la empresa: ")
                if(re.match(r'^[A-Z][a-z]*$',nombreCliente)is not None):
                    Clientes["nombre_contacto"]=nombreCliente
                    print("El dato es valido")
                   
                

            if not Clientes.get("apellido_contacto"):
                nombreCliente =input("Ingresa el apellido de representante de la empresa(ejemplo: Alberto): ")
                if(re.match(r'^[A-Z][a-z]*$',nombreCliente)is not None):
                    Clientes["apellido_contacto"]=nombreCliente
                    print("El dato es valido")
                    #break #solo para el ultimo modulo sino se rompe
                


            # expresion regular que tenga en cuenta la escritura de un numero de 10 digitos
            if not Clientes.get("telefono"):
                telefono=input("Ingresa el teléfono del cliente(000000000): ")
                if(re.match(r'^\d{10}$',telefono)is not None):
                    Data=getcli.getTel(telefono)
                    if(Data):
                        print(tabulate(Data, headers="keys",tablefmt="grid"))
                        raise Exception("El telefono del cliente ya existe")
                        #break #solo para el ultimo modulo sino se rompe
                    else:
                        Clientes["telefono"]=telefono
                        print("El dato es valido")

                else:
                    raise Exception("El dato no cumple con el estandar establecido")
       
            

            # expresion regular que tenga en cuenta la escritura de un numero de 9 digitos

            if not Clientes.get("fax"):
                fax=input("Ingresa el fax del cliente(000000000): ")
                if(re.match(r'^\d{9}$',fax)is not None):
                    Data=getcli.getfax(fax)
                    if(Data):
                        print(tabulate(Data, headers="keys",tablefmt="grid"))
                        raise Exception("El fax del cliente ya existe")
                        #break #solo para el ultimo modulo sino se rompe
                    else:
                        Clientes["fax"]=fax
                        print("El dato es valido")

                else:
                    raise Exception("El dato no cumple con el estandar establecido")




            # expresion que tenga en cuenta la escritura de una direccion 
            if not Clientes.get("linea_direccion1"):
                direccion1=input("Ingresa la primera direccion del cliente: ")
                if(re.match(r'\w+',direccion1)is not None):
                    Data=getcli.getDireccion1(direccion1)
                    if(Data):
                        print(tabulate(Data, headers="keys",tablefmt="grid"))
                        raise Exception("la dirección ya existe")
                        #break #solo para el ultimo modulo sino se rompe
                    else:
                        Clientes["linea_direccion1"]=direccion1
                        print("El dato es valido")

                else:
                    raise Exception("El dato no cumple con el estandar establecido")
                


            if not Clientes.get("linea_direccion2"):
                direccion2=input("Ingresa la segunda direccion del cliente: ")
                if(re.match(r'\w+',direccion2)is not None):
                    Data=getcli.getDireccion2(direccion2)
                    if(Data):
                        print(tabulate(Data, headers="keys",tablefmt="grid"))
                        raise Exception("La dirección ya existe")
                        #break #solo para el ultimo modulo sino se rompe
                    else:
                        Clientes["linea_direccion2"]=direccion2
                        print("El dato es valido")

                else:
                    raise Exception("El dato no cumple con el estandar establecido")


            # expresion regular que tenga en cuenta una palabra con mayuscula al principio,o  que pueda ser toda mayuscula, o que pueda tener un guion, que puedan ser varias palabras, que pueda tener numeros ni caracteres especiales
            if not Clientes.get("ciudad"):
                ciudad =input("Ingresa la ciudad del cliente: ")
                if(re.match(r'^([A-ZÁÉÍÓÚÜ][a-záéíóúü]*-?)+[A-ZÁÉÍÓÚÜ]?[a-záéíóúü]*$',ciudad)is not None):
                    Clientes["ciudad"]=ciudad
                    print("El dato es valido")
                    #break #solo para el ultimo modulo sino se rompe
                else:
                    raise Exception("El dato no cumple con el estandar establecido")



            if not Clientes.get("pais"):
                pais =input("Ingresa el país del cliente: ")
                if(re.match(r'^([A-ZÁÉÍÓÚÜ][a-záéíóúü]*-?)+[A-ZÁÉÍÓÚÜ]?[a-záéíóúü]*$',pais)is not None):
                    Clientes["pais"]=pais
                    print("El dato es valido")
                    #break #solo para el ultimo modulo sino se rompe
                else:
                    raise Exception("El dato no cumple con el estandar establecido")



            if not Clientes.get("region"):
                region =input("Ingresa la región del cliente: ")
                if(re.match(r'^([A-ZÁÉÍÓÚÜ][a-záéíóúü]*-?)+[A-ZÁÉÍÓÚÜ]?[a-záéíóúü]*$',region)is not None):
                    Clientes["region"]=region
                    print("El dato es valido")
                    # break #solo para el ultimo modulo sino se rompe
                else:
                    raise Exception("El dato no cumple con el estandar establecido")



            #expresion regular que tenga en cuenta la escritura de numeros solamente, o que escriba unas letras(obligatorio en mayuscula) junto con numeros separados por un espacio, o que pueda ser un numero seguido de un guión y luego más numeros todo pegado
            if not Clientes.get("codigo_postal"):
                codigoPostal =input("Ingresa el código postal del cliente(00000): ")
                if(re.match(r'^\d{5}$',codigoPostal)is not None):
                    Clientes["codigo_postal"]=codigoPostal
                    print("El dato es valido")
                    #break #solo para el ultimo modulo sino se rompe
                else:
                    raise Exception("El dato no cumple con el estandar establecido")


            # expresion regular que tenga en cuenta la escritura de un numero 
            if not Clientes.get("codigo_empleado_rep_ventas"):
                codigoEmpleado =input("Ingresa el código del representante de ventas del cliente: ")
                if(re.match(r'^\d+$',codigoEmpleado)is not None):
                    codigoEmpleado=int(codigoEmpleado)
                    Clientes["codigo_empleado_rep_ventas"]=codigoEmpleado
                    print("El dato es valido")
                    #break #solo para el ultimo modulo sino se rompe
                else:
                    raise Exception("El dato no cumple con el estandar establecido")


            # expresion regular que tenga en cuenta la escritura de un numero 
            if not Clientes.get("limite_credito"):
                limiteCredito =input("Ingresa el límite de crédito del cliente: ")
                if(re.match(r'^\d+$',limiteCredito)is not None):
                    limiteCredito=float(limiteCredito)
                    Clientes["limite_credito"]=limiteCredito
                    print("El dato es valido")
                    break #solo para el ultimo modulo sino se rompe
                else:
                    raise Exception("El dato no cumple con el estandar establecido")



        except Exception as error:
            print(error)
   

    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post("http://154.38.171.54:5001/cliente",headers=headers, data=json.dumps(Clientes, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]



#if(__name__ == "__main__"):
#    with open("storage/cliente.json", "r") as f:
#        fichero = f.read()
#        data = json.loads(fichero)
#        for i, val in enumerate(data):
#            data[i]["id"] = (i+1)
#        data=json.dumps(data, indent=4).encode("utf-8")
#        with open("storage/cliente.json", "wb+") as f1:
#                f1.write(data)
#                f1.close()



def deletecliente(id):
    data = getcli.getClienteId(id)
    if(len(data)):
        peticion = requests.delete(f"http://154.38.171.54:5001/cliente/{id}")
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

#    return [res]



def menu():
  while True:
    os.system("clear")
    print("""

    ___       __          _       _      __                     ____        __                
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______   / __ \____ _/ /_____  _____    
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/  / / / / __ `/ __/ __ \/ ___/    
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /     / /_/ / /_/ / /_/ /_/ (__  )     
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/_    /_____/\__,_/\__/\____/____/      
  ____/ /__     / /___  _____   / ____/ (_)__  ____  / /____  _____                           
 / __  / _ \   / / __ \/ ___/  / /   / / / _ \/ __ \/ __/ _ \/ ___/                           
/ /_/ /  __/  / / /_/ (__  )  / /___/ / /  __/ / / / /_/  __(__  )                            
\__,_/\___/  /_/\____/____/   \____/_/_/\___/_/ /_/\__/\___/____/                             
                                                                                              


                                 1. Guardar un nuevo cliente
                                 2. Eliminar algun cliente
                                 3. Actualizar datos de clientes
                                 0. Salir
""")
    try:
        opcion= int(input("\nSeleccione una de las opciones: "))
        if(opcion == 1):
            print(tabulate(agregarDatosDeClientes(), headers="keys", tablefmt="github"))
            input("Presione alguna tecla para continuar... ")

        elif(opcion == 2):
            idCliente = input(("Ingrese el id del cliente que deseas eliminar: "))
            print(tabulate(deletecliente(idCliente)["body"], headers="keys", tablefmt="github"))

        elif(opcion == 3):
            
            upCli.menu()

        elif(opcion==0):
            break
        else:
            print("Elija una opcion correcta: ")
    except ValueError:
        print("Seleccione una opcion valida del 0 al 3")
        time.sleep(3)

