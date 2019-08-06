import random
from src.main.perm.Cycle import Cycle
from src.main.perm.PermGroup import PermGroup


class RandomPerm:
    def __init__(self):
        pass

    def cycle(self, degree):
        x = set(range(degree))
        c = []
        i = random.randint(0, degree)
        while i in x:
            c.append(i)
            x.remove(i)
            i = random.randint(0, degree)
        return Cycle(c)

    def perm(self, degree):
        f = random.randint(0, degree)
        g = Cycle([])
        for i in range(f):
            g = g * self.cycle(degree)
        return g

    def permgroup(self, degree):
        f = random.randint(0, degree)
        gens = set()
        for i in range(f):
            gens.add(self.perm(degree))
        return PermGroup(gens)

