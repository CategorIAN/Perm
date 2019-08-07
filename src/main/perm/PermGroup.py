from .CAT import CAT
from copy import copy

class PermGroup(CAT):
    def __init__(self, gens):
        self.gens = gens
        d = 0
        for g in gens:
            if g.degree > d:
                d = g.degree
        self.degree = d

    def __repr__(self):
        return "PermGroup:{}".format(self.gens)

    def identity(self):
        return self.gens[0].id()

    def union(self, other):
        PermGroup(self.gens + other.gens)

    def __add__(self, other):
        self.gens.append(other)
        return self

    def SchStr(self, a):
        pts = [a]
        trvs = [self.identity()]
        for s in pts:
            for g in self.gens:
                r = g(s)
                if r not in pts:
                    pts.append(r)
                    trvs.append(trvs[pts.index(s)] * g)
        return (pts, trvs)

    def orbit(self, a, x = None, gg = None):
        if x is None: x = [a]
        if gg is None: gg = self.gens

        y = []
        for s in x:
            for g in gg:
                r = g(s)
                if r not in x and r not in y:
                    y.append(r)

        for s in y:
            for g in self.gens:
                r = g(s)
                if r not in x and r not in y:
                    y.append(r)

        return x + y

    def orbitstab(self, a, x = None, gx = None, gens = None):
        M = []
        if x is None: x = [a]; gx = [self.identity()]
        if gens is None: gens = self.gens

        y = []
        gy = []
        for s in x:
            for g in gens:
                r = g(s)
                if r not in x and r not in y:
                    y.append(r)
                    gy.append(gx[x.index(s)] * g)
                elif r in x:
                    M.append(gx[x.index(s)] * g * gx[x.index(r)].inv())
                else:
                    M.append(gx[x.index(s)] * g * gy[y.index(r)].inv())

        for s in y:
            for g in self.gens:
                r = g(s)
                if r not in x and r not in y:
                    y.append(r)
                    gy.append(gy[y.index(s)] * g)
                elif r in x:
                    M.append(gy[y.index(s)] * g * gx[x.index(r)].inv())
                else:
                    M.append(gy[y.index(s)] * g * gy[y.index(r)].inv())

        return (x + y, gx + gy, M)

    def schsims(self, base = None, perms = None):

        def partialbsgs(b, p):
            if b is None: b = []
            if p is None: p = []
            tt = self.gens + p
            groups = []
            m = 0
            for i in range(len(b)):
                groups.append(PermGroup([]))
            for g in tt:
                x = g.movedpt(b)
                if x is None:
                    y = g.movedpt()
                    if y is not None:
                        b.append(y)
                        groups.append(PermGroup([]))
                        m = len(b)
                        for i in range(m):
                            groups[i] = groups[i] + g
                            groups[i] = groups[i] + g.inv()
                else:
                    dropout = b.index(x)
                    m = max(m, dropout + 1)
                    for i in range(dropout + 1):
                        groups[i] = groups[i] + g
                        groups[i] = groups[i] + g.inv()
            b = b[:m]
            groups = groups[:m]

            return (b, groups)

        def getlevels(b, gg, newgens, xs, gxs, i):
            if i < 0:
                return BSGS(b, gg, (xs, gxs))
            else:
                (x, gx, tt) = gg[i].orbitstab(b[i], xs[i], gxs[i], newgens[i])
                xs[i] = x
                gxs[i] = gx
                newgens[i].clear()
                next = i - 1
                for g in tt:
                    (h, j) = self.strip(b, xs, gxs, i + 1, g)
                    if not h.isID():
                        next = max(next, j)
                        if j == len(base):
                            y = h.movedpt()
                            b.append(y)
                            gg.append(PermGroup([]))
                            newgens.append([])
                            xs.append([])
                            gxs.append([])
                        for k in range(i + 1, j + 1):
                            gg[k] = gg[k] + h + h.inv()
                            newgens[k] = newgens[k] + [h, h.inv()]
            return getlevels(b, gg, newgens, xs, gxs, next)

        base, groups = partialbsgs(base, perms)

        newgens = []
        xs = []
        gxs = []
        for i in range(len(groups)):
            xs.append(None)
            gxs.append(None)
            newgens.append(copy(groups[i].gens))

        return getlevels(base, groups, newgens, xs, gxs, len(groups) - 1)

    def atkinson(self, a, b):
        if a < b: bs = {b:a}; explore = [b]
        else: bs = {a:b}; explore = [a]

        for i in explore:
            for g in self.gens:
                if bs[g.act[i]] != bs[g.act[bs[i]]]:
                    c = min(bs[g.act[i]], bs[g.act[bs[i]]])
                    d = max(bs[g.act[i]], bs[g.act[bs[i]]])
                    bs[d] = c
                    explore.append(d)
        for i, j in bs.items:
            while j != bs[j]:
                j = bs[j]
                bs[i] = j

    def isprimitive(self):
        for i in self.gens[0].act:
            if len(self.atkinson(0, i).values()) > 1:
                return False
        return True

    def sum(self, other):
        gens0 = set()
        gens1 = set()
        for g in self.gens:
            gens0.add(g.sum(other.identity))
        for g in other.gens:
            gens1.add(g.sum(self.identity))
        return PermGroup(gens0.union(gens1))

    def prod(self, other):
        gens0 = set()
        gens1 = set()
        for g in self.gens:
            gens0.add(g.prod(other.identity))
        for g in other.gens:
            gens1.add(self.identity().prod(g))
        return PermGroup(gens0.union(gens1))

    def prodinv(self):
        gens0 = set()
        for g in self.gens:
            gens0.add(g.prodinv)
        return PermGroup(gens0)

    def seq(self):
        gens0 = set()
        for g in self.gens:
            gens0.add(g.seq)
        return PermGroup(gens0)

    def seqinv(self):
        gens0 = set()
        for g in self.gens:
            gens0.add(g.seqinv)
        return PermGroup(gens0)

    def gridFromseq(self, other):
        gens0 = set()
        gens1 = set()
        for g in self.gens:
            gens0.add(g.gridFromseq(other.identity))
        for g in other.gens:
            gens1.add(self.identity().gridFromseq(g))
        return PermGroup(gens0.union(gens1))

    def gridFromseqinv(self):
        gens0 = set()
        for g in self.gens:
            gens0.add(g.gridFromseqinv)
        return PermGroup(gens0)

    def strip(self, base, xs, gxs, start, g):
        l = start
        while True:
            if l < len(base):
                if g(base[l]) in xs[l]:
                    g = g * gxs[l][xs[l].index(g(base[l]))].inv()
                    l += 1
                    continue
                else:
                    return (g, l)
            else:
                return (g, l)

class BSGS:

    def __init__(self, base, groups, reprs):
        self.base = base
        self.groups = groups
        self.reprs = reprs

    def __repr__(self):
        return "Base: {}, Groups: {}, Reprs: {}".format(self.base, self.groups, self.reprs)

    def contains(self, g):
        return PermGroup.strip(PermGroup([]), self.base, self.reprs[0], self.reprs[1], 0, g)




































