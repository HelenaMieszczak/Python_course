# Utwórz dowolną krotkę zawierającą kilka wartości np. 10. Pozwól użytkownikowi podać dowolny index oraz wartość.
# Spróbuj w krotce podmienić wartość na zadanym indeksie. Obsłuż błąd


def get_user_input():
    while True:
        try:
            index = int(input("Podaj liczbę: "))
            value = input("Wpisz dowolną wartość: ")
            break
        except (ValueError, TypeError) as error:
            print(error, "Podaj wartość ponownie")

    return index, value


def change_value(seq, id_val):
    id, v = id_val
    try:
        seq[id] = v
    except TypeError:
        seq = list(seq)
        seq[id] = v

    return seq


def main():
    my_tuple = (2, 1.5, 'a', ".", 5, 8, 55, "b", "2", 4)

    new_data = get_user_input()
    tuple_to_newlist = change_value(my_tuple, new_data)
    print(my_tuple)
    print(tuple_to_newlist)


if __name__ == "__main__":
    main()
