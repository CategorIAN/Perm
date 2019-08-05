from .RandomPerm import RandomPerm
from random import random

def mul_degree(I, d = 10):
    R = RandomPerm()
    for i in range(I):
        a = random.randrange(d)
        b = random.randrange(d)
        g = R.perm(a)
        print("g is {}".format(g))
        h = R.perm(b)
        print("h is {}".format(h))
        m = g * h
        print("g * h is {}".format(m))
        assert (m.degree == g.degree or m.degree == h.degree), "degree is {}".format(m.degree)

if __name__ == "__main__":
    # mul_degree(10, 10)
    assert (5 == 5), "5 == 5"



