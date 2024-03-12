import os
from tabulate import tabulate 
import modules.getEmpleado as empleado
import modules.getClientes as clientes
import modules.getOficina as oficina
import modules.getPedido as pedido
import modules.getPago as pago
import modules.getProducto as producto
import sys


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


          
# for nombre, objeto in sys.modules.items():
#     if nombre.startswith("modules"):
#         modulo = getattr(objeto, "__name__", None)
#         if ((modulo != "modules")):
#           file = modulo.split("get")[-1]
#           print(file)
    
if(__name__ == "__main__"):
   while True:
      print("""
        
    __  ___                    ____       _            _             __
   /  |/  /__  ____  __  __   / __ \_____(_)___  _____(_)___  ____ _/ /
  / /|_/ / _ \/ __ \/ / / /  / /_/ / ___/ / __ \/ ___/ / __ \/ __ `/ / 
 / /  / /  __/ / / / /_/ /  / ____/ /  / / / / / /__/ / /_/ / /_/ / /  
/_/  /_/\___/_/ /_/\__,_/  /_/   /_/  /_/_/ /_/\___/_/ .___/\__,_/_/   
                                                    /_/                
        

        1. Cliente
        2. Oficina
        3. Empleado
        4. Pedidos
        5. Pago
        6. Producto 
        7. Salir 

               """)

      option = int(input("\nSeleccione una de las opciones: "))

      if(option == 1):
         clientes.menu()
      elif(option == 2):
         oficina.menu()
      elif(option == 3):
         empleado.menu()
      elif(option == 4):
         pedido.menu()  
      elif(option == 5):
         pago.menu()  
      elif(option == 6):
         producto.menu()
      elif(option == 7):
         break
      else:
         print("elija una opcion valida ")