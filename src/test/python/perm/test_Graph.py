from src.main.perm.Graph import Graph

def iso(ii = 10, d = 10):
    for i in range(ii):
        print("=====================")
        n1 = 4
        n2 = 4
        e1 = {(0, 1), (2, 3)}
        e2 = {(0, 2), (1, 3)}
        g1 = Graph(n1, e1)
        g2 = Graph(n2, e2)
        print(g1)
        print(g2)
        print(g1.iso(g2))


if __name__ == "__main__":
    iso(1, 1)



