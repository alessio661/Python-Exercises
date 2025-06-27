class Nodo:
    def __init__(self, key = None, next = None):
        self.key = key
        self.next = next

def crea(A):
    if not A:
        return None
    
    p = Nodo(A[0])
    q = p
    
    for i in range(1, len(A)):
        q.next = Nodo(A[i])
        q = q.next
    
    return p

class NodoD:
    def __init__(self, key = None, prev = None, next = None):
        self.key = key
        self.next = next
        self.prev = prev

def creaDoppia(A):
    if not A:
        return None
    
    p = NodoD(A[0])
    q = p
    
    for i in range(1, len(A)):
        q.next = NodoD(A[i], q)
        q = q.next
    
    return p
        

"""Esercizio 1:
data una lista tramite il puntatore alla sua testa, restituire
il puntatore all’ultimo elemento se la lista ha almeno un
elemento, None altrimenti
"""

def lastElement(pointer):
    if not pointer:
        return None
    
    while pointer.next:
        pointer = pointer.next
    
    return pointer.key

print("Esercizio 1: ", lastElement(crea([1, 2, 3, 4, 5])))
print("Esercizio 1: ", lastElement(crea([])))

"""Esercizio 2:
data una lista tramite il puntatore alla sua testa, restituire
il puntatore al penultimo elemento se la lista ha almeno
due elementi, None altrimenti; 
"""

def penultimo(pointer):
    if not pointer or not pointer.next:
        return None
    
    q = pointer.next
    
    while q.next:
        pointer = q
        q = q.next
        
    return pointer.key
    
print("Esercizio 2: ", penultimo(crea([1, 2, 3, 4, 5])))
print("Esercizio 2: ", penultimo(crea([1])))

"""Esercizio 3:
Dato il puntatore ad una lista doppiamente puntata restituire
la lunghezza della lista; 
"""

def lunghezzaDoppia(pointer, c = 0):
    if not pointer:
        return c
    
    while pointer:
        pointer = pointer.next
        c += 1
    
    return c

print("Esercizio 3: ", lunghezzaDoppia(creaDoppia([1, 2, 3, 4, 5])))
print("Esercizio 3: ", lunghezzaDoppia(creaDoppia([])))

"""Esercizio 4:
Dato il puntatore ad una lista doppiamente puntata stampare
gli elementi della lista in ordine inverso (i.e. dall’ultimo al
primo); 
"""

def reverse(pointer):
    if not pointer:
        return None
    
    while pointer.next:
        pointer = pointer.next
        
    while pointer:
        print(pointer.key)
        pointer = pointer.prev
    
print("Esercizio 4: ")
reverse(creaDoppia([1, 2, 3, 4, 5]))
        
"""Esercizio 5:
data una lista ordinata di interi tramite il puntatore al suo
primo elemento ed un intero , aggiungere alla lista in
modo da rispettare l’ordinamento; 
"""

def inserisci(pointer, x):
    if not pointer:
        return x
    
    q = pointer
    while q.next and q.next.key < x:
        q = q.next
    
    q.next = Nodo(x, q.next)
    
    return pointer
    
def stampa(pointer):
    while pointer:
        print(pointer.key)
        pointer = pointer.next
    
print("Esercizio 5: ")
stampa(inserisci(crea([1, 2, 3, 5, 6]), 4))

"""Esercizio 6:
Dato il puntatore ad una lista di interi doppiamente puntata
ed ordinata cancellare dalla lista tutti i duplicati.
"""

def eliminaDuplicati(pointer):
    if not pointer:
        return None
    
    D = {}
    while pointer:
        if pointer.key in D.keys():
            D[pointer.key] += 1
        else:
            D[pointer.key] = 1
        pointer = pointer.next
        
    A = [k for k, v in D.items() if v >= 2]
    
    while pointer:
        if pointer.key in A:
            pointer.prev.next = pointer.next
            pointer.prev = pointer.prev.prev
        pointer = pointer.prev
    
    return pointer

def stampa(pointer):
    while pointer:
        print(pointer.key)
        pointer = pointer.next

stampa(eliminaDuplicati(creaDoppia([2, 2, 4, 5, 2, 3, 3])))
        
    
                
    
    
        
        
        
        
    
    
        