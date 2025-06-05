import random
import time


##Búsqueda secuencial
def search(L, item):
    flag = 0
    for indexa in L:
        if indexa == item:
            flag = 1
            print('Position ',indexa)
            break
    if flag == 0:
        print('Not found')


##Búsqueda binaria

def binarySearch (arr, l, r, x): 
    if r >= l: 
        mid = l + (r - l) // 2
        if arr[mid] == x: 
            return mid 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
        else: 
            return binarySearch(arr, mid + 1, r, x) 
    else: 
        return -1


##Quick Sort
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
        return L


#Creamos el arreglo
L = []
num = int (input("Escribe un número entero"))
L = random.sample(range(num), num)
item = random.randrange(num,0,-1)
print ("buscamos",item)

#Ordenamos el arreglo
n = len(L)
quickSort(L,0,n-1)


start_time = time.time()
search (L, item)
print("Tiempo de Búsqueda secuencial", (time.time() - start_time))


start_time = time.time()
result = binarySearch (L, 0, len(L)-1, item)
if result != -1: 
    print ("Position", result) 
else: 
    print ("Not found")
print("Tiempo de Búsqueda binaria", (time.time() - start_time))
