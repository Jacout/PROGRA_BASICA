#clase 30 de agosto

listaAbril=list(range(1,10))
print(listaAbril)

listaAbril.sort(reverse=True) #ordena de mayor a menor la lista
print(listaAbril)

del listaAbril[4]  #elimina un valor en base a la posicion

print(listaAbril)

del listaAbril[2:4] #elimina dentro de un rango de posiciones
print(listaAbril)

del listaAbril[:3] #Elimina desde la primera posicion hasta la ultima
print(listaAbril)

del listaAbril [1:] #elimina desde una posicion hasta el final
print(listaAbril)

del listaAbril[:] #Elimina todo
print(listaAbril)

del listaAbril # Borra la variable
print(listaAbril)