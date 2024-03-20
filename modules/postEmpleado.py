import json
import requests
import os
from tabulate import tabulate
import modules.getEmpleado as getemp
import modules.updateEmpleado as upEmp

def postEmpleado():
    empleado = {
            "codigo_empleado": int(input("Ingrese el codigo de empleado: ")),
            "nombre": input("Ingrese el nombre de empleado: "),
            "apellido1": input("Ingrese el primer apellido del empleado: "),
            "apellido2": input("Ingrese el segundo apellido del empleado: "),
            "extension": input("Ingrese la extension del empleado: "),
            "email": input("Ingrese el email del empleado: "),
            "codigo_oficina": input("Ingrese el codigo de oficina del empleado: "),
            "codigo_jefe": int(input("Ingrese el codigo del jefe del empleado: ")),
            "puesto": input("Ingrese el puesto asignado al empleado: "),
        }
   
   
     # json-server storage/empleado.json -b 5504
    peticion = requests.post("http://154.38.171.54:5003/empleados", data = json.dumps(empleado, indent =4).encode("UTF-8"))
    res=peticion.json()
    res["mensaje"] = "Producto Guardado"
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

def deleteempleado(id):
    data = getemp.getEmpleadoId(id)
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
        print(tabulate(postEmpleado(), headers="keys", tablefmt="github"))
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
