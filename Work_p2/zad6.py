#Palindrom to wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej np.: Kobyła ma mały bok. \
# Pozwól użytkownikowi wprowadzić dowolne zdanie. Następnie sprawdź czy wprowadzone wyrażenie jest palindromem.

sentence = input("Wpisz dwole słowo lub zdanie: ")
sentence1 = sentence.replace(" ", "")

s1 = sentence1[0:]
s2 = sentence1[::-1]
print(s1, s2)
print(s1 == s2)




