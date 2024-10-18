
#numero
nJuego=[]
estaturasMinimas=[]
print("Juegos")
n=input("Numero de juego - estatura")
h=input("estatura minima\n")



nJuego=n.split(" ")

estaturasMinimas=h.split(" ")
#guardar estaturas
x=0
#comparar estaturas
for a in range(int(nJuego[0])):
    if(int(estaturasMinimas[a])<=int(nJuego[1])):
        x+=1

print(x)

nJuego=[]
estaturasMinimas=[]

n=input()
h=input()



nJuego=n.split(" ")

estaturasMinimas=h.split(" ")
#guardar estaturas
x=0
#comparar estaturas
for a in range(int(nJuego[0])):
    if(int(estaturasMinimas[a])<=int(nJuego[1])):
        x+=1

print(x)


#c MONTAÑA

puntoMontania=[]
catLikes=[]
catFotos=[]
puntos=int(input())
punto=input()
like=input()

puntoMontania=punto.split(" ")
catLikes=like.split(" ")

cantFotos=1
puntoActual=int(0)
likesActual=int(catLikes[0])

for t in range(puntos-1):
    if(int(puntoMontania[t])>=puntoActual):
        if(int(catLikes[t+1])>likesActual):
            cantFotos+=1
            catFotos.append(cantFotos)
        else:
            catFotos.append(cantFotos)
    elif(int(puntoMontania[t])<=puntoActual):
        if(int(catLikes[t+1])<likesActual):
            cantFotos-=1
            catFotos.append(cantFotos)
        else:
            catFotos.append(cantFotos)
    
    else:
        catFotos.append(cantFotos)
    puntoActual=int(puntoMontania[t])
    likesActual=int(catLikes[t+1])

print()
for a in range(puntos-1):
    print(catFotos[a],end=" ")



#B PERMUTACIONES

baraja=[]

cantBara=int(input())
barajas=input()
baraja=barajas.split(" ")

print(baraja)
nFac=len(baraja)
r=4
rFact=r
nrFac=nFac-r
for n in range(nFac-1,1,-1):
    nFac=nFac*n

for n in range(nrFac-1, 1, -1):
    nrFac=nrFac*n


for n in range(r-1,1,-1):
    rFact=rFact*n


print(nFac)
print(nrFac)
print(rFact)
p=nFac/(nrFac*rFact)
print(p)


#c MONTAÑA

puntoMontania=[]
catLikes=[]
puntos=int(input())
punto=input()
like=input()

puntoMontania=punto.split(" ")
catLikes=like.split(" ")

print(puntoMontania[0])