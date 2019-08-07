from random import randrange
from src.main.perm.RandomPerm import RandomPerm as R
from src.main.perm.Combinatorics import Combinatorics as C

def mul(ii = 10, d = 10):
    for i in range(ii):
        a = randrange(0, d)
        b = randrange(0, d)
        g = R().perm(a)
        print("g is {}".format(g))
        h = R().perm(b)
        print("h is {}".format(h))
        m = g * h
        print("g * h is {}".format(m))

def eq(ii = 10, d = 10):
    for i in range(ii):
        g1 = R().perm(randrange(0, d))
        g2 = R().perm(randrange(0, d))
        g3 = R().perm(randrange(0, d))
        m1 = g1 * g2
        m2 = g2 * g3
        print("----")
        print(m1 * g3)
        print(g1 * m2)
        assert(m1 * g3 == g1 * m2), "Associativity"

def id(ii = 10, d = 10):
    for i in range(ii):
        g = R().perm(randrange(0, d))
        print("---")
        print(g)
        print(g.id())
        print(g * g.id())
        assert(g * g.id() == g and g.id() * g == g), "Identity"

def inv(ii = 10, d = 10):
    for i in range(ii):
        g = R().perm(randrange(0, d))
        print("---")
        print(g)
        print(g.inv())
        print(g * g.inv())
        assert(g * g.inv() == g.id() and g.inv() * g == g.id()), "Inverses"

def movedpt(ii = 10, d = 10):
    for i in range(ii):
        g = R().perm(randrange(0, d))
        p = randrange(0, d)
        print("---")
        print(g)
        print(g.movedpt())

def sum(ii = 10, d = 10):
    for i in range(ii):
        g = R().perm(randrange(0, d))
        h = R().perm(randrange(0, d))
        print("---")
        print(g)
        g2 = g * g
        h2 = h * h
        print(h)
        print(g.sum(h))
        print(g.sum(h) * g.sum(h))
        print(g2.sum(h2))
        assert(g.sum(h) * g.sum(h) == g2.sum(h2))

def prod(ii = 10, d = 10):
    for i in range(ii):
        g = R().perm(randrange(0, d))
        h = R().perm(randrange(0, d))
        print("---")
        print(g)
        g2 = g * g
        h2 = h * h
        print(h)
        print(g.prod(h))
        print(g.prod(h) * g.prod(h))
        print(g2.prod(h2))
        assert(g.prod(h) * g.prod(h) == g2.prod(h2))

def prodinv(ii = 10, d = 10):
    for i in range(ii):
        g = R().perm(randrange(0, d))
        h = R().perm(randrange(0, d))
        print("---")
        print(g)
        print(h)
        print(g.prod(h))
        print(g.prod(h).prodinv())
        assert(g.prod(h).prodinv() == g)

def seq(ii = 10, d = 10):
    for i in range(ii):
        g = R().perm(randrange(0, d))
        print("---")
        print(g)
        print(g.seq())

def seqinv(ii = 10, d = 10):
    for i in range(ii):
        g = R().perm(randrange(0, d))
        print("---")
        print(g)
        h = g.seq()
        print(h)
        print(h.seqinv())
        assert(g.seq().seqinv() == g)

def gridFromseq(ii = 10, d = 10):
    for i in range(ii):
        g = R().perm(randrange(0, d))
        h = R().perm(randrange(0, d))
        print("---")
        print(g)
        print(h)
        print(g.seq())
        print(h.seq())
        print(g.seq().gridFromseq(h.seq()))

def gridFromseqinv(ii = 10, d = 10):
    for i in range(ii):
        g = R().perm(randrange(0, d))
        h = R().perm(randrange(0, d))
        m = g.seq().gridFromseq(h.seq())
        n = m.gridFromseqinv()
        print(g)
        print(h)
        print(m)
        print(n)

def subset(ii = 10):
    for i in range(ii):
        n = 5
        k = 3
        print("---")
        for j in range(C().nCk(n, k)):
            print(C().ksubset(n, k, j))

def grid(ii = 10, d = 10):
    for i in range(ii):
        g = R().perm(randrange(0, d))
        h = R().perm(randrange(0, d))
        m = g.grid(h)
        n = m.gridinv()
        print("----")
        print(g)
        print(h)
        print(m)
        print(n)


if __name__ == '__main__':
    grid(10, 4)




