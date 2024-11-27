titoli = ["Il Signore degli Anelli", "Harry Potter e la Pietra Filosofale", "Orgoglio e Pregiudizio", "Il Grande Gatsby"]
autori = ("J.R.R. Tolkien", "J.K. Rowling", "Jane Austen", "F. Scott Fitzgerald")
generi = {"Fantasy", "Romanzo", "Classico"}
catalogo = {
    "Il Signore degli Anelli": ("J.R.R. Tolkien", "Fantasy"),
    "Harry Potter e la Pietra Filosofale": ("J.K. Rowling", "Fantasy"),
    "Orgoglio e Pregiudizio": ("Jane Austen", "Classico"),
    "Il Grande Gatsby": ("F. Scott Fitzgerald", "Romanzo")
}

#Convertire tutti i titoli in minuscolo e rimuovere eventuali spazi superflui.
#Contare il numero di vocali in ciascun titolo.
def count_and_convert(titles):
    return ({titolo: sum(titolo.lower().count(vocale) for vocale in "aeiou") for titolo in titles}, 
            [titolo.lower().strip().replace("  ", " ") for titolo in titles])

#Aggiungi un nuovo titolo alla lista di titoli: "Il Codice da Vinci".
titoli.append("Il Codice da Vinci")

#Ordina i titoli alfabeticamente
titoli.sort()

#Aggiungere un nuovo genere al set: "Thriller".
generi.add("Thriller")

#Verifica se un genere è presente nel set
def check_gen(gen):
    return gen in generi

#Aggiungi il libro appena inserito alla lista con l'autore Dan Brown e il genere "Thriller".
catalogo["Il Codice da vinci"] = ("Dan Brown", "Fantasy")

#Trova tutti i libri appartenenti a un certo genere
def search_gen(gen):
    return list(k for k, v in catalogo.items() if v[1].lower() == gen.lower())

#Il numero totale di libri per ogni genere presente.
def books_for_gen():
    return {genere: len([k for k, v in catalogo.items() if v[1].lower() == genere.lower()]) for genere in generi}

print(count_and_convert(titoli))
print(check_gen("Fantasy"))
print(search_gen("Fantasy"))

print(books_for_gen())
    