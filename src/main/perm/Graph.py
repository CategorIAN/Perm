from perm import Code, Grid, PermCoset, Perm, SymGroup

class Graph(Code):
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        grid = Grid(list(vertices), list(vertices))
        symedges = set()
        for e in edges:
            symedges.update({e, (e[1], e[0])})
        super(symedges, grid)

    def id(self):
        idact = {}
        for i in self.vertices:
            idact[i] = i
        return Perm(idact)

    def trans(self, other):
        transact = {}
        for i in self.vertices:
            transact[(i, None)] = (None, i)
        for i in other.vertices:
            transact[(None, i)] = (i, None)
        return Perm(transact)

    def iso(self, other):
        if len(self.vertices) != len(other.vertices):
            return PermCoset(set(), self.id.sum(other.id))
        else:
            L = SymGroup(len(self.vertices)).sumdiag.griddiag
            z = self.trans(other).griddiag
            coset = PermCoset(L, z)
            pi = set()
            for p in self.pi:
                pi.add(((p[0], None), (p[1], None)))
            for p in other.pi:
                pi.add(((None, p[0]), (None, p[1])))
            phi = []
            psi = []
            for i in self.codegrid.phi:
                phi.append((i, None))
            for i in other.codegrid.phi:
                phi.append((None, i))
            for i in self.codegrid.psi:
                psi.append((i, None))
            for i in other.codegrid.psi:
                psi.append((None, i))
            grid = Grid(phi, psi)
            return Code(pi, grid).stabilizer(coset).gridinv







