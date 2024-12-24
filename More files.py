import random as r

#Funzione che prenda solo i caratteri numerici, separati in una lista e ordinati e li inserisca in un nuovo file
def takenumb(file, fileotp):
    with open(file, "r") as f:
        testo = "".join([char if char.isnumeric() or char == " " else " " for char in f.read()])
        lista = sorted([int(cifra) for numero in testo.split() for cifra in numero])
    
    with open(fileotp, "w") as fo:
        fo.write(" ".join(map(str, lista)))
        return lista
    


#Funzione che prenda soltanto i caratteri concatenati per più di 4 volte
def takechars(file):
    with open(file, "r") as f:
        testo = "".join(char if char.isalpha() or char == " " else " " for char in f.read())
        return [el for el in testo.split() if len(el) > 4]
    
    
    
"""
Scrivi un programma che esegua le seguenti operazioni sui file:

Crea un file chiamato dati.txt e scrivici una serie di numeri interi casuali (tra 1 e 1000), uno per riga. Il file deve contenere esattamente 1000 numeri.

Leggi il file dati.txt e:

Calcola la somma dei numeri pari e la somma dei numeri dispari.
Trova il numero massimo e minimo presente nel file.
Crea un secondo file chiamato risultati.txt e scrivici:

La somma dei numeri pari.
La somma dei numeri dispari.
Il numero massimo.
Il numero minimo.
Modifica il file dati.txt in modo che:

I numeri pari siano moltiplicati per 2.
I numeri dispari siano sostituiti con il loro quadrato.
Mantieni ogni numero nella propria riga.
Alla fine, il programma deve stampare il numero totale di righe del file modificato (dati.txt) e verificare che sia ancora 1000.
"""
def operations(dati, risultati):
    with open(dati, "w") as dw:
        for i in range(1000):
            dw.write(str(r.randint(1, 1000)) + "\n")
    
    with open(dati, "r") as dr:
        nums = list(map(int, dr.read().split()))
        
        pari = sum([el for el in nums if el % 2 == 0])
        dispari = sum([el for el in nums if el % 2 == 1])
        massimo, minimo = max(nums), min(nums)
        
    with open(dati, "w") as dm:
        newnums = list(map(lambda x : x*2 if x%2 == 0 else x**2, nums))
        
        dm.write("".join([str(el) + "\n" for el in newnums]))
    
    with open(risultati, "w") as rw:
        rw.write("La somma dei numeri pari è: " + str(pari) + "\n"
                 "La somma dei numeri dispari è: " + str(dispari) + "\n"
                 "Il numero più grande è: " + str(massimo) + "\n"
                 "Il numero più piccolo è: " + str(minimo))
        
    return len(newnums), len(newnums) == 1000



"""
Leggere il file sondaggio.txt.
Validare i dati (es. verificare che il formato sia corretto, nessun campo mancante).
Calcolare e stampare:
Numero totale di partecipanti.
Percentuale di risposte "Si" e "No".
Età media dei partecipanti.
Numero di partecipanti per sesso.
Generare un nuovo file analisi_sondaggio.txt con i risultati dell'analisi.
"""

def sondaggio(file, risultati, errori):
    with open(file, "r") as f:
        header = f.readline().strip().split(",")
        list_sondaggi = [dict(zip(header, lines.strip().split(","))) for lines in f]
        
        list_sondaggi = list({k: int(v) if v.isdigit() else v for k, v in diz.items()} for diz in list_sondaggi)
        
        partecipanti = len(list_sondaggi)
        età = sum(diz["Età"] for diz in list_sondaggi) / partecipanti
        
        maschi = femmine = Si = No = 0
        
        for diz in list_sondaggi:
            if diz["Sesso"] == "M":
                maschi += 1
            elif diz["Sesso"] == "F":
                femmine += 1
            
            if diz["Risposta"] == "Si":
                Si += 1
            elif diz["Risposta"] == "No":
                No += 1
         
        perc_si = (Si / partecipanti) * 100
        perc_no = (No / partecipanti) * 100
            
    with open(risultati, "w") as r:
        r.write("Numero di partecipanti: " + str(partecipanti) + "\n"
                "Età media: " + str(int(età)) + "\n"
                "Percentuale di si: " + str(perc_si) + "\n"
                "Percentuale di no: " + str(perc_no) + "\n"
                "Numero di maschi: " + str(maschi) + "\n"
                "Numero di femmine: " + str(femmine) + "\n")
        
   
    
print(takenumb("morefiles.txt", "morefilesotp.txt"))
print(takechars("morefiles.txt"))
print(operations("dati.txt", "risultati.txt"))
print(sondaggio("sondaggio.txt", "analisi_sondaggio.txt", "errori_sondaggio.txt"))