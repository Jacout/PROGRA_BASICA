#numpy con matplotlib
import matplotlib.pyplot as plt
import numpy as np


x1 = np.array([0,1,2,3])
y1 = np.array([3,8,1,10])
x2 = np.array([0,1,2,3])
y2 = np.array([6,2,7,11])

plt.plot(x1,y1,x2,y2)
plt.show()


#manejo de etiquetas
from pylab import plot,show
from pylab import legend #Para identificar cada conjutno de datos
from pylab import xlabel,ylabel #Para las etiquetas de los ejes
from pylab import title #Para el titulo de la grafica
from pylab import axis #Para los rangos de los ejes

legend([2000,2006,2012])
title("Temperatura promedio en NYC")
xlabel("Mes")
ylabel("Temperatura (K)")
#axis (ymin=0,ymax=100, xmin=1, xmas=12) pueden usarse como rangos maximos y minimos
show()


nyc_temp_2000 = [31.3,37.3,47.2,51.0,63.5,43,300,150,12,24.3,43,23]
nyc_temp_2006 = [44.5,47.5,32.4,20.2,10.2,8.2,-100,150,12,24.3,43,23]
nyc_temp_2012 = [51.7,56.3,60.9,66.6,70.3,51.7,300,150,12,24.3,43,23]

#creamos una lista de meses
meses = range(1,13)
#a continuacion llamamos a la funcion plot

plot(meses,nyc_temp_2000,meses,nyc_temp_2006,meses,nyc_temp_2012,marker="D")
legend([2000,2006,2012])
title("Temperatura promedio en NYC")
xlabel("Mes")
ylabel("Temperatura (K)")
show()



#FUNCION SCATTER dibuja un driagrama de dispersion puntitoa

x = np.array([5,7,8,7,2,1])
y = np.array([99,87,55,88,111,0])

plt.scatter(x,y)
plt.show()

#se pueden comparar entre mas graficas
#dia, uno, edad y velocidad de 13 autos
x = np.array([4,2,7,44,41,6,77,7,9,1,11,12])
y = np.array([99,87,55,88,111,0,1,2,3,4,5,6])

plt.scatter(x,y,color = 'hotpink') #le cambia color a los puntitos
show()

#se puede definir el mapa de colores, se agrega con el argumento cmap
plt.scatter(x,y,cmap = 'rainbow') #mapa de colores
plt.colorbar() #agreggar el mapa de colores

show()

plt.scatter(x,y,s=500)#para modificar el tamaño del punto
show()
plt.scatter(x,y,s=100,alpha=0.6) #transparencia del punto
show()

#funcion bar() para dibujar diiagrama de barras

x = np.array(["La de la 16","Administradora","Nose","Eloy"])
y = np.array([9,8,7,10])

plt.bar(x,y,color="red") #color de la barra
xlabel("Morra")
ylabel("Calificacion")
plt.show()
plt.barh(x,y, height=0.2) #asi si es horizonta, si es bar se usa width
plt.show()


#la de pastel pie
morritas = np.array(["La de la 16","Administradora","Nose","Eloy"])
y = np.array([9,8,7,10])

plt.pie(y,labels = morritas)
plt.show()

plt.savefig('Grafica_decision_importante.png')