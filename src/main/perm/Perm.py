from .CAT import CAT
from .Grid import Grid
from .Combinatorics import Combinatorics as C


class Perm(CAT):
    def __init__(self, act):
        self.act = act
        self.degree = len(act)

    def __repr__(self):
        if self.degree < 100:
            return "Perm{}".format(self.act)
        else:
            return "Perm of Degree {}".format(self.degree)

    def __call__(self, a):
        return self.act[a]

    def extend(self, deg):
        for i in range(self.degree, deg):
            self.act[i] = i
        self.degree = deg

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

    #=================================================


    def sum(self, other):
        sumact = {}
        for i in self.act:
            sumact[(i, None)] = (self(i), None)
        for i in other.act:
            sumact[(None, i)] = (None, other(i))

        return Perm(sumact)

    def prod(self, other):
        prodact = {}
        for i in self.act:
            for j in other.act:
                prodact[(i, j)] = (self(i), other(j))
        return Perm(prodact)

    def prodinv(self):
        prodinvact = {}
        for i in self.act:
            prodinvact[i[0]] = self(i)[0]
        return Perm(prodinvact)

    def seq(self):
        n = self.degree
        seqact = {}
        for i in range(C().nCks(n)):
            x = tuple(C().subset(n, i))
            y = []
            for j in x:
                y.append(self(j))
            seqact[x] = tuple(y)
        return Perm(seqact)

    def seqinv(self):
        x = ()
        for i in self.act:
            if len(x) < len(i):
                x = i
        y = self(x)
        seqinvact = {}
        for i in range(len(x)):
            seqinvact[x[i]] = y[i]
        return Perm(seqinvact)

    def gridFromseq(self, other):
        gridact = {}
        for i, j in self.act.items():
            for k, l in other.act.items():
                gridact[Grid(i, k)] = Grid(j, l)
        return Perm(gridact)


    def gridFromseqinv(self):
        seqact = {}
        for i, j in self.act.items():
           seqact[i.phi] = j.phi
        return Perm(seqact)




































