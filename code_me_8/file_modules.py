#Stwórz moduł, który zajmuje się jedynie otwieraniem plików - oferuje bezpieczny sposób odczytu oraz bezpieczny zapis.
# Funkcja czytająca pliki sprawdza najpierw czy dany plik istnieje oraz czy jest niepusty.
# Funkcja zapisująca do pliku chroni przed nadpisaniem istniejącego pliku.

import os


def check_file(user_file):
    if os.path.isfile(user_file) and os.stat(user_file).st_size > 0:
        return True
    else:
        return False


def open_user_file(user_file):
    if check_file(user_file):
        with open(user_file, encoding="utf-8") as f:
            print(f.read())


def save_user_file(user_save, user_data):
    with open(user_save, "a") as s:
        s.write(user_data)






