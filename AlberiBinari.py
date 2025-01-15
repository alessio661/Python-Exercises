"""
ESERCIZI SUGLI ALBERI BINARI!!
"""

"""
Es 1:
Si definisca la funzione es48(tree) ricorsiva (o che fa uso di funzioni o metodi ricorsive/i) che:
- riceve come argomento 'tree' un  albero  formato da nodi di tipo
  AlberoBinario definito nella libreria albero.py allegata
- calcola il numero di nodi che nell'albero hanno ESATTAMENTE due figli
- torna come risultato il numero calcolato
Esempio: se l'albero e':

         7
        /\
       1  3
      / \
    4    6
   /    /
  5    2
 /     \
9       8

Nell'albero ci sono solo due nodi con esattamente due figli (il nodo con valore 7 ed il nodo
con valore 1) cosi'  la funzione tornera' il valore 2.
"""

from albero import AlberoBinario

def es48(tree : AlberoBinario):
    if not tree:
        return 0
    
    count = es48(tree.sx) + es48(tree.dx)
    
    if tree.sx and tree.dx:
        count += 1
        
    return count




"""
es 2:
   Si definisca la funzione es7(tree,insieme,k ) ricorsiva (o che fa uso 
   di funzioni o metodi ricorsive/i) che:
    - riceve come argomenti:
      - l'albero 'tree'  formato da nodi del tipo Nodo definito nella libreria 
        albero.py allegata, 
      - un insieme di caratteri 
      - un intero k
    - torna come risultato il numero di nodi dell'albero aventi 
      ESATTAMENTE  k figli i quali hanno  identificatori   
      presenti nell'insieme.
    
    Esempio: sia k=2 e ins={1,2,3,5,9}, allora la funzione es1
    - sull'albero a sinistra deve restituire 2 (per i figli dei nodi 4 e 2)
    - sull'albero a destra deve restituire 3 (per i figli dei nodi 7, 9 e 10).

              5                                     7              
      ________|_____________                _______|______         
     |          |           |              |              |        
     20         4           6              5              9        
     |     _____|______                 ___|___        ___|__      
     11   |   |  |  |  |               |       |      |      |     
          10  2  9  8  7               10      8      3      1     
            __|__                     _|_     _|_    _|_    _|_    
           |     |                   |   |   |   |  |   |  |   |   
           3     1                   1   2   12  13 15  6  4   0   
                                                                   
"""

from albero import Nodo

def es7(tree : Nodo, insieme, k):
    if not tree.f:
        return 0
    
    count = 0
    elcount = 0
    
    for el in tree.f:
        count += es7(el, insieme, k)
        
        if el.id in insieme:
            elcount += 1
        
    if elcount == k:
        count += 1
        
    return count

"""
es 3:
     Si definisca la funzione es14(tree,x) ricorsiva (o che fa uso di funzioni o metodi ricorsive/i) 
     che riceve come argomenti:
     -  'tree' un  albero  formato da nodi di tipo AlberoBinario definito nella libreria 
         albero.py allegata
     - un intero x
     - calcola il numero di nodi che nell'albero che hanno valore divisibile per x 
     - torna come risultato il numero calcolato

     ATTENZIONE: E' VIETATO USARE I METODI DELLA LIBRERIA albero

     Esempio: se x = 2 e l'albero e':

             7
             /\
           1  3
           / \
         4    6
       /    /
       5    2
     /     \
     9       8

 Nell'albero ci sono 3 nodi con valore divisibile per 2+livello (sono i nodi a valore 3,4 e 5)
 cosi'  la funzione tornera' il valore 3.
"""

from albero import AlberoBinario

def es14(tree : AlberoBinario, x):
    if not tree:
        return 0
    
    count = 0
    
    if tree.dx:
        count += es14(tree.dx, x+1)
    
    if tree.sx:
        count += es14(tree.sx, x+1)
        
    if tree.valore % x == 0:
        count += 1
    
    return count





"""
es 4: (con spiegazione)

Si definisca la funzione es6(testo) ricorsiva (o che fa uso di funzioni o 
metodi ricorsive/i) che:
- riceve come argomento:
   - un insieme di stringhe che hanno la proprietà che ciascuna è stata 
   ottenuta a partire dallo stesso albero binario
      (in cui ciascun nodo contiene un solo carattere), risalendo da ciascuna 
      foglia fino alla radice e concatenando
      i valori dei nodi
      NOTA l'albero è localmente ordinato da sinistra a destra, ovvero:
      - ciascun figlio sinistro contiene un carattere minore di quello del padre
      - ciascun figlio destro contiene un carattere maggiore di quello del padre
- ricostruisce l'albero originale e lo torna come risultato

Esempio: se l'albero da ricostruire è
                  i     
                  |
          |-----------------|               
          h                 m 
          |                 |   
      |--------|        |------|   
      c        j        k      p
      |        |               |
   |-----|  |-----|         |-----|
   a     f  g     k         m     q    

L'insieme di stringhe è
   { 'achi', 'qpmi', 'gjhi', 'fchi', 'mpmi', 'kmi', 'kjhi' }

ATTENZIONE: è VIETATO usare i metodi della classe AlberoBinario
"""

from albero import AlberoBinario

def es6(percorsi):
    # Trasformo il set in una lista in modo da poter sottoscriverla
    lista = list(percorsi)
    # Rendo root un nodo della classe AlberoBinario
    root = AlberoBinario(lista[0][-1:])
    
    # Per ogni percorso nella lista, root richiama la funzione ricorsiva
    for percorso in lista:
        root = albero(root, percorso[:-1])
    
    # Mi ritorna la root di quel path, di quel percorso e ricomincia
    return root

def albero(root : AlberoBinario, path):
    # Caso base: se il path non esiste (""), mi ritorna la root
    if not path:
        return root
    
    # Mi prendo l'ultima lettera del path, che ogni volta andrà a scalare 
    # fino a rendere il path vuoto e tornare al caso base
    lastChar = path[-1:]
    
    # l'esercizio dice che a destra il carattere è ogni volta più grande, quindi confrontiamo
    if root.valore < lastChar:
        # Se il ramo destro della nostra root non esiste (None), lo creiamo, sarà la nostra lastChar attuale
        if not root.dx:
            root.dx = AlberoBinario(lastChar)
            # Riesegue la funzione a partire dalla nostra posizione attuale, levando il carattere
            # "usato" nella scorsa chiamata
            albero(root.dx, path[:-1])
        else:
            albero(root.dx, path[:-1])
    # Da qui in poi sempre la stessa cosa...
    elif root.valore > lastChar:
        if not root.sx:
            root.sx = AlberoBinario(lastChar)
            albero(root.sx, path[:-1])
        else:
            albero(root.sx, path[:-1])
    
    # Ritorna la nostra posizione attuale.
    return root
    
    
    


