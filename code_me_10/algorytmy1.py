# napisz kod funkcji, szukającej email na liśćie emaili


def search_email():
    email_list = ["aaa@wp.pl", "ccc@onet.pl", "bbbb@eu.pl"]
    email = input("Ktorego maila szukasz? ")
    for i in email_list:
        if i == email:
            print("Twój email został znaleziony: ", i)
        else:
            print("Nie znaleziono podanego maila.")
            break


search_email()