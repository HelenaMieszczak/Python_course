#W wierszu policz wystąpienie każdego wyrazu, zignoruj wielkość liter.
"""Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""
#Zadbaj o sposób wyświetlania np.:
#szybko : 5
#zbudź : 1

poem = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""

poem = poem.lower()
poem = poem.replace(",", " ")
poem = poem.split()
print(poem)

words = {}

for i in poem:
    if i in words:
        words[i] += 1
    else:
        words[i] = 1

print(words)

for k, v in words.items():
    print(k, ":", v)