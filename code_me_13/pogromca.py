# Dodaj do gry warunek zastrzelenia: Gracz razi wroga. Wykorzystaj moduł random,
# aby wylosować celność strzału - w skali od 1 do 10. Gracz musi trafić conajmniej 3 punkty, w przeciwnym razie to wróg wygrywa np.
# zje gracza. Obiekt hero wywołuje metodę win() (wygraj) dla obiektu enemy. Alien mlaska na zakończenie i idzie spać.

import random


class Player(object):

    def blast(self, enemy):
        print("gracz razi wroga")
        shoot = random.randint(0, 10)
        if shoot >= 3:
            print(shoot)
            enemy.die()
        else:
            print(shoot)
            enemy.win()



class Alien(object):

    def die(self):
        print('Obcy z trudem łapie oddech, "To już koniec. Ale prawdziwie wielki koniec... \n',
              'Walczyliśmy do końca. Nie, to nie koniec. Larwy moje jednoczcie się! \n',
              'O tak one pomszczą mnie pewnego dnia... \n',
              'Żegnaj, okrutny Wszechświecie! Umieeeraaam"')

    def win(self):
        print("Obcy Cie zjadł")


if __name__ == "__main__":
    print('************ Śmierć Obcego ************\n')
    hero = Player()
    invader = Alien()
    hero.blast(invader)
    input('\n\nAby zakończyć program, naciśnij klawisz Enter.')