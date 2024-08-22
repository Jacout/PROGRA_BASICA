from matplotlib.pyplot import colorbar
from pylab import plot, show

x_number = [1,2,3]
y_number = [2,4,6]

plot(x_number,y_number)
show() #muestra grafica


#pasar usar puntos sin linea


plot(x_number,y_number,'o:g',ms=15)
show()

#usar puntos y lineas
plot(x_number,y_number,marker='o')
show()

print("Diferentes tipos de marcadores")
#se pueden definir distintos de marcadores

nyc_temp = [53.9,56.3,56.4,52.4,54.5,55.8,54.5,55.8,56.8,55.0,55.3,54.0,56.7]
years = range(2000,2013)
plot(years,nyc_temp,marker="D",linestyle="-.") #podemos usar marcadores ya definidos y estilos de linea, buscar, tambien los colores
#se pueden poner tres valores distintos marker | line | color, ms para estalecer el tamaña del punto o marcador
show()
#para establecer el color del bor de los marcadores se usa mec o markeredgecolor
plot(years,nyc_temp,'o:g',ms=10,mec='r')

#Para establecer el color dentro del borde los marcadores markerfacecolor o mfc
plot(years,nyc_temp,'o:g',ms=10,mfc='r')
show()

#se usa linewidth para cambiar el ancho de la linea o lw
plot(years,nyc_temp,'o:g',ms=10,lw='5.5')
show()