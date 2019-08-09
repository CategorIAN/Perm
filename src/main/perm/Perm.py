from .CAT import CAT
from .Grid import Grid
from .Combinatorics import Combinatorics as C
from copy import copy


class Perm(CAT):
    def __init__(self, act):
        self.act = act
        self.degree = len(act)


    def __repr__(self):
        if self.degree < 100:
            display = []
            for x in sorted(self.act.keys()):
                display.append(self(x))
            return "Perm{}".format(display)
        else:
            return "Perm of Degree {}".format(self.degree)

    def __call__(self, a): return self.act[a]

    def extend(self, deg):
        for i in range(self.degree, deg):
            self.act[i] = i
        self.degree = deg
        return self

    def __mul__(self, other):
        d = max(self.degree, other.degree)
        self.extend(d)
        other.extend(d)
        prodact = {}
        for i in self.act:
            prodact[i] = other(self(i))
        return Perm(prodact)

    def __eq__(self, other):
        for i in self.act:
            if self(i) != other(i):
                return False
        return True

    #==================================================

    def id(self):
        idact = {}
        for i in self.act:
            idact[i] = i
        return Perm(idact)

    def inv(self):
        invact = {}
        for k, v in self.act.items():
            invact[v] = k
        return Perm(invact)

    def movedpt(self, seq = None):
        if seq == None:
            pts = self.act
        else:
            pts = seq
        for i in pts:
            if self(i) != i:
                return i
        return None

    def isID(self):
        return self.movedpt() is None

    def strip(self, base, xs, gxs, l):
        g = copy(self)
        while True:
            if l < len(base):
                if g(base[l]) in xs[l]:
                    g = g * gxs[l][xs[l].index(g(base[l]))].inv()
                    l += 1
                else:
                    return (g, l)
            else:
                return (g, l)

    #=================================================

    def prod(self, other):
        prodact = {}
        for i in self.act:
            for j in other.act:
                prodact[(i, j)] = (self(i), other(j))
        return Perm(prodact)

    def diag(self):
        return self.prod(self)

    def prodinv_0(self):
        prodinvact = {}
        for i in self.act:
            prodinvact[i[0]] = self(i)[0]
        return Perm(prodinvact)

    def prodinv_1(self):
        prodinvact = {}
        for i in self.act:
            prodinvact[i[1]] = self(i)[1]
        return Perm(prodinvact)

    def seq(self):
        n = self.degree
        seqact = {}
        for i in range(C().nCks(n)):
            x = C().tuple(n, i)
            y = ()
            for j in x:
                y = y + (self(j),)
            seqact[x] = tuple(sorted(y))
        return Perm(seqact)

    def seqinv(self):
        x = ()
        for i in self.act:
            if len(x) < len(i):
                x = i
        seqinvact = {}
        for i in range(len(x)):
            seqinvact[x[i]] = self((x[i],))[0]
        return Perm(seqinvact)

    def gridFromseq(self, other):
        gridact = {}
        for i, j in self.act.items():
            for k, l in other.act.items():
                gridact[Grid(i, k)] = Grid(j, l)
        return Perm(gridact)

    def gridFromseqdiag(self):
        return self.gridFromseq(self)

    def griddiag(self):
        return self.grid(self)

    def gridFromseqinv_phi(self):
        seqact = {}
        for i, j in self.act.items():
           seqact[i.phi] = j.phi
        return Perm(seqact)

    def gridFromseqinv_psi(self):
        seqact = {}
        for i, j in self.act.items():
            seqact[i.psi] = j.psi
        return Perm(seqact)




































