# Funzione da usare:
def load_file(filename: str):
    with open(filename) as f:
        return f.read()


# Dato il nome di un file di testo, ritornare il numero di volte che una parola
# e' presente nel file. La ricerca ignora la distinzione tra maiuscole e minuscole,
# e la punteggiatura.
def search_word(filename: str, word: str):
    with open(filename, "r") as f:
        return sum("".join(char for char in parole.lower() if char.isalnum()) == word for parole in f.read().split())
    

# Dato il nome di un file di testo, si ritorna una "tabella" formata da una
# lista di dizionari. Nel file, la prima riga contiene i nomi delle colonne
# (chiavi nel dizionario) e le righe contengono i valori, tutti separati da
# spazi.
def load_table(filename: str):
    with open(filename, "r") as f:
        header = f.readline().split()
        return list(dict(zip(header, lines.split())) for lines in f)


# Caricare una tabella in modo simile al precente. In questo caso però, i valori
# che rappresentano numeri interi vanno convertiti in interi e non lasciati come
# stringhe.
def load_data(filename: str):
    with open(filename, "r") as f:
        header = f.readline().split()
        table = list(dict(zip(header, lines.split())) for lines in f)
        
        return list({k: int(v) if v.isdigit() else v for k, v in diz.items()} for diz in table)


# Caricare una tabella in modo simile al precente. In questo caso però, i valori
# sono separati da virgole e ci posso essere valori non presenti (due virgole
# consecutive). I valori mancanti devono essere aggiunti se `empties==True` come
# None, oppure essere omessi.
def load_csv(filename: str, empties: bool):
    with open(filename, "r") as f:
        header = f.readline().strip().split(",")
        
        def zipper(lines, empties):
            lista = list()
            
            for el in lines.strip().split(","):
                if el.isdigit():
                    lista.append(int(el))
                elif not el and empties:
                    lista.append(None)
                else:
                    lista.append(el)
            return lista
        
        data = list(dict(zip(header, zipper(lines, empties))) for lines in f)
        
        for diz in data:
            templista = list()
            for k, v in diz.items():
                if diz[k] == "":
                    templista.append(k)
            
            for el in templista:
                del diz[el]
        
        return data
        
        
# Dato una file CSV, che si carica con la funzione precedente, ritornare un
# dizionario con la somma dei valori di ogni colonna numerica.
# Usare la funzione load_csv(), con la variable empties data a vostra scelta.
def column_stats(filename: str):
    diz = dict()
        
    for loadeddiz in load_csv(filename, True):
        for k, v in loadeddiz.items():
            if isinstance(v, int):
                if not k in diz:
                    diz[k] = v
                else:
                    diz[k] += v

    return diz