import rectangulo #importar todo el modulo

from rectangulo import area #importar solo una funcion
x=0
while x<1:
  rectangulo.b=8 #variables
  rectangulo.a=5 
  print("Area =",rectangulo.area()) 
  rectangulo.imprimir() #funciones
  x+=1