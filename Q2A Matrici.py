'''
si definisca la funzione es62(matrice) che riceve come argomento una matrice (lista di liste)
di interi e che:
    - individua le coordinate x1,y1 del MINIMO valore in essa contenuto
        (in caso di parita' si prenda l'elemento con x minima 
        e in caso di ulteriore parita' quello con y minima)
    - individua le coordinate x2,y2 del MASSIMO valore in essa contenuto
        (in caso di parita' si prenda l'elemento con x massima
        e in caso di ulteriore parita' quello con y massima)
    - scambia le due righe y1 ed y2 e le due colonne x1 ed x2.
Ritorna come risultato la matrice ottenuta.
La matrice originale non deve essere modificata.    
La funzione deve poter funzionare anche se x1==x2 e/o y1==y2.

Esempio: se
            | 2  0   -4 |                   | 5  10  20 |
matrice =   | 5  10  20 |   risultato =>    | 2  0   -4 |
            | 5  1   -1 |                   | 5  1   -1 |
Se invece            
            | 2   0  -4 |                   | -1  1  25 |
matrice =   | 5  10  10 |   risultato =>    | 10 10   5 |
            | 25  1  -1 |                   | -4  0   2 |
'''

def minAndMax(matrice):
    min, max, ccmin, ccmax = float("inf"), float("-inf"), (0, 0), (0, 0)
    
    for r, row in enumerate(matrice):
        for c, col in enumerate(row):
            if col < min: 
                min = col
                ccmin = (r, c)
                
            if col > max:
                max = col
                ccmax = (r, c)
                
    newMatrix = [[matrice[row][col] for col in range(len(matrice[0]))] for row in range(len(matrice))]
    
    for row in range(len(matrice[0])):
        newMatrix[row][ccmin[1]] = matrice[row][ccmax[1]]
        newMatrix[row][ccmax[1]] = matrice[row][ccmin[1]]
        
        for col in range(len(matrice[0])):
            newMatrix[ccmin[0]][col] = matrice[ccmax[0]][col]
            newMatrix[ccmax[0]][col] = matrice[ccmin[0]][col]
            
    return ccmin, ccmax, newMatrix

print(minAndMax([[2, 0, -4], [5, 10, 20], [5, 1, -1]]))





'''
es21(matrice) presa la matrice di caratteri rappresentata tramite una lista di liste di caratteri, 
la restituisce dopo averne ordinato le colonne in ordine lessicografico. 
La matrice passata in input al termine della funzione non deve risultare modificata.  
Ad esempio se la matrice di input e'
 [['q','s','g','g'],
  ['b','a','m','f'],
  ['a','b','n','z']] 
la funzione restituira' la matrice:
 [['a','a','g','f'],
  ['b','b','m','g'],
  ['q','s','n','z']]     
'''

def ording(matrice):
    matrix = [[] for i in range(len(matrice))]
    
    for col in range(len(matrice[0])):
        colonna = []
        
        for row in range(len(matrice)):
            colonna += matrice[row][col]
        colonna.sort()
        
        for row in range(len(matrice)):
            matrix[row] += colonna[row]

    return matrix
            
print(ording([['q','s','g','g'],['b','a','m','f'],['a','b','n','z']]))





'''
la funzione es55(sel,m,n,A) che, presi in input:
- una stringa di testo contenente uno tra i caratteri 'r' e 'c'
- due interi m e n
- una matrice A di interi (rappresentata tramite lista di liste in cui ciascuna lista e' una riga della matrice)
restituisce la coppia (tupla) di interi con  il minimo e il massimo tra gli elementi della matrice
e la modifica distruttivamente.
Al termine della funzione:
-se sel='r' allora la  riga m e la riga n della matrice A risultano scambiate tra loro.
-se sel='c' allora la colonna m e la colonna n della matrice A risultano scambiate tra loro
Si puo' assumere che le dimensioni h e w della matrice siano tali che m,n <=h e m,n<=w.
Ad esempio:
- per sel='r', m=1,n=2 e A=[[2,0,-4],[5,10,20],[5,1,-1]] al termine dell'esecuzione della funzione
  verra' restituita la tupla (-4,10) e  si avra' A=[[2,0,-4],[5,1,-1],[5,10,20]]
- per sel='c', m=0,n=1 e A=[[2,0,-4],[5,10,20],[5,1,-1]] al termine dell'esecuzione della funzione   
verra' restituita la tupla (-4,10) e  si avra' A=[[0,2,-4],[10,5,20],[1,5,-1]]
'''

def es55(sel,m,n,A):
    assert sel.lower() == "r" or sel.lower() == "c", "Parametri errati!"
    
    min, max, tupla = float("inf"), float("-inf"), tuple()
    
    for row in A:
        for col in row:
            if col < min:
                min = col
                
            if col > max:
                max = col
    tupla = (min, max)
    
    if sel.lower() == "r":
        local = A[m]
        A[m] = A[n]
        A[n] = local
    else: 
        for r in range(len(A)):
            local = A[r][m]
            A[r][m] = A[r][n]
            A[r][n] = local
        
    return A, tupla

print(es55("r", 1, 2, [[2,0,-4],[5,10,20],[5,1,-1]]))
print(es55("c", 0, 1, [[2,0,-4],[5,10,20],[5,1,-1]]))





'''
la funzione es56(tabella) che presa in input:
- una tabella  di interi (rappresentata tramite lista di liste in cui ciascuna lista e' 
una riga della tabella) restituisce la lista con gli interi che occorrono il massimo 
numero di volte nella tabella e modifica la tabella distruttivamente. 
La lista restituita deve risultare  ordinata in modo crescente. Al termine della funzione, 
nella tabella i numeri che occorrevano un numero massimo di volte devono risultare sostituiti dal 
carattere '*'.
Ad esempio per tabella= [[3,2,1,3],[2,1,3,5],[1,3,2,1]] al termine della funzione la lista 
restituita e' [1,3] e la tabella diviene [[*,2,*,*],[2,*,*,5],[*,*,2,*]] 
'''

def es56(tabella):
    conteggio, max, lista = dict(), 1, list()
    
    for row in tabella:
        for col in row:
            
            if not col in conteggio:
                conteggio[col] = 0
            else:
                conteggio[col] += 1 
            
    for k, v in conteggio.items():
        if v > max:
            max = v
        
    lista.extend([k for k, v in conteggio.items() if v == max])
    
    for r, row in enumerate(tabella):
        for c, col in enumerate(row):
            if tabella[r][c] in lista:
                tabella[r][c] = "*"
       
    return sorted(lista), tabella

print(es56([[3,2,1,3],[2,1,3,5],[1,3,2,1]]))





# Una matrice si dice sparsa se ha pochi valori diversi da zero. Per risparmiare spazio 
# di memoria, anzicche' utilizzare liste di liste  possiamo rappresentare matrici 
# sparse tramite dizionari. Il dizionario di una matrice sparsa M ha come chiavi delle tuple  
# e come attributo degli interi. Le tuple sono coppie e la coppia (i,j) e' presente nel dizionario 
# se e solo se M[i][j] e' diverso  da zero. L'attributo della chiave (i,j) sara' poi proprio M[i][j].
# ad ESEMPIO il dizionario 
# d={(0,2): 4,(1,0): 1, (1,1): 2, (2,1):8 } rappresenta la matrice quadrata  M=
# | 0 0 4 |
# | 1 2 0 |
# | 0 8 0 |

"""
Si definisca la  funzione es52(d1,d2) che, 
- riceve due dizionari di matrici sparse della stessa dimenzione.
- restituisce un dizionario con la matrice sparsa somma delle due matrici avute in input.
Ad ESEMPIO se
d1={(0,2): 4,(1,0): 1, (1,1): 2, (2,1):8 } e d2={(0,0): 5,(1,1): 2, (2,2): 5, (1,0):2 }
allora la funzione restituira' il dizionario 
{(0,2): 4,(1,0): 3, (1,1): 4, (2,1):8, (0,0):5, (2,2):5 }
I dizionari ricevuti non devono essere modificati

((Modificato, restituirà anche una matrice NxN dove N è la dimensione massima trovata in diz e con i valori in diz))
"""
        
def es52(d1, d2):
    diz = {k : d1[k] for k in d1}
    dimensione = float("-inf")
    
    for k, v in d2.items():
        if k in diz:
            diz[k] += v
        else:
            diz[k] = v
    
    for k in diz.keys():
        if k[0] > dimensione:
            dimensione = k[0]
        
        if k[1] > dimensione:
            dimensione = k[1]
            
    matrice = [[0 * row for row in range(dimensione + 1)] for col in range(dimensione + 1)]
    
    for k, v in diz.items():
        matrice[k[0]][k[1]] = v

    return diz, matrice

print(es52({(0,2): 4,(1,0): 1, (1,1): 2, (2,1):8 }, {(0,0): 5,(1,1): 2, (2,2): 5, (1,0):2 }))
                



'''
La funzione es60(ftesto, ftestoMod) che modifica il contenuto del file di testo il cui
percorso e' dato da ftesto, registra il file modificato nel file di testo il cui indirizzo
e' in ftestoMod e restituisce un intero.
Il file di testo ftesto contiene una matrice che ha per elementi elementi interi tra 1 e 9.
Ogni riga del file di testo contiene una riga della matrice ed i vari interi della riga sono
separati tra loro da uno spazio.
Una colonna della matrice si dice "dispari" se la maggior parte dei suoi elementi e' dispari.
(se il numero di elementi dispari è uguale al numero di elementi pari, la riga non è dispari)
In ftestoMod deve essere registrata la matrice dove tutti gli elementi  che occorrono
in colonne "dispari" sono stati sostituiti dalla cifra zero.
La funzione restituisce il numero di colonne della matrice che sono state azzerate.
Ad esempio se il file in ftesto contiene la matrice:
1 2 3 4 5 7
3 4 4 4 4 5
3 1 4 6 3 1
2 5 8 1 7 3
al termine della funzione verra' restituito il numero 3 e il file ftestoMod conterra' la matrice
0 2 3 4 0 0
0 4 4 4 0 0
0 1 4 6 0 0
0 5 8 1 0 0
'''

def es60(ftesto, ftestoMod):
    matrix = []
    azzeramenti = 0
    
    with open(ftesto) as f:
        for row in f:
            columns = list(map(int, row.split()))
            matrix.append(columns)
            
    for c, col in enumerate(matrix[0]):
        even = odd = 0
        for r, row in enumerate(matrix):
                if matrix[r][c] % 2 == 1:
                    odd += 1
                else:
                    even += 1
        
        if odd > even:
            azzeramenti += 1
            for r in range(len(matrix)):
                matrix[r][c] = 0
                
    with open(ftestoMod, "w") as f:
        f.write("\n".join(" ".join(map(str, row)) for row in matrix))
    
    return matrix, azzeramenti

print(es60("matrice1.txt", "matrice1RisCheck.txt"))





'''
La funzione es62(ftesto, op, sel) che, legge una matrice di interi contenuta
nel file di testo ftesto e restituisce una lista di interi.
La matrice e' memorizzata nel file per righe con  gli interi nelle righe separati da un numero
arbitrario di spazi.
La lista da tornare contiene i risultati di una operazione da effetture sulle righe, le colonne
o le diagonali della matrice. Il parametro 'op' specifica il tipo di operazione, e
puo' assumere tre diversi valori:
    'max' (per il calcolo del massimo),
    'min' (per il calcolo del minimo)
    e 'sum' (per il calcolo della somma).
Il parametro 'sel' specifica su quali elementi della matrice  l'operazione deve operare.
puo' assumere i seguenti valori:
    'row' (per applicarla alle varie righe della  matrice, in ordine crescente),
    'col' (per applicarla alle varie colonne della  matrice, in ordine crescente),
    'dp' (per applicarla  alla diagonale principale)
    e 'ds' per applicarla alla diagonale  secondaria.
Ad esempio se la matrice contenuta nel file di testo e':
2  0   -4
5  10  20
5  1   -1

a seconda dei parametri si avra':

es61(ftesto, 'max','row')= [2, 20, 5]
es61(ftesto, 'min','row')= [-4, 5,-1]
es61(ftesto, 'sum','row')= [-2, 35, 5]
es61(ftesto, 'max','col')= [ 5,  10, 20]
es61(ftesto, 'min','col')= [ 2,  0, -4]
es61(ftesto, 'sum','col')= [ 12, 11, 15]
es61(ftesto, 'max','dp' )= [10]
es61(ftesto, 'min','dp' )= [-1]
es61(ftesto, 'sum','dp' )= [11]
es61(ftesto, 'max','ds' )= [10]
es61(ftesto, 'min','ds' )= [-4]
es61(ftesto, 'sum','ds' )= [11]
'''

def es61(ftesto, op, sel = "row", risultato = "risultato.txt"):
    matrix = list()
    
    with open(ftesto) as f:
        for riga in f:
            columns = list(map(int, riga.split()))
            matrix.append(columns)
            
    if op == "sum":
        changefile(risultato, somma(matrix, sel))
        return somma(matrix, sel)
        
    if op == "max":
        changefile(risultato, massimo(matrix, sel))
        return massimo(matrix, sel)
        
    if op == "min":
        changefile(risultato, minimo(matrix, sel))
        return minimo(matrix, sel)
    

def changefile(file, risultato):
    with open(file, "w") as f:
        if isinstance(risultato, list):
            f.write(" ".join(map(str, risultato)))
        else:
            f.write(str(risultato))
            
            
def somma(matrice, sel):
    lista = list()
    
    if sel == "row":
        return [sum(riga) for riga in matrice]
    
    if sel == "col":
        for c, col in enumerate(matrice[0]):
            somma = 0
            
            for r, row in enumerate(matrice):
                somma += row[c]
            
            lista.append(somma)
            return lista
        
    if sel == "dp":
        lista.extend([matrice[row][col] for col in range(len(matrice[0])) 
                      for row in range(len(matrice)) if row == col])
        return sum(lista)
    
    if sel == "ds":
        newmatrix = matrice[::-1]
        lista.extend([newmatrix[row][col] for col in range(len(matrice[0]))
                      for row in range(len(matrice)) if row == col])
        return sum(lista)
        
    
def massimo(matrice, sel):
    lista = list()
    
    if sel == "row":
        return [max(row) for row in matrice]
    
    if sel == "col":
        for c, col in enumerate(matrice[0]):
            columns = list()
            for r, row in enumerate(matrice):
                columns.append(matrice[r][c])
                
            lista.append(max(columns))
        
        return lista
    
    if sel == "dp":
        lista.extend([matrice[row][col] for col in range(len(matrice[0])) 
                      for row in range(len(matrice)) if col == row])
        
        return max(lista)
    
    if sel == "ds":
        newmatrix = matrice[::-1]
        lista.extend([newmatrix[row][col] for col in range(len(matrice[0]))
                      for row in range(len(matrice)) if col == row])
        
        return max(lista)
        

def minimo(matrice, sel):
    lista = list()
    
    if sel == "row":
        return [min(row) for row in matrice]
    
    if sel == "col":
        for c, col in enumerate(matrice[0]):
            columns = list()
            for r, row in enumerate(matrice):
                columns.append(matrice[r][c])
                
            lista.append(min(columns))
        
        return lista
    
    if sel == "dp":
        lista.extend([matrice[row][col] for col in range(len(matrice[0])) 
                      for row in range(len(matrice)) if col == row])
        
        return min(lista)
    
    if sel == "ds":
        newmatrix = matrice[::-1]
        lista.extend([newmatrix[row][col] for col in range(len(matrice[0]))
                      for row in range(len(matrice)) if col == row])
        
        return min(lista)
    
print(es61("matrice2.txt", 'max','row'))
print(es61("matrice2.txt", 'min','row'))
print(es61("matrice2.txt", 'sum','row'))
print(es61("matrice2.txt", 'max','col'))
print(es61("matrice2.txt", 'min','col'))
print(es61("matrice2.txt", 'sum','col'))
print(es61("matrice2.txt", 'max','dp' ))
print(es61("matrice2.txt", 'min','dp' ))
print(es61("matrice2.txt", 'sum','dp' ))
print(es61("matrice2.txt", 'max','ds' ))
print(es61("matrice2.txt", 'min','ds' ))
print(es61("matrice2.txt", 'sum','ds' ))

    
