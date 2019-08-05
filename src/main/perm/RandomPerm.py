import random
import perm

class RandomPerm:

    def cycle(self, degree):
        x = set(range(degree))
        c = []
        i = random.randint(0, degree)
        while i not in x:
            c.append(i)
            x.remove(i)
            i = random.randint(0, degree)
        return perm.Cycle(c)

    def perm(self, degree):
        f = random.randint(0, degree)
        g = perm.Cycle([degree - 1])
        for i in range(f):
            g = g * self.cycle(degree)

    def permgroup(self, degree):
        f = random.randint(0, degree)
        gens = set()
        for i in range(f):
            gens.add(self.perm(degree))

