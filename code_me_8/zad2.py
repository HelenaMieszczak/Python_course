#Stwórz moduł, który zajmuje się jedynie otwieraniem plików - oferuje bezpieczny sposób odczytu oraz bezpieczny zapis.
# Funkcja czytająca pliki sprawdza najpierw czy dany plik istnieje oraz czy jest niepusty.
# Funkcja zapisująca do pliku chroni przed nadpisaniem istniejącego pliku.

import file_modules


def main():
    print("***MENU***")
    choice = input("Wybierz: \n1 - otwórz plik\n2 - zapisz plik")
    if choice == "1":
        open_file()
    elif choice == "2":
        save_file()


def open_file():
    filename = input("Podaj nazwę pliku: ")
    if file_modules.check_file(filename):
        file_modules.open_user_file(filename)
    else:
        print("Dany plik nie istnieje.")


def save_file():
    user_save = input("Podaj nazwe pliku:")
    user_data = input("Tresc:")
    user_save = user_save + ".txt"
    file_modules.save_user_file(user_save, user_data)


main()

