from random import randint

class NodoAB:
    def __init__(self, key = None, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right
        
def genera(n, m):
    if not n:
        return None
    
    root = NodoAB(randint(1, m))
    s = randint(0, n-1)
    
    root.left = genera(s, m)
    root.right = genera(n - 1 - s, m)
    
    return root

def stampa(root):
    if not root:
        return []
    
    space = spazio(root)
    A = [None]*(space+1)
    
    inserisci(root, A)
    return A
    
def spazio(root, x = 0):
    a = b = 0
    if root.left:
        a = spazio(root.left, 2*x+1)
    if root.right:
        b = spazio(root.right, 2*x+2)
    
    return max(a, b, x)

def inserisci(root, A, x = 0):
    if root:
        A[x] = root.key
        
        if root.right:
            inserisci(root.right, A, 2*x+2)
        if root.left:
            inserisci(root.left, A, 2*x+1)
            
print("Prova: ", stampa(genera(7, 20)))

"""Esercizio 1:
Tutti gli alberi non vuoti hanno foglie, dato un albero binario
non vuoto vogliamo sapere qual’è il livello minimo in cui
compaiono le sue foglie. 
"""

def minimo(root):
    if root.left == root.right == None:
        return 0
    
    if not root.right:
        return minimo(root.left) + 1
    if not root.left:
        return minimo(root.right) + 1
    
    return min(minimo(root.right), minimo(root.left)) + 1

    
print("Livello minimo: ", minimo(genera(7, 20)))
        

"""Esercizio 2:
Progettare una funzione che dato il puntatore alla radice di un albero
binario non vuoto memorizzato tramite puntatori verifichi se nell’albero
è presente un cammino radice-foglia dove la sequenza di chiavi
incontrate è strettamente crescente. 
"""

def crescente(root):
    if root.left == root.right == None:
        return True
    
    if root.left and crescente(root.left) and root.key < root.left.key:
        return True
    
    if root.right and crescente(root.right) and root.key < root.right.key:
        return True
    
    return False

print("Path crescente? ", crescente(genera(7, 20)))


"""Esercizio 3:
In un albero binario sono presenti nodi con un solo figlio, nodi con due figli
e nodi senza figli (le foglie).
Progettare un algoritmo che dato il puntatore alla radice di un albero binario
di nodi restituisce la terna di interi (x,y,z) dove x è il numero di nodi con
due figli, y il numero di nodi con 1 figlio e z il numero di foglie. 
"""

def terna(root):
    if not root:
        return 0, 0, 0
    
    if not root.left and not root.right:
        return 0, 0, 1
    
    if root.left:
        xS, yS, zS = terna(root.left)
    if root.right:
        xD, yD, zD = terna(root.right)
        
    if not root.left:
        return xD, yD + 1, zD
    if not root.right:
        return xS, yS + 1, zS

    return xD + 1, yD, zD

print("Terne: ", terna(genera(7, 20)))

"""Esercizio 4:
Trova la profondità massima (altezza) e la somma di tutte le foglie"""

def profondità_e_somma(root):
    if not root:
        return 0, 0
    
    if root.left:
        profSinistra, sommaSinistra = profondità_e_somma(root.left)
    if root.right:
        profDestra, sommaDestra = profondità_e_somma(root.right)
        
    if not root.left and not root.right:
        return 1, root.key
    
    return max(profSinistra, profDestra) + 1, sommaSinistra + sommaDestra

"""VARIANTE DOVE SOMMO SOLO LE FOGLIE AL LIVELLO MASSIMO:"""

def profondità_e_sommamax(root):
    if not root:
        return 0, 0
    
    if root.left:
        profSx, sommaSx = profondità_e_sommamax(root.left)
    if root.right:
        profDx, sommaDx = profondità_e_sommamax(root.right)
        
    if not root.left and not root.right:
        return 1, root.key
        
    if profSx > profDx:
        return profSx + 1, sommaSx
    
    if profDx > profSx:
        return profDx + 1, sommaDx
    
    return profSx + 1, sommaSx + sommaDx

"""Esercizio 5
Esame gennaio 2024, nodi validi"""

def validi(root):
    if not root:
        return 0
    
    if not root.left or not root.right:
        return 0
    
    if root.left.key > root.key > root.right.key or root.right.key > root.key > root.left.key:
        return 1 + validi(root.right) + validi(root.left)
    
    return validi(root.right) + validi(root.left)

"""Esercizio 6:
Esame gennaio 2023, tutti i nodi uguali"""

def same_values(root):
    if not root:
        return 1
    
    if root.left and root.left.key != root.key:
        return 0
    
    if root.right and root.right.key != root.key:
        return 0
    
    if same_values(root.left) and same_values(root.right):
        return 1
    else:
        return 0
    
"""Esercizio 7:
2 figli e chiavi pari"""

def research(root):
    if not root:
        return 0
    
    if root.left and root.right and root.key % 2 == 0:
        return 1 + research(root.left) + research(root.right)
    
    return research(root.left) + research(root.right)

"""Esercizio 8:
Sia T un albero binario qualunque memorizzato tramite record e puntatori. 
Ogni nodo dell’albero
contenga un valore intero come chiave. 
Si progetti un algoritmo ricorsivo che, dato il puntatore r alla radice dell’albero,
restituisca T true se l’albero è vuoto oppure se la chiave di ogni
nodo interno dell’albero risulta essere la somma delle chiavi
dei nodi foglia presenti nel suo sottoalbero, restituisca F alse
altrimenti. """

def void_or_sum(root):
    validator, _ = appoggio(root)
    return validator
    
def appoggio(root):
    if not root:
        return True, 0
    
    if not root.left and not root.right:
        return True, root.key
    
    if root.left:
        leftT, leftSum = appoggio(root.left)
    if root.right:
        rightT, rightSum = appoggio(root.right)
        
    if root.key == leftSum + rightSum:
        return True, leftSum + rightSum
    
    return False, leftSum + rightSum

"""Esercizio 9:
Sia dato un albero binario T, memorizzato tramite vettore dei padri. 
Per semplicità, assumiamo che gli n nodi di T siano etichettati con gli interi da 0 ad
n − 1, così che sia già evidente la biezione tra ciascun nodo e
il corrispondente indice. Si progetti un algoritmo iterativo
che, dato l’array P, che rappresenta il vettore dei padri di T,
restituisca il numero di foglie di T. Il costo dell’algoritmo
proposto deve essere di O(n), ed è consentito utilizzare O(n)
memoria ausiliaria. """

def vettore_padri(P):
    n = len(P)
    A = [0]*(n+1)
    
    for x in P:
        A[x] += 1
    
    foglie = 0
    
    for x in range(A):
        if x == 0:
            foglie += 1
    
    return foglie

"""Esercizio 10
Sia T un albero binario radicato memorizzato tramite record e puntatori. L’albero è non vuoto e
ogni nodo contiene un valore intero come chiave. Definiamo il
costo di un cammino radice-foglia come la somma delle chiavi
dei nodi che compongono il cammino.
Si progetti un algoritmo ricorsivo per trovare il valore minimo del costo 
di un cammino radice-foglia in un albero T
dato in input tramite il puntatore alla sua radice."""

def costo(root):
    if not root:
        return 0
    
    if not root.left and not root.right:
        return root.key
    
    sinistra = float("inf")
    destra = float("inf")
    
    if root.left:
        sinistra = costo(root.left)
    if root.right:
        destra = costo(root.right)
        
    return root.key + min(destra + sinistra)

"""Esercizio 11:
Sia dato un albero binario T non vuoto
contenente interi, e questo sia memorizzato tramite puntatori
e record di tre campi: il campo key contenente il valore ed i
campi left e right contenenti i puntatori al figlio sinistro e al
figlio destro, rispettivamente (questi puntatori valgono None
in mancanza del figlio).
Dato il puntatore r al nodo radice di T, progettare un algoritmo 
ricorsivo che in tempo Θ(n) restituisca True se in T esiste
un cammino radice-foglia dove gli interi dei nodi che si incontrano lungo il cammino formano una sequenza strettamente
crescente, False altrimenti."""

def crescente(root):
    if not root:
        return True
    
    if root.left and root.left.key > root.key and crescente(root.left):
        return True
    
    if root.right and root.right.key > root.key and crescente(root.right):
        return True
    
    return False

"""Esercizio 12:

    
    



        
    
        
    
    
    



    
    
        
      
        
    



    
    
    
    
    
    
    
    


    
    

    
    