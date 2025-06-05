import random
import time
 
def insertionSort(L): 
    for i in range(1, len(L),1): #Empezamos en 1
        key = L[i]
        j = i-1
        while j >= 0 and key < L[j] :
            L[j + 1] = L[j] 
            j -= 1     
        L[j + 1] = key
##        print (L)

def bubblesort(L):
    for i in range (len(L)):
        for j in range (0,len(L)-i-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j] #Intercambio

def mergeSort(L): 
    if len(L) >1: 
        mid = len(L)//2 #mid es la mitad del arreglo
        I = L[:mid] # Usamos splice (I - Izquierda)
        D = L[mid:] # Segunda parte del arreglo (D - Derecha)

        mergeSort(I) 
        mergeSort(D) 

        i = j = k = 0

        while i < len(I) and j < len(D): 
            if I[i] < D[j]: 
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






        
def arreglo(num):
    for x in range (num):
        L.append(random.randrange(100,0,-1))
    return L

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

                ip = partition(L,low,high) 


                quickSort(L, low, ip-1) 
                quickSort(L, ip+1, high)


L = []
num = int (input("Escribe un número entero"))
L = arreglo(num)

start_time = time.time()
bubblesort(L) 
print("Tiempo de Bubble Sort", (time.time() - start_time))
L.clear()
L = arreglo(num)


start_time = time.time()
insertionSort(L) 
print("Tiempo de Insertion Sort", (time.time() - start_time))
L.clear()
L = arreglo(num)

start_time = time.time()
n = len(L)
quickSort(L,0,n-1)
print("Tiempo de Quick Sort", (time.time() - start_time))
print (L)
L.clear()
L = arreglo(num)



start_time = time.time()
mergeSort(L) 
print("Tiempo de Merge Sort", (time.time() - start_time))
L.clear()
L = arreglo(num)




