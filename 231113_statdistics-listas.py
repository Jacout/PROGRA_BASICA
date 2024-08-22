from statistics import mean
from fractions import Fraction as F
from decimal import Decimal as D
import random

from statistics import mode #importar solamente mode

#se declara 4 listas vacias
listaInt = list()
listaFloat = list()
listaDec = list()
listaFrac = list()
for i in range(5): #que se rellenan 5 veces con numeros aleatorios a cada lista
  listaInt.append(random.randint(1,100))
  listaFloat.append(random.uniform(1,100))
  var = str(random.random()+random.randint(0,10))
  var = var [:5]
  listaDec.append(D(var))
  listaFrac.append(F(random.randint(1,10),random.randint(1,10)))


print(listaInt, "Media", mean(listaInt)) #mean se usa para obtener la media de una lista solo jala con listas nota
print("\n")
print(listaFloat, "Media", mean(listaFloat))
print("\n")
print(listaDec, "Media", mean(listaDec))
print("\n")
print(listaFrac, "Media", mean(listaFrac))


#obtener cuantas veces se repite

calificaciones = list()
for e in range(250):
  calificaciones.append(random.randint(0,100))

print(calificaciones)
print("La calificiacion que mas se repirte es: ", mode(calificaciones)) #con mode se obtiene en base a una lista cuantas veces se repite