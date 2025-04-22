"""
Jacob Misael Rodríguez Morales 1907926
Jahir Eduardo Alday Encinia 1974475
H diccionario de clientes 5 de octubre
"""


dataCliente=dict()
x = 1
while(x==1):
  print("Que opcion requiere realizar")
  print("\n1.Alta\n2.Eliminar\n3.Consultar")
  print("\n4.Reporte\n5.Reporte Clte preferente\n6. Salir")
  op = int(input())
  if(op==1):
    claveC = input("Ingrese la clave a asignar\n")
    nom = input("Ingrese el nombre del cliente\n")
    dir = input("Ingrese la direccion del cliente\n")
    tel = input("Ingrese el telefono del cliente\n")
    corr = input("Ingrese el correo del cliente\n")
    pref = input("Cliente preferencia 1.Si, 2.No\n")
    
 

