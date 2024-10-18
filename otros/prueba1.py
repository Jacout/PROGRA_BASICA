#ejemplo de edad mayoria de edad

edad=int(input("Hola, escribe tu edad \n"))

if (edad>=18):
  print("No eres cp")
  print("Naciste en el año: ",str(2023-edad))
elif(edad<18 and edad>0):
  print("Eres cp")

else:
  print("No existes pa")

