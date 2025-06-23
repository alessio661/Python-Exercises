"""Algoritmi di ordinamento"""

def selectionSort(A):
    for i in range(len(A) - 1):
        indice_min = i
        
        for j in range(i+1, len(A)):
            if A[j] < A[indice_min]:
                indice_min = j
            
        A[i], A[indice_min] = A[indice_min], A[i]
        
"""Costo: Theta n^2"""

"""--------------------------------------"""
    
def insectionSort(A):
    for i in range(1, len(A)):
        x, j = A[i], i - 1
        
        while j >= 0 and A[j] > x:
            A[j + 1] = A[j]
            j -= 1
            
        A[j + 1] = x
        
"""Prende il primo elemento della parte ordinata e lo confronta con gli elementi
della parte non ordinata
Costo: Caso migliore Theta(N)
Costo: Caso peggiore Theta(N^2)"""

"""--------------------------------------"""

def bubbleSort(A):
    for i in range(len(A) - 1):
        scambi = False
        
        for j in range(len(A) - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                scambi = True
                
        if not scambi:
            return

"""Confronta le coppie adiacenti a 2 a 2 da sinistra a destra fino a stabilire
ogni volta un massimo
Costo: Caso migliore Theta(N)
Costo: Caso peggiore Theta(N^2)"""

"""--------------------------------------"""

def countingSort(A):
    n, k = len(A), max(A)
    counter = [0]*(k+1)
    
    for i in range(n):
        counter[A[i]] += 1
        
    j = 0
    for i in range(k+1):
        for _ in range(counter[i]):
            A[j] = i
            j += 1
            
"""Crea un array di conteggio che conta il numero di occorrenze per ogni elemento
Costo: Complessita O(n + k)"""
        
"""--------------------------------------"""
    
def mergeSort(A, i, j):
    if i < j:
        mid = (i + j) // 2
        mergeSort(A, i, mid)
        mergeSort(A, mid + 1, j)
        fondi(A, i, mid, j)

def fondi(A, i, mid, j):
    a, b = i, mid+1
    B = []
    
    while a <= mid and b <= j:
        if A[a] <= A[b]:
            B.append(A[a])
            a += 1
        else:
            B.append(A[b])
            b += 1
    
    while a <= mid:
        B.append(A[a])
        a += 1
        
    while b <= j:
        B.append(A[b])
        b += 1
    
    for x in range(len(B)):
        A[i + x] = B[x]

"""Ricapitolando:
    Divide: la sequenza in 2 sequenze ogni volta (n/2)
    impera: le 2 sottosequenze vengono ordinate ricorsivamente
    combina: Le sottosequenze per creare la lista ordinata
    
    Funzionamento funzione fondi:
        Il minimo della sequenza complessiva non può che essere il minimo
        tra i 2 minimi delle sottosequenze
    
    Complessità: 2T(n/2) + Theta(n) -> nlog(n)"""

"""--------------------------------------"""

def quickSort(A):
    if len(A) <= 1:
        return A
    
    pivot = A[0]
    sinistra = destra = []
    
    for i in range(1, len(A)):
        if A[i] < pivot:
            sinistra.append(A[i])
        else:
            destra.append(A[i])
    
    return quickSort(sinistra) + pivot + quickSort(destra)

"""Proposta chiara, ma crea ogni volta più liste quindi adoperiamo una partition,
ecco il quicksort completo:"""

def quickSortWPartition(A, primo, ultimo):
    if primo < ultimo:
        k = partiziona(A, primo, ultimo)
        quickSortWPartition(A, primo, k-1)
        quickSortWPartition(A, k+1, ultimo)

def partiziona(A, primo, ultimo):
    pivot = A[primo]
    i, j = primo + 1, ultimo
    
    while True:
        while i <= ultimo and A[i] <= pivot:
            i += 1
        
        while A[j] >= pivot:
            j -= 1
        
        if i < j:
            A[i], A[j] = A[j], A[i]
        else:
            A[primo], A[j] = A[j], A[primo]
            return j

"""
Complessità partition: Theta(n)
Complessità QuickSort: T(k) + T(n - 1 - k) + Theta(n) -> nlog(n) (Nel caso medio)
"""
    
    
    
    
    

