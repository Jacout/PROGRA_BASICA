import random
import time
def partition(L,low,high): 
        i = ( low-1 )		# índice del elemento más pequeño
        pivot = L[high]	        # pivote

        for j in range(low , high): 

		# Si el elemento actual es más pequeño que el pivote
                if L[j] < pivot: 
		
			# incrementa el índice del elemento más pequeño
                        i = i+1
                        L[i],L[j] = L[j],L[i] 

        L[i+1],L[high] = L[high],L[i+1] 
        return ( i+1 ) 

def quickSort(L,low,high): 
        if low < high: 

		# ip es el indice de particion
		# L[p] ahora está en un lugar correcto 
                ip = partition(L,low,high) 


                # Ordena los elementos antes y despues de la particion
                quickSort(L, low, ip-1) 
                quickSort(L, ip+1, high) 


##Implementación
L = []
num = int (input("Escribe un número entero"))
for x in range (num):
        L.append(random.randrange(100,0,-1))

n = len(L)
quickSort(L,0,n-1) 
print ("Arreglo ordenado") 
print (L)
