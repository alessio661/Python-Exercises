"""
MIX DI ESERCIZI

Sets:
Esercizio Avanzato: Operazioni e Proprietà dei Set
Scrivi uno script Python che utilizzi i set per eseguire operazioni avanzate 
basandosi sulle loro proprietà matematiche.
"""
import random
import math

def operationSets():
    S = {el for el in range(1, 31)}
    
    pari = set(filter(lambda x : x % 2 == 0, S))
    dispari = set(filter(lambda x : x % 2 != 0, S))
    
    quadrati = set(map(lambda x : x**2, S))
    
    multipli_di_re = set(filter(lambda x : x % 3 == 0, S))
    
    maggiori_di_10 = set(filter(lambda x : x >= 10, S))
    
    cubi = set(map(lambda x : x**3, range(1, 21)))
    
    union_quadrati = set(map(lambda x : x**2, pari)) | set(map(lambda x : x**2, dispari))
    

def operationSetsAdvanced():
    S = list(random.randint(1, 1000) for _ in range(100))
    
    multipli_5e7 = set(filter(lambda x : x % 7 == 0 or x % 5 == 0, S))
    
    frequenze = set(map(lambda x : (x, S.count(x)), S))
    
    lista = list(map(lambda x: {"numero": x, "quadrato": x**2, "radice": round(math.sqrt(x))}, S))




"Adesso con i dizionari!"

def operationsDicts():
    D = {random.randint(1, 1000) : random.randint(1, 1000)**2 for _ in range(100)}
    
    pari_dict = dict(filter(lambda k: k[0] % 2 == 0, D.items()))
    dispari_dict = dict(filter(lambda k: k[0] % 2 != 0, D.items()))
    
    def un_divisibile(n):
        return any(x % n == 0 for x in D.keys())
    
    def tutti_divisibili(n):
        return all(x % n == 0 for x in D.keys())
    
    return pari_dict, dispari_dict, un_divisibile(5), tutti_divisibili(5)
    
print(operationsDicts())




"Esercizi sui cicli!"

def primopari(lista : list):
    for i, el in enumerate(lista):
        if el % 2 == 0:
            return el 
            break 
        
def punteggi(nomi : list, punteggio : list):
    return dict(zip(nomi, punteggio))

def sum_and_product(start, end):
    somma, prodotto = 0, 1 
    
    for num in range(start, end + 1):
        somma += num
        prodotto *= num
    
    return (somma, prodotto)

def tabelline(start, end):
    for num in range(start, end + 1):
        for mult in range(start, end + 1):
            print(f"{num} x {mult} = {num*mult}")
            
def enumerate_con_filtraggio(lista : list):
    return list(filter(lambda x: x[0] % 2 == 0, [(i, num) for i, num in enumerate(lista)]))

def combine_and_filter(l1 : list, l2 : list):
    return list(filter(lambda x : x[0] + x[1] >= 10, [(x, y) for x, y in zip(l1, l2)]))


"""
ESERCIZIO: Studenti e punteggi
Obiettivo: Data una lista di studenti e una lista di punteggi, 
scrivi un programma che crei un dizionario con gruppi di studenti basato sul punteggio. 
I gruppi devono essere suddivisi come segue:

"A": punteggio maggiore o uguale a 90
"B": punteggio maggiore o uguale a 75 ma inferiore a 90
"C": punteggio maggiore o uguale a 50 ma inferiore a 75
"D": punteggio inferiore a 50
"""

def studenti_e_punteggi(studenti: list, punteggi: list):
    L = [(s, p) for s, p in zip(studenti, punteggi)]
    out = {"A": [], "B": [], "C": [], "D": []}
    
    for s, p in L:
        if p >= 90:
            out["A"].append(s)
        
        if p >= 75 and p < 90:
            out["B"].append(s)
            
        if p >= 50 and p < 75:
            out["C"].append(s)
            
        if p < 50:
            out["C"].append(s)
            
    return out
    
print(primopari([1, 3, 4, 6, 7, 9, 10]))
print(sum_and_product(3, 15))
print(tabelline(1, 10))
print(enumerate_con_filtraggio([2, 4, 6, 4, 5, 9, 2, 3]))
print(combine_and_filter([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]))





    
    