# Sprawdź jak wygląda kod modułu antigravity. Korzystając z tego samego sposobu otwarcia dowolnego url pozwól użytkownikowi podać adres www
# Pamiętaj sprawdzić czy url jest prawidłowy może zaczynać się:
# https://
# http://
# www
# bez www
# Może się kończyć za pomocą:
# .pl
# .com
# Jeśli podany adres nie jest linkiem, podnieś wyjątek URLError, który będzie informował, że url jest nieprawidłowy.
# Nie masz dość? Swietnie! Przepisz to zadanie za pomocą wyrażeń regularnych (RegEx)

import webbrowser
import urllib


def open_site(site):
    if site.endswith(".pl") or site.endswith("com"):
        webbrowser.open(site)
        if site.startswith("https://") or site.startswith("http://") or site.startswith("www"):
            webbrowser.open(site)
    else:
        raise urllib.URLError("Wrong site address")


def main():
    user_site = input("Enter site address: ")
    open_site(user_site)


main()

