'''
Si progetti la funzione es42(fImageIn, fcolori, fImageOut) che
modifica il colore di alcuni pixel presenti in un imagine  PNG fImageIn  e salva poi l'immagine
modificata  in un nuovo file PNG FImageOut.
La funzione inoltre ritorna il numero di pixel dell'immagine i cui colori sono stati modificati.
I colori da modificare sono specificati dal file di testo fcolori.
Il file fcolori ha tante righe quanti sono i colori da modificare.
Ogni riga di fcolori contiene  6 interi a valori tra 0 e 255.
I primi tre indicano il colore da modificare
e i secondi tre il nuovo colore
Ad esempio la presenza eventuale della riga
0 0 0  255 255 255
indica che nell'immagine tutti  i pixel di colore nero ( i.e. di colore  (0,0,0)) devono
assumere colore bianco (i.e. devono assumere colore (255,255,255)).

NOTA: i colori devono essere sostituiti contemporaneamente
(e non con una sostituzione alla volta che potrebbe modificare un pixel piu' volte)

:param fImageIn: nome del file PNG contenente l'immagine da modificare
:param fcolori: nome del file di testo in cui trovare i colori da modificare
:param fImageOut: nome del file PNG in cui salvare l'immagine modificata
:return: numero di pixel modificati
'''

import immagini

def es42(fImageIn, fcolori, fImageOut):
    img = immagini.load(fImageIn)
    counter = 0
    diz = dict()
    
    with open(fcolori, "r") as f: 
        for line in f:
            r, g, b, R, G, B = map(int, line.split())
            diz[(r, g, b)] = R, G, B 
        
    for r, row in enumerate(img):
        for c, col in enumerate(row):
            if col in diz:
                img[r][c] = diz[col]
                counter += 1    
    
    immagini.save(img, fImageOut)
        
    return counter





'''    
Es 3: 6 punti
Si definisca la  funzione es3(fimm1,fimm2,fimm3) che, 
- riceve gli  indirizzi di due file .PNG da leggere (fimm1 e fimm2) e l'indirizzo 
  di un file (fimm3) da creare.
- legge le due immagini DI DIMENSIONI DIVERSE e crea la terza immagine da salvare all'indirizzo fimm3.
  La terza immagine si ottiene dalle prime due. Ha ampiezza  massima tra 
  le ampiezze  di fimm1 e fimm2 ed  altezza massima tra le altezze di fimm1 e fimm2.
  Per quanto riguarda i colori dei pixel della nuova immagine:
  il pixel [y][x] avra' colore nero (vale a dire (0,0,0)) se presente in entrambe
  le immagini originarie o in nessuna delle due. In caso contrario assumera' il   colore 
  del pixel dell'unica immagine originaria in cui e' presente.
  (guardate le immagini di test per chiarimenti)
- salva l'immagine creata all'indirizzo fimm3
- calcola  il numero di pixel di colore nero presenti  nell'immagine creata.
  - restituisce il valore calcolato
Per caricare e salvare i file PNG si possono usare load e save della libreria immagini.
'''

import immagini

def es15(fimm1,fimm2,fimm3):
    img_1 = immagini.load(fimm1)
    img_2 = immagini.load(fimm2)
    
    rows = max(len(img_1), len(img_2))
    columns = max(len(img_1[0]), len(img_2[0]))

    img_3, counter = list(), 0
    
    for r in range(rows):
        row = list()
        
        for c in range(columns):
            if (r < len(img_1) and c < len(img_1[0])) and (r < len(img_2) and c < len(img_2[0])):
                row.append((0, 0, 0))
                counter += 1
            
            if (not r < len(img_1) and c < len(img_1[0])) and not (r < len(img_2) and c < len(img_2[0])):
                row.append((0, 0, 0))
                counter += 1
            
            if (r < len(img_1) and c < len(img_1[0])) and not (r < len(img_2) and c < len(img_2[0])):
                row.append(img_1[r][c])
                
                if img_1[r][c] == (0, 0, 0):
                    counter += 1
            
            if not (r < len(img_1) and c < len(img_1[0])) and (r < len(img_2) and c < len(img_2[0])):
                row.append(img_2[r][c])
                
                if img_2[r][c] == (0, 0, 0):
                    counter += 1
        
        img_3.append(row)
    immagini.save(img_3, fimm3)
    return counter
            
    immagini.save(img_3, fimm3)





'''
Si definisca la  funzione es49(fimm1,fimm2,fimm3) che, 
- riceve gli  indirizzi di due file .PNG da leggere (fimm1 e fimm2) e l'indirizzo 
  di un file (fimm3) da creare.
- legge le due immagini e crea la terza immagine da salvare all'indirizzo fimm3. 
  La terza immagine si ottiene dalle prime due. Ha ampiezza  minima tra 
  le ampiezze  di fimm1 e fimm2 ed  altezza minima tra le altezze di fimm1 e fimm2.
  il pixel [i][j] dell'immagine ha lo stesso colore del pixel corrispondente
  dell'immagine fimm1 se i e j sono entrambi numeri pari o entrambi numeri dispari, 
  ha il colore del pixel corrispondente in  fimm2 altrimenti
- salva l'immagine creata all'indirizzo fimm3
- calcola  il numero di pixel presenti nell'immagine creata per i quali  la somma delle 
  tre coordinate del colore e' un numero dispari.
  - restituisce il valore calcolato
Per caricare e salvare i file PNG si possono usare load e save della libreria immagini.
'''

import immagini

def es49(fimm1,fimm2,fimm3):
    img1 = immagini.load(fimm1)
    img2 = immagini.load(fimm2)
    
    rows = min(len(img1), len(img2))
    columns = min(len(img1[0]), len(img2[0]))
    
    img3 = [[(0, 0, 0) for _ in range(columns)] for _ in range(rows)]
    
    counter = 0
    
    for r, row in enumerate(img3):
        for c, col in enumerate(row):
            img3[r][c] = img2[r][c]
            
            if r % 2 == c % 2:
                img3[r][c] = img1[r][c]
            
            if (col[0] + col[1] + col[2]) % 2 == 1:
                counter += 1
    
    immagini.save(img3, fimm3)
    
    return counter





'''
Un quadrato sul piano e' individuato dalla sestupla  di interi (x,y,l,r,g,b) dove
(x,y) e' la coordinata del  vertice in alto a sinistra del quadrato,  l e' la lunghezza del lato
e gli ultimi tre valori danno il suo colore (r,g,b).
La funzione es65(k,lista1,fout) salva in formato PNG all'indirizzo fout un'immagine quadrata
di lato $k$ ottenuta come segue:
Su di uno sfondo di colore nero (0,0,0) di dimensione k per k  vengono disegnati in
sequenza i quadrati in lista1 che ricadono in tutto o in parte nella finestra k per k.
Il colore dei quadrati non deve necessariamente essere quello originale ma viene determinato
in base a questa regola: il colore del quadrato e' quello originale se nessuno dei pixel su cui incide il quadrato
ha un colore maggiore, in caso contrario il colore del quadrato sara' dato dal colore
massimo tra quello dei pixel su cui incide.
Un colore(x,y,z) e' maggiore di un altro (x',y',z') se x>x' o a parita' y>y' o a parita' z>z'.
Infine la funzione deve restituire il numero di pixel di  colore nero che compaiono nell’immagine
dopo aver inserito i quadrati.
Ad esempio se
lista1=[(20,50,20,0,255,0),(30,60,20,255,0,0),(60,50,20,255,0,0),(70,60,20,0,255,0)]
con es65(100,lista1,'prova1.png') si otterra' la figura nel file prova1.png
e verra' restituito il valore 8600.
'''

import immagini

def es65(k,lista1,fout):
    img = [[(0, 0, 0) for _ in range(k)] for _ in range(k)]
    matrice = len(img)
    count = 0
    
    for square in lista1:
        x, y, l, r, g, b = square
        
        for eachy in range(y, y+l):
            for eachx in range(x, x+l):
                if eachy < matrice and eachx < matrice:
                    img[eachy][eachx] = massimo((r, g, b), img[eachy][eachx])
                
    for r, row in enumerate(img):
        for c in range(len(row)):
            if img[r][c] == (0, 0, 0):
                count += 1
                    
    immagini.save(img, fout)
    
    return count


def massimo(colore1, colore2):
    r, g, b = colore1
    R, G, B = colore2
    
    if r > R or (r == R and g > G) or (r == R and g == G and b > B):
        return colore1
    return colore2





"""
 Definite la funzione es75 che riceve come argomenti
     h:                  altezza della immagine
     w:                  larghezza della immagine
     listaColori:        una lista di N colori nel formato (R, G, B) che devono essere applicati, nell'ordine da sinistra a destra, ai rettangoli
     listaAltezze:       una lista di N altezze < h
     larghezzaPalazzo:   la larghezza di ciascuno dei rettangoli da disegnare
     filePngOut:         path del file PNG in cui salvare l'immagine
     :return             numero di pixel cambiati piu' di 1 volta
 e che crea una immagine di dimensioni w,h con sfondo blu (0,0,255).
 Sulla immagine devono essere disegnati N rettangoli equispaziati tutti di larghezza larghezzaPalazzo, appoggiati in basso.
 L'altezza ed il colore del rettangolo i-esimo (da sinistra a destra) e' data dallo i-esimo elemento delle liste listaAltezze e listaColori.
 I rettangoli devono essere disegnati in modo che i rettangoli piu' bassi restino in primo piano rispetto ai rettangoli piu' alti.
 La funzione deve inoltre ritornare il numero di pixel che appartengono a piu' di un rettangolo
 (ovvero quelli di rettangoli che sono stati coperti da almeno un altro rettangolo)

 Nota:   assumete che la larghezza w della immagine sia sempre un multiplo di (1+N),
         in modo che il centro della posizione x di ciascun palazzo sia un valore intero
 Nota:   assumete che larghezzaPalazzo sia un valore pari
 Nota:   assumete che tutte le altezze siano minori o uguali dell'altezza h della immagine
 """

import immagini

def es75(w, h, listaColori, listaAltezze, larghezzaPalazzo, filePngOut):
    img = [[(0, 0, 255) for _ in range(w)] for _ in range(h)]
    pixelcambiati = [[0 for _ in range(w)] for _ in range(h)]
    rettangoli = list()
    
    count = 0
    start = 0
    end = larghezzaPalazzo
    
    step = (w - larghezzaPalazzo) // (len(listaAltezze) - 1)
    
    for i, altezza in enumerate(listaAltezze):
        rettangoli.append((start, end, h-altezza, h, listaColori[i]))
        start += step
        end += step
        
    rettangoli = sorted(rettangoli, key = lambda x: x[2])
    
    for rettangolo in rettangoli:
        c_start, c_end, r_high, r_low, colore  = rettangolo
        
        for row in range(r_high, r_low):
            for col in range(c_start, c_end):
                img[row][col] = colore
                pixelcambiati[row][col] += 1
                
    for r, row in enumerate(pixelcambiati):
        for c, col in enumerate(row):  
            if col > 1:
                count += 1
                
    immagini.save(img, filePngOut)
    
    return count

