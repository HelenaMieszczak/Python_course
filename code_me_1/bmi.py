
weight = int(input("Podaj wagę (kg): "))
height = float(input("Podaj wzrost (m):"))
BMI = round(weight / (height ** 2), 2)
print("Your BMI is: " , BMI)
