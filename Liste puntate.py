class Nodo:
    def __init__(self, key=None, next=None):
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

def stampa(p):
    if not p:
        return None
    
    while p:
        print(p.key)
        p = p.next

"""Esercizio 1:
Esercizio 1. Scrivere una funzione ITERATIVA che, preso in
input un intero , restituisce il puntatore ad una lista
concatenata di nodi contenenti nell’ordine i valori
n, n-1, n-2 ... 1"""

def creaIter(n):
    if not n:
        return None
    
    p = Nodo(n)
    q = p
    
    while n != 1:
        n -= 1
        q.next = Nodo(n)
        q = q.next
    
    return p

print("Esercizio 1: ", stampa(creaIter(7)))

"""Ora la versione ricorsiva!"""

def creaRic(n):
    if not n:
        return None
    
    p = Nodo(n)
    p.next = creaRic(n-1)
    return p

print("Esercizio 1 ricorsivo:", stampa(creaRic(7)))

"""Esercizio 2:
Esercizio 2. Scrivere una funzione ITERATIVA che, preso in
input il puntatore alla testa di una lista concatenata e una
chiave x restituisce lil numero di occorrenze di x della lista.
"""

def contaOccorrenzeITER(p, x):
    if not p:
        return 0
    
    counter = 0
    
    while p:
        if p.key == x:
            counter += 1
        p = p.next
    
    return counter

print("Esercizio 2: ", contaOccorrenzeITER(crea([2, 3, 4, 8, 8, 8]), 8))

"""VERSIONE RICORSIVA!"""

def contaOccorrenzeRIC(p, x):
    if not p:
        return 0
    
    if p.key != x:
        return contaOccorrenzeRIC(p.next, x)
    
    return 1 + contaOccorrenzeRIC(p.next, x)

print("Esercizio 2 RICORSIVO: ", contaOccorrenzeRIC(crea([2, 3, 4, 8, 8, 8]), 8))

"""Esercizio 3:
Scrivere una funzione RICORSIVA che preso
in input il puntatore alla testa di una lista concatenata
stampa le chiavi dei nodi presenti nella lista in ordine
inverso.
"""

def stampaInversaRIC(p):
    if p == None:
        return
    
    stampaInversaRIC(p.next)
    print(p.key)
    
print("Esercizio 3 RICORSIVO: ", stampaInversaRIC(crea([4, 3, 2, 5, 1, 2])))

"""Esercizio 4:
Scrivere una funzione RICORSIVA che preso in
input il puntatore alla testa di una lista concatenata non vuota
ed un intero x, rimuovere dalla lista le occorrenze di x e
restituisce la testa della lista.
"""

def eliminaOccorrenze(p, x):
    if not p:
        return None
    
    if p.key == x:
        return eliminaOccorrenze(p.next, x)
    else:
        p.next = eliminaOccorrenze(p.next, x)
        return p
    
print("Esercizio 4 RICORSIVO: ", stampa(eliminaOccorrenze(crea([2, 3, 4, 4, 5]), 4)))
    
"""Esercizio 5:
Scrivere una funzione che preso in input il puntatore
alla testa di una lista concatenata restituisce i puntatori alle teste di
due liste concatenate, la prima con gli elementi dei nodi di posto
pari nella lista di partenza, e la seconda con gli elementi dei nodi
di posto dispari (senza creare nuovi record).
"""

def pariEDispari(p):
    p1, p2=None, None
    dispari = True
    while p:
        q=p.next
        if dispari:
            p.next=p1
            p1=p
        else:
            p.next=p2
            p2=p
        dispari=not dispari
        p=q
    
    return p1, p2

"""Esercizio 6:
Data in input una lista ordinata di interi tramite il
puntatore al primo elemento, ed un elemento da inserire,
aggiungere tale elemento alla lista in modo da rispettare
l’ordinamento.
"""

def inserisci_ord(p, x):
    if not p or x < p.key:
        return Nodo(x, p)
    
    while p.next and (p.next).key < x:
        p = p.next
        
    p = Nodo(x, p.next)
    
    return p

print("Esercizio 6: ", stampa(inserisci_ord(crea([2, 4, 6, 8, 10]), 5)))
print("Esercizio 6: ", stampa(inserisci_ord(crea([2, 4, 6, 8, 10]), 11)))
print("Esercizio 6: ", stampa(inserisci_ord(crea([2, 4, 6, 8, 10]), 1)))

"""Esercizio 7:
Abbiamo due liste a puntatori ciascuna priva di duplicati e le cui chiavi
compaiono nelle liste in modo non decrescente.
Progettare un algoritmo che, dati i puntatori e alle teste delle due
liste, restituisce il puntatore alla testa di una terza lista contenente le
chiavi comuni alle due liste. Non è importante l’ordine con cui le chiavi
compaiono nella terza lista ma questa non deve contenere duplicati. Le
due liste di partenza non vanno alterate.
La procedura deve avere complessità O(n + m) dove n e m sono le
lunghezze delle due liste. 
"""

def commons(p, q):
    t = None
    while p and q:
        if p.key == q.key:
            t = Nodo(p.key, t)
        
            while p.next and (p.next).key == p.key:
                p = p.next
            p = p.next
        
            while q.next and (q.next).key == q.key:
                q = q.next
            q = q.next
            
        elif p.key < q.key:
            while p.next and (p.next).key == p.key:
                p = p.next
            p = p.next
            
        else:
            while q.next and (q.next).key == q.next:
                q = q.next
            q = q.next
    
    return t

print("Esercizio 7", commons(crea([2, 2, 5, 7, 8]), crea([2, 3, 5, 9])))

"""Esercizio 8:
Hai una lista concatenata senza duplicati, costruita con la classe Nodo. Devi scrivere una funzione che:
Copia ogni nodo della lista, creando un nuovo nodo con lo stesso valore key.
Interlaccia la copia subito dopo il nodo originale.
Dividi la lista originale e la lista copia, restituendo due liste separate:
Una con i nodi originali.
Una con i nodi copiati.
"""

def interlaccia(p):
    if not p:
        return None
    
    original = copy = None
    
    while p:
        p.next = Nodo(p.key, p.next)
        
        original = Nodo(p.key)
        copy = Nodo(p.key)
        
        p = p.next.next
    
    return original, copy

"""Esercizio 9: 
Esame febbraio 2024"""

def least(p, k):
    if not p:
        return 0
    
    if p.key >= k:
        return 1
    
    return least(p.next, k - p.key) + 1

"""Esercizio 10
Esame gennaio 2023"""

def equals(p):
    if not p:
        return 0
    
    c = p.key + equals(p.next)
    
    if c == p.key:
        return p.key
    
    return c

"""Esercizio 11
Trovare iterativamente i picchi di una lista a puntatori
"""

def peaks(p):
    if not p:
        return 0
    
    counter = 0
    
    while p.next.next:
        if (p.next.key // 2 <= p.key) and (p.next.next.key // 2 <= p.key):
            counter += 1
        p = p.next
    
    return counter

"""Esercizio 12
Sia p il puntatore alla testa di una lista concatenata i cui
nodi sono costituiti da un campo key contenente un valore
intero ed un campo next contenente un puntatore al nodo
successivo o None nel caso dell’ultimo nodo. Si progetti un
algoritmo ricorsivo che, dato in input il puntatore p, cancelli
dalla lista tutti i nodi con chiave negativa e restituisca il
puntatore alla testa della nuova lista."""

def nonNegatives(p):
    if not p:
        return None
    
    if p.key < 0:
        return nonNegatives(p.next)
    
    p.next = nonNegatives(p.next)
    
    return p

    
    


    
    
        
    
            

        
        
            
        
        
    
    
    


    