#grafica de pastel con pie

from matplotlib.collections import PolyCollection
import matplotlib.pyplot as plt
import numpy as np


y = np.array([100,70,60,80])
morras = ["Elo","Dani","Lic","La de la 16"]


plt.pie(y,labels = morras)
plt.savefig("Morritas.png")
plt.show()


#destacar una seccion
myexplode = [0,0,0.2,2]
plt.pie(y,labels = morras, explode = myexplode)
plt.show()

#colores
colores = ["#ceff25", "#EE34F1", "b","#4CAF50"]
plt.pie(y,labels = morras, colors = colores)
plt.show()


#Leyenda
plt.pie(y, labels = morras)
plt.legend()
plt.show()

#leyenda con titulo

plt.pie(y,labels =morras)
plt.legend("ELOV")
plt.show()

#TAMAÑO DEFAULT 6
x_number = [1,2,3]
y_number = [2,4,6]
figure(figsize=[3,3], facecolor="blue")
#Estilos predefinidos
print(style.avaible)
style.use('ggplot')
pl(x_number,y_number)
plt.show()

# Un array es una estructura de datos que almacena una colección de elementos, típicamente del mismo tipo