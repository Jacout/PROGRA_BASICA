#11455 filtrando multiplos que en una secuencia y que reemplace con x el los numeros que no son multiplos de ese numero

listaA=[]
n=int(input())
numeros=input()

listaA=numeros.split()
num=int(input())

for a in range(len(listaA)):
  numeroM=int(listaA[a])
  mult=numeroM%num
  if(mult==0):
    print(listaA[a], end=" ")
  else:
    print("X", end=" ")

