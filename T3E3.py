#ECUACION CUADRATICA
##JACOUT 28 AGOSTO DE 2023
#puse un ciclo para hacer los 3 de una sola ejecucion
x=0

while(x<3):
    a=float(input("Ingresa el valor de a"))
    b=float(input("Ingresa el valor de b"))
    c=float(input("Ingresa el valor de c"))


    x1=(-(b)+(b**2-(4*a*c))**0.5)/2*a
    x2=(-(b)-(b**2-(4*a*c))**0.5)/2*a


    print("El valor de la primer raiz es de: ", x1)
    print("El valor de la segunda raiz es de: ", x2)
    print("\n")
    x+=1
