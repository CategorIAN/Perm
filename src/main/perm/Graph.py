from .PermCoset import Code
from .Grid import Grid
from .Perm import Perm
from .PermCoset import PermCoset
from .PermGroup import PermGroup
from .Cycle import Cycle
from copy import copy


class Graph(Code):
    def __init__(self, n, edges):
        self.n = n
        self.vertices = set(range(n))
        self.edges = edges
        grid = Grid(tuple(range(n)), tuple(range(n)))
        symedges = set()
        for e in edges:
            symedges.update({e, (e[1], e[0])})
        super().__init__(symedges, grid)

    def __repr__(self):
        return "Vertices: {}, Edges: {}".format(self.vertices, self.edges)

    def id(self, degree):
        idact = {}
        for i in range(degree):
            idact[i] = i
        return Perm(idact)

    def flip(self):
        flipact = {}
        for i in self.codegrid.phi:
            flipact[i] = i + self.n
            flipact[i + self.n] = i
        return Perm(flipact)

    def iso(self, other):
        if self.n != other.n:
            return PermCoset(PermGroup([]), self.id(self.n + other.n))
        else:
            gens = [Cycle(list(range(0, self.n))).extend(2 * self.n), Cycle(list(range(self.n, 2 * self.n)))]
            if self.n > 1:
                gens = gens + [Cycle([0, 1]).extend(2 * self.n), Cycle([self.n, self.n + 1]).extend(2 * self.n)]
            L = PermGroup(gens).griddiag()
            z = self.flip().griddiag()
            coset = PermCoset(L, z)
            pi = copy(self.pi)
            for p in other.pi:
                pi.add((p[0] + self.n, p[1] + self.n))
            phi = tuple(range(2 * self.n))
            psi = tuple(range(2 * self.n))
            grid = Grid(phi, psi)
            return Code(pi, grid).stabilizer(coset).gridinv_0()







