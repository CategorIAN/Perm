from math import factorial
from .CAT import CAT
from .Grid import Grid


class Perm(CAT):
    def __init__(self, act):
        self.act = act
        self.degree = len(act)

    def __str__(self):
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
        for k, v in self.act.items:
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
#------------------------------------------------------------------------------------
    def nCk (self, n, k): #This computes the number of k-subsets from a set of size n.
        f = factorial
        return f(n) // f(k) // f(n-k)

    def nCks(self, n):
        N = 0
        for k in range(n + 1):
            N += self.nCk(n, k)
        return N

    def ksubset(self, n, k, i): #This returns the subset of a given index.
        p = 0
        s = 0
        S = set()
        while len(S) < k:
            p += self.nCk(n - s - 1, k - len(S) - 1)
            if i < p:
                S.add(s)
            s += 1
        return S

    def subset(self, n, i):
        j = i
        k = 0
        while True:
            if j < self.nCk(n, k):
                return self.ksubset(n, k, j)
            j -= self.nCk(n, k)
            k += 1
#----------------------------------------------------------------------

    def seq(self):
        n = self.degree
        seqact = {}
        for i in range(self.nCks(n)):
            x = list(self.subset(n, i))
            y = []
            for j in x:
                y.append(self(j))
            seqact[x] = y
        return Perm(seqact)

    def seqinv(self):
        x = []
        for i in self.act:
            if len(x) < len(i):
                x = i
        y = self(x)
        seqinvact = {}
        for i in range(len(x)):
            seqinvact[x[i]] = y[i]

    def gridFromseq(self, other):
        gridact = {}
        for i, j in self.act.items:
            for k, l in other.act:
                gridact[Grid(i, k)] = Grid(j, l)
        return Perm(gridact)


    def gridFromseqinv(self):
        seqact = {}
        for i, j in self.act.items:
           seqact[i.phi] = j.phi

    #Need random.




































