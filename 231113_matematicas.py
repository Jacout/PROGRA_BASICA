from fractions import Fraction
#return la fraccion 11/35
print(Fraction(3,5))
#return la fraccion 1/2 recibiendo una cadena
print(Fraction('1/2'))

#definir las fracciones
fraccionA = Fraction("3/5")
fraccionB = Fraction("1/2")
#suma
fraccion = fraccionA + fraccionB
print("Suma", fraccion)
#resta
fraccion = fraccionA - fraccionB
print("Resta", fraccion)

#notacion cientifica
print("\nNotacion cientifica")
g = 6.673e-11
print(g)
m_tierra = 1.989e30
m_luna = 5.972e24
distancia = 1.496e11

fuerza = g * m_tierra * m_luna / (distancia**2)

print(fuerza)

#Sistemas Numericos

try: #atrapa los posibles programas con el try except (catch pa la raza)
  numero = input("Introduce un número:\n")
  sistema = int(input("Introduce un sistema de conversión:\n"))
  print(int(numero,sistema))
except:
  print("Error en la conversion")


import cmath
#Numeros complejos
a = 1 + 3j #asi se puede crear un numero complejo
print(a.real) #1.0
print(a.imag) #3.0
#Suma
b = 4 + 1j
print(a+b) #(5+4j)

print(cmath.phase(complex(5,0))) #de esta forma tambien se crear numeros complejos
print(cmath.polar(complex(5,5)))
