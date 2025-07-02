from random import randint

class NodoABR:
    def __init__ (self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def genera(A):
    lista = sorted(A, reverse = True)
    return generaABR(len(lista), lista)

def generaABR(n, A):
    if not n:
        return 0
    
    root = NodoABR()
    s = randint(0, n-1)
    
    root.left = generaABR(s, A)
    root.key = A.pop()
    root.right = generaABR(n-1-s, A)
    
    return root
    
"""Esercizio 1:
Cercare elemento x nell'albero binario di ricerca
"""

def ricercaABR(root, x):
    if not root:
        return None
    
    while root:
        if root.key == x:
            return x
        else:
            if x < root.key:
                root = root.left
            else:
                root = root.right

def ricercaABR_ric(root, x):
    if not root:
        return None
    
    if root.key == x:
        return x
    else:
        if x < root.key:
            return ricercaABR_ric(root.left, x)
        else:
            return ricercaABR_ric(root.right, x)

print(ricercaABR(genera([2, 3, 6, 4, 7, 9, 5]), 7)) 
print(ricercaABR_ric(genera([2, 3, 6, 4, 7, 9, 5]), 7))   

"""Esercizio 2:
Inserire un elemento nell'albero binario di ricerca"""

def inserisci(root, x):
    elemento = NodoABR(x)
    if not root:
        return elemento.key
    
    nodo = root
    while nodo:
        if x < nodo.key:
            if not nodo.left:
                nodo.left = elemento
                break
            else:
                nodo = nodo.left
        else:
            if not nodo.right:
                nodo.right = elemento
                break
            else:
                nodo = nodo.right
    return root

def inserisciRIC(root, x):
    if not root:
        return NodoABR(x)
    
    if x < root.key:
        root.left = inserisciRIC(root.left, x)
    else:
        root.right = inserisciRIC(root.right, x)
    
    return root

"""Esercizio 3:
Progettare una procedura ricorsiva che, dato il puntatore alla
radice di un simile albero e un valore , restituisce il valore
del - nodo in un ordinamento delle chiavi dell’albero. Viene
stampato nel caso l’albero abbia meno di nodi.
"""

def returner(root, k):
    A = []
    visita(root, k)
    
    if k <= len(A):
        return A[k - 1]

def visita(root, A):
    if not root:
        return 
    
    visita(root.left, A)
    A.append(root.key)
    visita(root.right, A)

"""Esercizio 4:
Trova la somma dei valori di tutti i nodi le cui chiavi sono comprese 
in un intervallo [L, R]
"""

def somma_intervallo(root, L, R):
    if not root:
        return 0
    
    if root.key < L:
        return somma_intervallo(root.right, L, R)
    
    if root.key > R:
        return somma_intervallo(root.left, L, R)
    
    return root.key + somma_intervallo(root.left, L, R) + somma_intervallo(root.right, L, R)
    
print("Esercizio 4: ", somma_intervallo(genera([2, 3, 6, 4, 7, 8, 5]), 3, 7))
    
    
    
    
    
    
            
        

        
            
    
    
    
    
    
        
    