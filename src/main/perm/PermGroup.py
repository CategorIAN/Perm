from .CAT import CAT
from copy import copy
from .Perm import Perm

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
        if len(self.gens) > 0:
            return self.gens[0].id()
        else: return Perm({})

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
                else:
                    if r in x:
                        h = gx[x.index(s)] * g * gx[x.index(r)].inv()
                    else:
                        h = gx[x.index(s)] * g * gy[y.index(r)].inv()
                    if h not in M:
                        M.append(h)

        for s in y:
            for g in self.gens:
                r = g(s)
                if r not in x and r not in y:
                    y.append(r)
                    gy.append(gy[y.index(s)] * g)
                else:
                    if r in x:
                        h = gy[y.index(s)] * g * gx[x.index(r)].inv()
                    else:
                        h = gy[y.index(s)] * g * gy[y.index(r)].inv()
                    if h not in M:
                        M.append(h)

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
                    (h, j) = g.strip(b, xs, gxs, i + 1)
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
        bs = {}
        for i in range(self.degree):
            bs[i] = i
        if a < b: bs[b] = a; explore = [b]
        elif b < a: bs[a] = b; explore = [a]
        else: explore = []
        for i in explore:
            for g in self.gens:
                if bs[g(i)] != bs[g(bs[i])]:
                    c = min(bs[g(i)], bs[g(bs[i])])
                    d = max(bs[g.act[i]], bs[g.act[bs[i]]])
                    bs[g(i)] = c
                    bs[g(bs[i])] = c
                    explore.append(d)
        for i, j in bs.items():
            k = bs[j]
            ll = []
            while k != j:
                ll.append(i)
                i = j
                j = k
                k = bs[j]
            for l in ll:
                bs[l] = k
        return bs

    def isprimitive(self):
        for i in range(1, self.degree):
            if len(set(self.atkinson(0, i).values())) > 1:
                return False
        return True

    def prod(self, other):
        gens0 = []
        gens1 = []
        id0 = copy(self.identity())
        id1 = copy(other.identity())
        if len(id0.act) == 0:
            id0 = Perm({0:0})
        if len(id1.act) == 0:
            id1 = Perm({0:0})
        for g in self.gens:
            gens0.append(g.prod(id1))
        for g in other.gens:
            gens1.append(id0.prod(g))
        return PermGroup(gens0 + gens1)

    def diag(self):
        gens = []
        for g in self.gens:
            gens.append(g.diag())
        return PermGroup(gens)

    def prodinv_0(self):
        gens0 = []
        for g in self.gens:
            gens0.append(g.prodinv_0())
        return PermGroup(gens0)

    def prodinv_1(self):
        gens1 = []
        for g in self.gens:
            gens1.append(g.prodinv_1())
        return PermGroup(gens1)

    def seq(self):
        gens0 = []
        for g in self.gens:
            gens0.append(g.seq())
        return PermGroup(gens0)

    def seqinv(self):
        gens0 = []
        for g in self.gens:
            gens0.append(g.seqinv())
        return PermGroup(gens0)

    def gridFromseq(self, other):
        gens0 = []
        gens1 = []
        id0 = copy(self.identity())
        id1 = copy(other.identity())
        if len(id0.act) == 0:
            id0 = Perm({():()})
        if len(id1.act) == 0:
            id1 = Perm({():()})
        for g in self.gens:
            gens0.append(g.gridFromseq(id1))
        for g in other.gens:
            gens1.append(id0.gridFromseq(g))
        return PermGroup(gens0 + gens1)

    def gridFromseqdiag(self):
        gens = []
        for g in self.gens:
            gens.append(g.gridFromseqdiag())
        return PermGroup(gens)

    def griddiag(self):
        gens = []
        for g in self.gens:
            gens.append(g.griddiag())
        return PermGroup(gens)

    def gridFromseqinv_phi(self):
        gens0 = []
        for g in self.gens:
            gens0.append(g.gridFromseqinv_phi())
        return PermGroup(gens0)

    def gridFromseqinv_psi(self):
        gens1 = []
        for g in self.gens:
            gens1.append(g.gridFromseqinv_psi())
        return PermGroup(gens1)



class BSGS:

    def __init__(self, base, groups, reprs):
        self.base = base
        self.groups = groups
        self.reprs = reprs

    def __repr__(self):
        return "Base: {}, Groups: {}, Reprs: {}".format(self.base, self.groups, self.reprs)

    def contains(self, g):
        return g.strip(self.base, self.reprs[0], self.reprs[1], 0)




































