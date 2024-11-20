import time
 
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    izq = [0] * (n1)
    der = [0] * (n2)
 
    for i in range(0, n1):
        izq[i] = arr[l + i]
 
    for j in range(0, n2):
        der[j] = arr[m + 1 + j]
 
    i = 0     
    j = 0     
    k = l    

    while i < n1 and j < n2:
        if izq[i] <= der[j]:
            arr[k] = izq[i]
            i += 1
        else:
            arr[k] = der[j]
            j += 1
        k += 1
 
    while i < n1:
        arr[k] = izq[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = der[j]
        j += 1
        k += 1
 
 
def mergeSort(arr, l, r):

    if l < r:
        m = l+(r-l)//2
 
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)



 
 
arr = [12, 11, 13, 56, 6, 24, 7, 8, 15, 100, 2, 72]
n = len(arr)


time.sleep(1)
print(f"Arreglo sin ordenar: {arr}")
mergeSort(arr, 0, n-1)
time.sleep(1)
print(f"\nArreglo ordenado: {arr}")
 
