# Napisz program zmieniający skalę w stopniach Fahrenheita na nasz Celcjusza.\
# Program powinen wykonać się w pętli od 0 do 200 stopni Fahrenheit, co 20 stopni.

#C = 5/9 * (F - 32) # wzór Celsjusz → Fahrenheit

start = 0
limit = 200
step = 20

fahr = start
while (fahr <= 200):
    celsius = 5/9 * (fahr - 32)
    print(fahr, "\t", celsius)
    fahr = fahr + step