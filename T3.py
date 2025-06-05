#OPERACIONES ARITMETICAS
#JACOUT 28 DE AGOSTO 2023
#CAPTURANDO, USANDO INPUT Y CONVERSIONES DE TIPO NECESARIAS

a=str(input("Ingresa lo que deesee"))
b=str(input("Ingresa lo que deesee (2)"))
c=int(input("Ingresa un numero"))
d=int(input("Ingresa otro numero"))
e=float(input("Ingresa un numero con decimal"))
f=float(input("Ingresa otro numero con decimal"))


#a y b
print("a y b")
#Un if por si el dato no es entero no haga las operaciones
if(a is int and b is int):
 sumaAB=a+b
 restaAB=a-b
 multiAB=a*b
 diviAB=a/b
 divisAB=a//b
 expoAB=a**b
 moddAB=a%b

 print("La suma es de: " ,sumaAB)
 print("La resta es de: ", restaAB)
 print("La multiplicacion es de: " ,multiAB)
 print("La division es de: ", diviAB)
 print("La division sin residuo es de: " ,divisAB)
 print("El exponente es de: ", expoAB)
 print("El residuo es de: ", moddAB)

else:
    print("El tipo de dato no se puede realizar operaciones")

print("c y d")
sumaCD=c+d
restaCD=c-d
multiCD=c*d
diviCD=c/d
divisCD=c//d
expoCD=c**d
moddCD=c%d


print("La suma es de: " ,sumaCD)
print("La resta es de: ", restaCD)
print("La multiplicacion es de: " ,multiCD)
print("La division es de: ", diviCD)
print("La division sin residuo es de: " ,divisCD)
print("El exponente es de: ", expoCD)
print("El residuo es de: ", moddCD)



#e y f
print("e y f")
sumaEF=e+f
restaEF=e-f
multiEF=e*f
diviEF=e/f
divisEF=e//f
expoEF=e**f
moddEF=e%f


print("La suma es de: " ,sumaEF)
print("La resta es de: ", restaEF)
print("La multiplicacion es de: " ,multiEF)
print("La division es de: ", diviEF)
print("La division sin residuo es de: " ,divisEF)
print("El exponente es de: ", expoEF)
print("El residuo es de: ", moddEF)




#a y c
print("a y c")
if(a is int and c is float):
 sumaAC=a+c
 restaAC=a-c
 multiAC=a*c
 diviAC=a/c
 divisAC=a//c
 expoAC=a**c
 moddAC=a%c

 print("La suma es de: " ,sumaAC)
 print("La resta es de: ", restaAC)
 print("La multiplicacion es de: " ,multiAC)
 print("La division es de: ", diviAC)
 print("La division sin residuo es de: " ,divisAC)
 print("El exponente es de: ", expoAC)
 print("El residuo es de: ", moddAC)

else:
    print("El tipo de dato no se puede realizar operaciones")

#c y e
print("e y c")
sumaEC=e+c
restaEC=e-c
multiEC=e*c
diviEC=e/c
divisEC=e//c
expoEC=e**c
moddEC=e%c


print("La suma es de: " ,sumaEC)
print("La resta es de: ", restaEC)
print("La multiplicacion es de: " ,multiEC)
print("La division es de: ", diviEC)
print("La division sin residuo es de: " ,divisEC)
print("El exponente es de: ", expoEC)
print("El residuo es de: ", moddEC)