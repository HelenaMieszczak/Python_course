# Napisz program zmieniający skalę w stopniach Fahrenheita na nasz Celcjusza.\
# Program powinen wykonać się w pętli od 0 do 200 stopni Fahrenheit, co 20 stopni.
# C = 5/9 * (F - 32) # wzór Celsjusz → Fahrenheit
# Napisz rozwiązanie zarówno z użyciem pętli while jak i for

print("***Pętla while***")
start = 0
limit = 200
step = 20

fahr = start
while (fahr <= 200):
    celsius = 5 / 9 * (fahr - 32)
    print(fahr, "\t", celsius)
    fahr = fahr + step

print("\n")
print("***Pętla for***")

start = 0
limit = 200
step = 20
fahr = start

for step in range(0,200,20):
    celsius = 5 / 9 * (step - 32)
    print(step, "\t", celsius)
