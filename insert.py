import time
def insertionSort(arr):
    time.sleep(1)
    print(f"Arreglo inicial sin ordenar: {arr}")
    n = len(arr)  
    
    if n <= 1:
        return  
 
    for i in range(1, n):  
        piv = arr[i]  
        j = i-1
        while j >= 0 and piv < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = piv
    time.sleep(1)
    print(f"Arreglo final ordenado: {arr}")

  
nums = [12, 11, 13, 56, 6, 24, 7, 8, 15, 100, 2]
insertionSort(nums)
