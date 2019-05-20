'''Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron, a następnie:
Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.
Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich
Połącz dane w jeden ciąg book za pomocą spacji
Policz liczbę wszystkich znaków w napisie book
'''

book_title = input("Podaj tytuł książki: ")
book_author = input("Podaj nazwisko autora: ")
book_pages = input("Podaj ilość stron w książce: ")


print(book_title.isalpha())
print(book_pages.isdigit())

print("Tytuł ksiązki: ", book_title.title())
print("Nazwiko autora książki: ", book_author.title())

book = book_title + " " + book_author + " " + book_pages
print(book)
print(len(book))