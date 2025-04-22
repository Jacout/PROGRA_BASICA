#15318 enteros con pares, 
#primera linea lista de arreglo hechote mai
arreglo=[]


n=int(input())
numeros=input()
de=int(input())

arreglo=numeros.split()

if(de==1):
  for a in range(len(arreglo)):
    residuo=int(arreglo[a])%2
    if(residuo!=0):
      print(arreglo[a], end=" ")
if(de==0):
  for a in range(len(arreglo)):
    residuo=int(arreglo[a])%2
    if(residuo==0):
      print(arreglo[a], end=" ")