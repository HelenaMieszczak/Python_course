# Zapytaj użytkownika o numer od 1 do 100, jeśli użytkownik zgadnie liczbę ukrytą przez programistę \
# wyświetl komunikat “gratulacje!”, w przeciwnym razie “pudło!”.

user_num = int(input("Podaj dowolną liczbę od 1 do 100: "))
programmer_num = 50

if user_num == programmer_num:
    print("Gratulacje!")
else:
    print("Pudło!")