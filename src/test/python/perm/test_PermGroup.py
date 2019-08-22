from src.main.perm.PermGroup import PermGroup
from src.main.perm.SymGroup import SymGroup
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
        r = Cycle([0,1,2,3,4,5])
        s = Cycle([0, 5]) * Cycle([1, 4]) * Cycle([2, 3])
        gg = PermGroup([r, s])
        print("----")
        print(gg)
        print(gg.schsims())

def atkinson(ii = 10, d = 10):
    for i in range(ii):
        r = Cycle([0, 1, 2, 3, 4, 5])
        s = Cycle([0, 5]) * Cycle([1, 4]) * Cycle([2, 3])
        gg = PermGroup([r, s])
        print(gg.atkinson(0, 3))

def isprimitive(ii = 10, d = 10):
    for i in range(ii):
        r = Cycle([0, 1, 2, 3, 4, 5])
        s = Cycle([0, 5]) * Cycle([1, 4]) * Cycle([2, 3])
        gg = PermGroup([r, s])
        hh = SymGroup(list(range(5)))
        print(gg.isprimitive())
        print(hh.isprimitive())

def sum(ii = 10, d = 10):
    for i in range(ii):
        a = randrange(0, d)
        b = randrange(0, d)
        gg = R().permgroup(a)
        hh = R().permgroup(b)
        print(gg.sum(hh))

def prod(ii = 10, d = 10):
    for i in range(ii):
        a = randrange(0, d)
        b = randrange(0, d)
        gg = R().permgroup(a)
        hh = R().permgroup(b)
        print("---")
        print(gg)
        print(hh)
        print(gg.prod(hh))

def prodinv(ii = 10, d = 10):
    for i in range(ii):
        a = randrange(0, d)
        b = randrange(0, d)
        gg = R().permgroup(a)
        hh = R().permgroup(b)
        print("---")
        print(gg)
        print(hh)
        x = gg.prod(hh)
        print(x)
        print(x.prodinv())

def seq(ii = 10, d = 10):
    for i in range(ii):
        a = randrange(0, d)
        gg = R().permgroup(a)
        print("---")
        print(gg)
        print(gg.seq())

def seqinv(ii = 10, d = 10):
    for i in range(ii):
        a = randrange(0, d)
        gg = R().permgroup(a)
        print("---")
        print(gg)
        print(gg.seq())
        print(gg.seq().seqinv())

def gridFromseq(ii = 10, d = 10):
    for i in range(ii):
        a = randrange(0, d)
        b = randrange(0, d)
        gg = R().permgroup(a)
        hh = R().permgroup(b)
        print("---")
        print(gg)
        print(gg.seq())
        print(hh)
        print(hh.seq())
        print(gg.seq().gridFromseq(hh.seq()))

def gridFromseqinv(ii = 10, d = 10):
    for i in range(ii):
        a = randrange(0, d)
        b = randrange(0, d)
        gg = R().permgroup(a)
        hh = R().permgroup(b)
        print("---")
        print(gg)
        print(gg.seq())
        print(hh)
        print(hh.seq())
        print(gg.seq().gridFromseq(hh.seq()))
        print(gg.seq().gridFromseq(hh.seq()).gridFromseqinv())

def grid(ii = 10, d = 10):
    for i in range(ii):
        a = randrange(0, d)
        b = randrange(0, d)
        gg = R().permgroup(a)
        hh = R().permgroup(b)
        print("---")
        print(gg)
        print(hh)
        print(gg.grid(hh))

if __name__ == "__main__":
    schsims(1, 1)

