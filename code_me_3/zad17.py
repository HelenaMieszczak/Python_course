# Pobierz od użytkownika dowolny tekst i wyświetl tylko te znaki, które są na pozycjach parzystych. \ Wykonaj na dwa
# sposoby - za pomocą pętli oraz przez string slicing ( ‘abrakadabra’ -> ‘baaar’).

sentence = input("Podaj dowolne wyrażenie: ")

print("***string slicing***")
print(sentence[1::2])

print("\n")
print("***loop***")


i = 1
for i in range(1,len(sentence)+1, 2):
    print(sentence[i])
    i = i + 2

