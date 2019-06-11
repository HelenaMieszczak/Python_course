cookies = int(input("How many cookies will you bake?"))
people = int(input("Number of people ?"))

def party_planner(cookies, people):
    leftovers = None
    num_each = None
    try:
        num_each = cookies // people
        leftovers = cookies % people
    except ZeroDivisionError as error:
        print("Somebody will come for sure!", error)

    return print((f"Cookies per person: {num_each} and cookies left: {leftovers}."))

party_planner(cookies, people)