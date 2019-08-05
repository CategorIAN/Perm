from random import randrange
from src.main.perm.PermCoset import PermCoset
from src.main.perm.Perm import Perm
from src.main.perm.PermGroup import PermGroup
from src.main.perm.RandomPerm import RandomPerm

def mul_degree(I, d = 10):
    R = RandomPerm()
    for i in range(I):
        a = randrange(0, 10)
        b = randrange(0, 10)
        g = R.perm(a)
        print("g is {}".format(g))
        h = R.perm(b)
        print("h is {}".format(h))
        m = g * h
        print("g * h is {}".format(m))
        #assert (m == g)

if __name__ == '__main__':
    mul_degree(20, 10)



