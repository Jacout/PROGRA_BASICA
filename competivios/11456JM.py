#11456 vetor dominante, que la primera linea sea mayor que la segunda

lista1=[]
lista2=[]
n=int(input())
numeros1=input()
numeros2=input()
salida=0
valeria=0
lista1=numeros1.split(" ")
lista2=numeros2.split(" ")

for a in range(len(lista1)):
  n1=int(lista1[a])
  n2=int(lista2[a])
  if(n1>n2 and valeria==0):
    salida=1
  elif(n1<=n2):
    salida=0
    valeria=1
print(salida)