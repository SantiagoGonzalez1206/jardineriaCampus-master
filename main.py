import os
from tabulate import tabulate 
import sys

import modules.getEmpleado as Repempleado
import modules.postEmpleado as CRUDempleado

import modules.getClientes as Repclientes
import modules.postClientes as CRUDclientes

import modules.getOficina as Repoficina
import modules.postOficina as CRUDoficina

import modules.getPedido as Reppedido
import modules.postPedido as CRUDpedido

import modules.getPago as Reppago
import modules.postPago as CRUDpago

import modules.getProducto as Repproducto
import modules.postProducto as CRUDproducto

import modules.getGamas as gama_producto




#PUNTOS PAGINA

   #1 punto
#print(tabulate(oficina.getCodigoOfiCiudadName(), tablefmt="grid"))

   #2 punto
#print(tabulate(oficina.getCiudadTelefonoEspaña(), tablefmt="grid"))

   #3 punto
#print(tabulate(empleado.getNombreApellidoEmailJefe(), tablefmt="grid"))

   #4 punto
#print(tabulate(empleado.getAllJefesCode(), tablefmt="grid"))

   #5 punto
#print(tabulate(empleado.getEmpleadosPuesto(), tablefmt="grid"))

   #6 punto
#print(tabulate(clientes.getNombreClientesEspaña(), tablefmt="grid"))

   #7 punto
#print(tabulate(pedido.getEstadoPedido(), tablefmt="grid"))

   #8 punto
#print(pago.getFechaPago())

   #9 punto
#print(tabulate(pedido.getAllPedidosEntregadosAtrasados(), tablefmt="grid"))

   #10 punto
#print(tabulate(pedido.getPedidosDosDias(), tablefmt="grid"))

   #11 punto
#print(tabulate(pedido.getRechazos2009(), tablefmt="grid"))

   #12 punto
#print(tabulate(pedido.getEntregadosEnero(), tablefmt="grid"))

   #13 punto
#print(tabulate(pago.getPagoPaypal(), tablefmt="grid"))

   #14 punto 
#print(tabulate(pago.getFormaDePago))

   #16 punto
# print(tabulate(clientes.getClienteCiudadMadrid1130()))

   #EJERCICIOS PRACTICA

   #Todos los nombres de los empleados
#print(tabulate(empleado.getAllEmpleadosName(), tablefmt="grid"))

   #Filtrar la informacion por el codigo de jefe correspondiente
#print(tabulate(empleado.getAllEmpleado(15)))

   #La informacion del nombre de la persona 
#print(tabulate(empleado.getOneEmpleadoNombreApellidos("Ruben")))

   #Con el codigo del empleado y opcional el nombre muestra la informacion
#print(tabulate(empleado.getOneEmpleadoCodeNombre(17)))

   #Filtrar la informacion por el codigo de jefe correspondiente
#print(tabulate(empleado.getAllEmpleadosCode(15)))

   #Muestra toda la información de las personas que no son representante de ventas
#print(tabulate(empleado.getOneEmpleadoExtension("Representante Ventas")))



def menuOficina():
   while True:
      os.system("clear")
      print("""
            


    ____  _                            _     __               __     
   / __ )(_)__  ____ _   _____  ____  (_)___/ /___     ____ _/ /     
  / __  / / _ \/ __ \ | / / _ \/ __ \/ / __  / __ \   / __ `/ /      
 / /_/ / /  __/ / / / |/ /  __/ / / / / /_/ / /_/ /  / /_/ / /       
/_____/_/\___/_/ /_/|___/\___/_/ /_/_/\__,_/\____/   \__,_/_/        
                           __     ____  _____      _                 
   ____ ___  ___  ____  __/_/_   / __ \/ __(_)____(_)___  ____ ______
  / __ `__ \/ _ \/ __ \/ / / /  / / / / /_/ / ___/ / __ \/ __ `/ ___/
 / / / / / /  __/ / / / /_/ /  / /_/ / __/ / /__/ / / / / /_/ (__  ) 
/_/ /_/ /_/\___/_/ /_/\__,_/   \____/_/ /_/\___/_/_/ /_/\__,_/____/  
                                                                     
            
   
                                                                        


            1. Reportes de las oficinas
            2. Guardar, Actualizar y Eliminar oficinas
            0. Regresar al menu principal                                                               

      """)

      option = int(input("\nSeleccione una de las opciones: "))

      if(option == 1):
         Repoficina.menu()
      elif(option == 2):
         CRUDoficina.menu()
      elif(option == 0):
         break




def menuCliente():
   while True:
      os.system("clear")
      print("""
            

    ____  _                            _     __                    __   
   / __ )(_)__  ____ _   _____  ____  (_)___/ /___  _____   ____ _/ /   
  / __  / / _ \/ __ \ | / / _ \/ __ \/ / __  / __ \/ ___/  / __ `/ /    
 / /_/ / /  __/ / / / |/ /  __/ / / / / /_/ / /_/ (__  )  / /_/ / /     
/_____/_/\___/_/ /_/|___/\___/_/ /_/_/\__,_/\____/____/   \__,_/_/      
                           __     _________            __               
   ____ ___  ___  ____  __/_/_   / ____/ (_)__  ____  / /____  _____    
  / __ `__ \/ _ \/ __ \/ / / /  / /   / / / _ \/ __ \/ __/ _ \/ ___/    
 / / / / / /  __/ / / / /_/ /  / /___/ / /  __/ / / / /_/  __(__  )     
/_/ /_/ /_/\___/_/ /_/\__,_/   \____/_/_/\___/_/ /_/\__/\___/____/      
                                                                        


            1. Reportes de los clientes
            2. Guardar, Actualizar y Eliminar clientes
            0. Regresar al menu principal                                                               

      """)

      option = int(input("\nSeleccione una de las opciones: "))

      if(option == 1):
         Repclientes.menu()
      elif(option == 2):
         CRUDclientes.menu()
      elif(option == 0):
         break




def menuProducto():
   while True:
      os.system("clear")
      print("""
            
    ____  _                            _     __               __                          __     
   / __ )(_)__  ____ _   _____  ____  (_)___/ /___     ____ _/ /  ____ ___  ___  ____  __/_/_    
  / __  / / _ \/ __ \ | / / _ \/ __ \/ / __  / __ \   / __ `/ /  / __ `__ \/ _ \/ __ \/ / / /    
 / /_/ / /  __/ / / / |/ /  __/ / / / / /_/ / /_/ /  / /_/ / /  / / / / / /  __/ / / / /_/ /     
/_____/_/\___/_/ /_/|___/\___/_/ /_/_/\__,_/\____/   \__,_/_/  /_/ /_/ /_/\___/_/ /_/\__,_/      
   / __ \_________  ____/ /_  _______/ /_____  _____                                             
  / /_/ / ___/ __ \/ __  / / / / ___/ __/ __ \/ ___/                                             
 / ____/ /  / /_/ / /_/ / /_/ / /__/ /_/ /_/ (__  )                                              
/_/   /_/   \____/\__,_/\__,_/\___/\__/\____/____/                                               


            1. Reportes de los productos
            2. Guardar, Actualizar y Eliminar productos
            0. Regresar al menu principal                                                               

      """)

      option = int(input("\nSeleccione una de las opciones: "))

      if(option == 1):
         Repproducto.menu()
      elif(option == 2):
         CRUDproducto.menu()
      elif(option == 0):
         break


def menuEmpleado():
   while True:
      os.system("clear")
      print("""

            
    ____  _                            _     __               __                     
   / __ )(_)__  ____ _   _____  ____  (_)___/ /___     ____ _/ /                     
  / __  / / _ \/ __ \ | / / _ \/ __ \/ / __  / __ \   / __ `/ /                      
 / /_/ / /  __/ / / / |/ /  __/ / / / / /_/ / /_/ /  / /_/ / /                       
/_____/_/\___/_/ /_/|___/\___/_/ /_/_/\__,_/\____/   \__,_/_/                        
                           __     ______                __               __          
   ____ ___  ___  ____  __/_/_   / ____/___ ___  ____  / /__  ____ _____/ /___  _____
  / __ `__ \/ _ \/ __ \/ / / /  / __/ / __ `__ \/ __ \/ / _ \/ __ `/ __  / __ \/ ___/
 / / / / / /  __/ / / / /_/ /  / /___/ / / / / / /_/ / /  __/ /_/ / /_/ / /_/ (__  ) 
/_/ /_/ /_/\___/_/ /_/\__,_/  /_____/_/ /_/ /_/ .___/_/\___/\__,_/\__,_/\____/____/  
                                             /_/                                     
                                          


            1. Reportes de los empleados
            2. Guardar, Actualizar y Eliminar empleados
            0. Regresar al menu principal                                                               

      """)

      option = int(input("\nSeleccione una de las opciones: "))

      if(option == 1):
         Repempleado.menu()
      elif(option == 2):
         CRUDempleado.menu()
      elif(option == 0):
         break


def menuPago():
   while True:
      os.system("clear")
      print("""
            


    ____  _                            _     __               __   
   / __ )(_)__  ____ _   _____  ____  (_)___/ /___     ____ _/ /   
  / __  / / _ \/ __ \ | / / _ \/ __ \/ / __  / __ \   / __ `/ /    
 / /_/ / /  __/ / / / |/ /  __/ / / / / /_/ / /_/ /  / /_/ / /     
/_____/_/\___/_/ /_/|___/\___/_/ /_/_/\__,_/\____/   \__,_/_/      
   ____ ___  ___  ____  __/_/_   / __ \____ _____ _____            
  / __ `__ \/ _ \/ __ \/ / / /  / /_/ / __ `/ __ `/ __ \           
 / / / / / /  __/ / / / /_/ /  / ____/ /_/ / /_/ / /_/ /           
/_/ /_/ /_/\___/_/ /_/\__,_/  /_/    \__,_/\__, /\____/            
                                          /____/                   
   


            1. Reportes de los clientes
            2. Guardar, Actualizar y Eliminar clientes
            0. Regresar al menu principal                                                               

      """)

      option = int(input("\nSeleccione una de las opciones: "))

      if(option == 1):
         Reppago.menu()
      elif(option == 2):
         CRUDpago.menu()
      elif(option == 0):
         break



def menuPedido():
   while True:
      os.system("clear")
      print("""
            


    ____  _                            _     __               __   
   / __ )(_)__  ____ _   _____  ____  (_)___/ /___     ____ _/ /   
  / __  / / _ \/ __ \ | / / _ \/ __ \/ / __  / __ \   / __ `/ /    
 / /_/ / /  __/ / / / |/ /  __/ / / / / /_/ / /_/ /  / /_/ / /     
/_____/_/\___/_/ /_/|___/\___/_/ /_/_/\__,_/\____/__ \__,_/_/      
   ____ ___  ___  ____  __/_/_   / __ \___  ____/ (_)___/ /___     
  / __ `__ \/ _ \/ __ \/ / / /  / /_/ / _ \/ __  / / __  / __ \    
 / / / / / /  __/ / / / /_/ /  / ____/  __/ /_/ / / /_/ / /_/ /    
/_/ /_/ /_/\___/_/ /_/\__,_/  /_/    \___/\__,_/_/\__,_/\____/     
                                                                   



            1. Reportes de los pedidos
            2. Guardar, Actualizar y Eliminar pedidos
            0. Regresar al menu principal                                                               

      """)

      option = int(input("\nSeleccione una de las opciones: "))

      if(option == 1):
         Reppedido.menu()
      elif(option == 2):
         CRUDpedido.menu()
      elif(option == 0):
         break






if(__name__ == "__main__"):
   while True:
      os.system("clear")
      print("""


___  ___                  ______     _            _             _ 
|  \/  |                  | ___ \   (_)          (_)           | |
| .  . | ___ _ __  _   _  | |_/ / __ _ _ __   ___ _ _ __   __ _| |
| |\/| |/ _ \ '_ \| | | | |  __/ '__| | '_ \ / __| | '_ \ / _` | |
| |  | |  __/ | | | |_| | | |  | |  | | | | | (__| | |_) | (_) | |
\_|  |_/\___|_| |_|\__,_| \_|  |_|  |_|_| |_|\___|_| .__/ \__,_|_|
                                                   | |            
                                                   |_|            

        1. Oficina
        2. Cliente
        3. Producto
        4. Empleado
        5. Pago
        6. Pedido
        0. Salir 

               """)

      option = int(input("\nSeleccione una de las opciones: "))

      if(option == 1):
         menuOficina()
      elif(option == 2):
         menuCliente()       
      elif(option == 3):
         menuProducto()
      elif(option == 4):
         menuEmpleado()         
      elif(option == 5):
         menuPago() 
      elif(option == 6):
         menuPedido()
      elif(option == 0):
         break
      else:
         print("elija una opcion valida")


        # https://patorjk.com/software/taag/#p=display&h=2&v=2&f=Slant&t=Menu%20Principal
         
      #json-server storage/oficina.json -b 5501 & json-server storage/cliente.json -b 5502 & json-server storage/producto.json -b 5503 & json-server storage/empleado.json -b 5504 & json-server storage/pago.json -b 5505 & json-server storage/pedido.json -b 5506