# Rozwiń kod bmi.py z pierwszych zajęć dodając teraz instrukcję warunkową, \
# która wyświetli w zależności od wyniku: niedowaga / waga normalna / nadwaga / otyłość.

weight = float(input("Podaj wagę (kg): "))
height = float(input("Podaj wzrost (m): "))
BMI = round(weight/(height**2),2)

#mniej niż 16 -  18,4 niedowaga
#18.5 - 24.99 - wartość prawidłowa
#25 - 30 - nadwaga
#powyżej 30 - otyłość

if BMI <= 18.4:
    print(BMI, '-', "niedowaga")
elif BMI >18.4 and BMI <= 24.99:
    print(BMI, '-', "waga normalna")
elif BMI > 24.99 and BMI <= 30:
    print(BMI, '-',"nadwaga")
else:
    print(BMI, '-', "otyłość")