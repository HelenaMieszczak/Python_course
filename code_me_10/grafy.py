graph = {
    0 : [1, 2, 3],
    1 : [0, 4],
    2 : [0, 3],
    3 : [0, 2, 4],
    4 : [1, 3],
    5 : [2, 6],
    6 : [4, 5]
}


def generate_edges():
    for k, v in graph.items():
        for val in v:
            print(k, "-", val)


generate_edges()
