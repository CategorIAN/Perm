from src.main.perm.PermGroup import PermGroup
from src.main.perm.RandomPerm import RandomPerm as R
from random import randrange
from src.main.perm.Cycle import Cycle


def orbit(ii = 10, d = 10):
    for i in range(ii):
        a = randrange(1, d)
        b = randrange(0, a)
        gg = R().permgroup(a)
        print("----")
        print(gg)
        print(b)
        print(gg.orbit(b))
        print(gg.SchStr(b))


def SchStr(ii = 10, d = 10):
    for i in range(ii):
        a = randrange(1, d)
        b = randrange(0, a)
        gg = R().permgroup(a)
        print("----")
        print(gg)
        print(b)
        print(gg.SchStr(b))


def orbitstab(ii = 10, d = 10):
    for i in range(ii):
        a = randrange(1, d)
        b = randrange(0, a)
        gg = R().permgroup(a)
        print("----")
        print(gg)
        print(b)
        print(gg.orbitstab(b))


def schsims(ii = 10, d = 10):
    for i in range(ii):
        a = randrange(1, d)
        r = Cycle([0,1,2,3,4,5])
        s = Cycle([0, 5]) * Cycle([1, 4]) * Cycle([2, 3])
        gg = PermGroup([r, s])
        print("----")
        print(gg)
        print(gg.schsims())



if __name__ == "__main__":
    schsims(1, 5)

