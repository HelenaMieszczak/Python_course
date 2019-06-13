#  Stwórz własną implementację kolejki FIFO. Klasa Kolejka powinna na starcie przyjmować listę elementów.
#  Wśród metod powinny się znaleźć takie jak: wyswietlenie kolejki, sprawdzenie czy jest pusta,
#  dodanie elementu do kolejki (put), wyjęcie elementu z kolejki (get).
# Utwórz kilka obiektów klasyz różnymi parametrami.


class Queue:
    def __init__(self, items):
        self.items = items

    def show_q(self):
        print(self.items)

    def is_empty(self):
        return bool(len(self.items))

    def put_item(self):
        item_num = int(input("Ile elementów chcesz dodac? "))
        for n in range(0, item_num):
            new_items = str(input())
            self.items.append(new_items)
            print(self.items)

    def get_item(self):
        shorter_list = self.items.pop(0)
        return shorter_list


def main():
    my_q = Queue(["*", "d", "f"])
    print(my_q.items)
    print(my_q.is_empty())
    print(my_q.put_item())
    print((my_q.get_item()))
    print(my_q.items)


if __name__ == "__main__":
    main()

