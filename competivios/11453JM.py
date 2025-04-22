#11453 producto de vectores


lista1=[]
lista2=[]
n=int(input())
numeros1=input()
numeros2=input()
producto=0
sumaVec=0
lista1=numeros1.split(" ")
lista2=numeros2.split(" ")

for a in range(len(lista1)):
  n1=int(lista1[a])
  n2=int(lista2[a])
  producto=n1*n2
  sumaVec+=producto

print(sumaVec)