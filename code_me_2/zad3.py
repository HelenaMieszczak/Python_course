#Stwórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy, utwórz nowy łańcuch s3, dołączając s2 w środku s1.

s1 = input("słowo 1 = ")
s2 = input("słowo 2 = ")

mid = len(s1) // 2
s3 = s1[mid:] + s2 + s1[:mid]

print(s3)