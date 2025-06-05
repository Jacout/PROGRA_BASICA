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
def arreglo(num):
    for x in range (num):
        L.append(random.randrange(100,0,-1))
    return L
 
L = []
num = int (input("Escribe un número entero"))
L = arreglo(num)
start_time = time.time()
insertionSort(L) 
print( "Tiempo de primera ejecucion",(time.time() - start_time))

L.clear()
L = arreglo(num)
start_time = time.time()
insertionSort(L) 
print("Tiempo de segunda ejecucion", (time.time() - start_time))
