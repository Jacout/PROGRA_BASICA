import random
import time

def mergeSort(L): 
    if len(L) >1: 
        mid = len(L)//2 #mid es la mitad del arreglo
        I = L[:mid] # Usamos splice (I - Izquierda)
        D = L[mid:] # Segunda parte del arreglo (D - Derecha)

        mergeSort(I) #Resolvemos por merge sort la parte izquierda
        mergeSort(D) #Resolvemos por merge sort la parte derecha

        i = j = k = 0

        while i < len(I) and j < len(D): 
            if I[i] < D[j]: #Comparamos los elementos del arreglo I con el de arreglo D
                L[k] = I[i] 
                i+=1
            else: 
                L[k] = D[j] 
                j+=1
            k+=1

        while i < len(I): 
            L[k] = I[i] 
            i+=1
            k+=1
		
        while j < len(D): 
            L[k] = D[j] 
            j+=1
            k+=1


def printList(L): 
	for i in range(len(L)):		 
		print(L[i],end=" ") 
	print() 

##Implementacion
	
L = []
num = int (input("Escribe un número entero"))
for x in range (num):
    L.append(random.randrange(100))

print ( "El tiempo para ordenar un arreglo tamaño",num," por merge sort ","es:")
start_time = time.time()
mergeSort(L)
print((time.time() - start_time))
