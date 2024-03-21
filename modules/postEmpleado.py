import json
import requests
import os
from tabulate import tabulate
import modules.getEmpleado as getEmp
import modules.updateEmpleado as upEmp
import re

# def postEmpleado():
#     empleado = {
#             "codigo_empleado": int(input("Ingrese el codigo de empleado: ")),
#             "nombre": input("Ingrese el nombre de empleado: "),
#             "apellido1": input("Ingrese el primer apellido del empleado: "),
#             "apellido2": input("Ingrese el segundo apellido del empleado: "),
#             "extension": input("Ingrese la extension del empleado: "),
#             "email": input("Ingrese el email del empleado: "),
#             "codigo_oficina": input("Ingrese el codigo de oficina del empleado: "),
#             "codigo_jefe": int(input("Ingrese el codigo del jefe del empleado: ")),
#             "puesto": input("Ingrese el puesto asignado al empleado: "),
#         }
   
   
#      # json-server storage/empleado.json -b 5504
#     peticion = requests.post("http://154.38.171.54:5003/empleados", data = json.dumps(empleado, indent =4).encode("UTF-8"))
#     res=peticion.json()
#     res["mensaje"] = "Producto Guardado"
#     return [res]


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



def agregarDatosEmpleados():
    empleados={}
    while True:
        try:


            # 

            if not empleados.get("codigo_cliente"):
                codigo=input("Ingresa el codigo del empleados: ")
                if (re.match(r'^\d+$',codigo)is not None):
                    codigo= int(codigo)
                    Data=getEmp.getEmpleadoCodigoCliente(codigo)
                    if(Data):
                        print(tabulate(Data, headers="keys",tablefmt="grid"))
                        raise Exception("El código ya existe")
                    
                else:
                    empleados["codigo_cliente"]=codigo
                    print("El dato cumple con el estandar, OK")






            

            if not empleados.get("nombre"):
                nombre=input("Ingresa un nombre del empleados: ")
                if(re.match(r'\w+',nombre)is not None):
                    empleados["nombre"]=nombre
                    print("El dato cumple con el estandar,OK")
                    
                


            

            if not empleados.get("apellido1"):
                apellido1 =input("Ingresa el primer apellido del empleados(ejemplo: Alberto): ")
                if(re.match(r'^[A-ZÁÉÍÓÚÜÑ][a-záéíóúüñ]*$',apellido1)is not None):
                    empleados["apellido1"]=apellido1
                    print("El dato cumple con el estandar,OK")
                    
            else:
                raise Exception("El dato no cumple con el estandar establecido")      





            if not empleados.get("apellido2"):
                apellido2 =input("Ingresa el segundo apellido del empleados(ejemplo: Suarez): ")
                if(re.match(r'^[A-ZÁÉÍÓÚÜÑ][a-záéíóúüñ]*$',apellido2)is not None):
                    empleados["apellido2"]=apellido2
                    print("El dato cumple con el estandar,OK")
                    
            else:
                raise Exception("El dato no cumple con el estandar establecido")      





            #
            if not empleados.get("extension"):
                extension =input("Ingresa la extension del empleado(0000): ")
                if(re.match(r'^\d{4}$',extension)is not None):
                    empleados["extension"]=extension
                    print("El dato cumple con el estandar,OK")
                    
                else:
                    raise Exception("El dato no cumple con el estandar establecido")


            
                
            if not empleados.get("email"):
                email=input("Ingresa el email del empleado: ")
                if(re.match(r'^[\s\S]*$',email)is not None):
                    Data=getEmp.getEmailEmpleado(email)
                    if(Data):
                        print(tabulate(Data, headers="keys",tablefmt="grid"))
                        raise Exception("El email de la oficina ya existe")
                        
                    else:
                        empleados["email"]=email
                        print("El dato cumple con el estandar,OK")

                else:
                    raise Exception("El dato no cumple con el estandar establecido")



            
            if not empleados.get("codigo_oficina"):
                oficina =input("Ingresa el código de la oficina(AAA-AAA): ")
                if(re.match(r'^[A-Z]+-[A-Z]+$',oficina)is not None):
                    empleados["codigo_oficina"]=oficina
                    print("El dato cumple con el estandar,OK")
                   
                else:
                    raise Exception("El dato no cumple con el estandar establecido")



           
            if not empleados.get("codigo_jefe"):
                jefe =input("Ingresa el código del jefe del empleado: ")
                if(re.match(r'^\d+$',jefe)is not None):
                    empleados["codigo_jefe"]=jefe
                    print("El dato cumple con el estandar,OK")
                    
                else:
                    raise Exception("El dato no cumple con el estandar establecido")



            if not empleados.get("puesto"):
                puesto=input("Ingresa el puesto del empleado(ejemplo: Representante Ventas): ")
                if(re.match(r'^[A-Z][a-z]*( [A-Z][a-z]*)*$',puesto)is not None):
                    print(tabulate(Data, headers="keys",tablefmt="grid"))
                    empleados["puesto"]=puesto
                    print("El dato cumple con el estandar,OK")
                    break 
            else:
                raise Exception("El dato no cumple con el estandar establecido")



        except Exception as error:
            print(error)


    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post("http://154.38.171.54:5003/empleados",headers=headers, data=json.dumps(empleados, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]




def deleteempleado(id):
    data = getEmp.getEmpleadoId(id)
    if(len(data)):
        peticion= requests.delete(f"http://154.38.171.54:5003/empleados/{id}")
        if(peticion.status_code == 204):
            data.append({"message": "empleado eliminado correctamente"})
            return{
                "body" : data,
                "status": peticion.status_code
            }
        
        else:
            return{
                "body": [{
                    "mesagge": "cliente no encontrado",
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
                                 
            

                                 1. Guardar un nuevo empleado
                                 2. Eliminar algun empleado
                                 0. Salir
""")

    opcion= int(input("\nSeleccione una de las opciones: "))
    if(opcion == 1):
        print(tabulate(agregarDatosEmpleados(), headers="keys", tablefmt="github"))
        input("Presione Enter para continuar... ")
    elif(opcion == 2):
        idEmpleado = input(("Ingrese el id del cliente que deseas eliminar: "))
        print(tabulate(deleteempleado(idEmpleado)["body"], headers="keys", tablefmt="github"))

    elif(opcion == 3):
        
        upEmp.menu()

    elif(opcion==0):
       break
    else:
       print("Elija una opcion correcta: ")
