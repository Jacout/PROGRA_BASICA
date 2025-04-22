#7676 mario con n escenarios y diferentes saltos, imprimir el escenario y numero de brinos altos y bajos

escGlobal=[]
esc=[]
escSaltos=[]
t=int(input())

for a in range(t):
  k=int(input())
  salMa=0
  salMe=0
  n=input()
  esc=n.split(" ")
  actual=int(esc[0])
  for v in range(len(esc)-1):
    sig=int(esc[v+1])
    dif=actual-sig
    if dif<0:
      salMa+=1
    elif dif>0:
      salMe+=1
    actual=int(esc[v+1])
  escSaltos.append(salMa)
  escSaltos.append(salMe)
  escGlobal.append(escSaltos)
  escSaltos=list()
#agrega la lista en la lista principal, kuego para imprimir se imprime la lista 1 en sus diferentes n posiciones hasta la k lista principal

for a in range(len(escGlobal)):
  print("Escenario",a+1, end="")
  print(":",end=" ")
  for b in range(2):
    print(escGlobal[a][b], end=" ")
  if(a!=2):
    print()
  
  
  