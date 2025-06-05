#Ejercicio de temperatura de 5 maxima y minimas

dias=["Lunes","Martes","Miercoles","Jueves","Viernes"]
diasConMenos=[]
diasBuscados=[]
temperaturasMinimas=[0,0,0,0,0]
temperaturasMaximas=[0,0,0,0,0]
promediosTemp=[0,0,0,0,0]

for a in range(5):
    print("Día ", dias[a])
    temperaturasMinimas[a]=float(input("Ingrese la temperatura minima\n"))
    temperaturasMaximas[a]=float(input("Ingrese la temperatura maxima\n"))
    promediosTemp[a]=(temperaturasMaximas[a]+temperaturasMinimas[a])/2

tempBuscada=float(input("Ingrese una temperatura maxima que quiera buscar\n"))

print("             Temperatura maxima", end="           ")
print("Temperatura minima", end="           " )
print("Temperaturas promedio")
for a in range(5):
    print(dias[a], end="   ")
    print("         ", temperaturasMaximas[a], "°C", end="          ")
    print("         ", temperaturasMinimas[a], "°C", end="          " )
    print("         ", promediosTemp[a])
#Mostrar dias de la semana y mostrar cual día maxima, promedio, mostrar días

#dias con menos temperaturas

minima=promediosTemp[0]
diasConMenos.append(dias[0])
for a in range(4):
  c=a+1
  if(minima>promediosTemp[c]):
    diasConMenos.clear()
    minima=promediosTemp[c]
    diasConMenos.append(dias[c])
  elif(minima==promediosTemp[c]):
    diasConMenos.append(dias[c])

#busca el clima especificado
for a in range(5):
  if(tempBuscada==temperaturasMaximas[a]):
    diasBuscados.append(dias[a])

print("Dia(s) con menos temperatura:", end=" ")

for a in diasConMenos:
  print(a, end="-")
print("\n Dias con la temperatura buscada:")
for a in diasBuscados:
  print(a,end="-")
#imprime los climas con menos dias
#Listo
