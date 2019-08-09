import random
from src.main.perm.Cycle import Cycle
from src.main.perm.PermGroup import PermGroup
from src.main.perm.PermCoset import PermCoset
from src.main.perm.Grid import Grid
from src.main.perm.PermCoset import Code

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
        g.extend(degree)
        for i in range(f):
            g = g * self.cycle(degree)
        return g

    def permgroup(self, degree):
        f = random.randint(0, degree)
        gens = []
        if f == 0 and degree > 0:
            f += 1
        for i in range(f):
            gens.append(self.perm(degree))
        return PermGroup(gens)

    def permcoset(self, degree):
        return PermCoset(self.permgroup(degree), self.perm(degree))

    def code(self, a, b):
        c = random.randint(0, a * b)
        aa = tuple(range(a))
        bb = tuple(range(b))
        phi = set()
        for i in range(c):
            phi.add((random.choice(aa), random.choice(bb)))
        codegrid = Grid(aa, bb)
        return Code(phi, codegrid)


