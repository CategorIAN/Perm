from .CAT import CAT

class PermGroup(CAT):
    def __init__(self, gens):
        self.gens = gens
        d = 0
        for g in gens:
            if g.degree > d:
                d = g.degree
        self.degree = d

    def __str__(self):
        return "PermGroup:{}".format(self.gens)

    def identity(self):
        return self.gens[0].id

    def union(self, other):
        PermGroup(self.gens.union(other.gens))

    def __add__(self, other):
        PermGroup(self.gens.add(other))

    def SS(self, a):
        repr = {a:self.identity}
        for s in repr:
            for g in self.gens:
                r = g.act[s]
                if repr.get(r) is None:
                    repr[r] = repr[s] * g

    def orbit(self, a, x = None, gg = None):
        if x == None: x = {a}
        if gg == None: gg = self.gens

        y = set()
        for s in x:
            for g in gg:
                r = g.act[s]
                if r not in x:
                    y.add(r)

        for s in y:
            for g in self.gens:
                r = g.act[s]
                if r not in x or r not in y:
                    y.add(r)

        return x.union(y)

    def orbitStab(self, a, x = None, gg = None):
        M = set()
        if x is None: x = {a:self.identity}
        if gg is None: gg = self.gens

        y = {}
        for s in x:
            for g in gg:
                r = g.act[s]
                if x.get(r) is None:
                    y[r] = x[s] * g
                else:
                    M.add(x[s] * g * x[r].inv)

        for s in y:
            for g in self.gens:
                r = g.act[s]
                if x.get(r) is None:
                    if y.get(r) is None:
                        y[r] = y[s] * g
                    else:
                        M.add(y[s] * g * y[r].inv)
                else:
                    M.add(y[s] * g * x[r].inv)

        return (x.update(y), M)

    def schsims(self, base, perms):

        def partialbsgs(b, p):
            tt = self.gens.union(p)
            notbase = tt[0].keys().difference( b )
            groups = []
            max = 0
            for i in range(len(b)):
                groups[i] = PermGroup(set())
            for g in tt:
                x = g.movedpt(b)
                if x is None:
                    y = g.movedpt(notbase)
                    if y is not None:
                        b.append(y)
                        groups.append(PermGroup(set()))
                        notbase.remove(y)
                        max = len(b)
                        for i in range(max):
                            groups[i] = groups[i] + g + g.inv
                else:
                    dropout = b.index(x)
                    max = max(max, dropout)
                    for i in range(dropout + 1):
                        groups[i] = groups[i] + g + g.inv
            b = b[:max]
            groups = groups[:max]

            return groups

        def getlevels(base, groups, newgens, reprs, i):
            if i < 0:
                return BSGS(base, groups, reprs)
            else:
                (repr, tt) = groups[i].orbitStab(base[i], reprs[i], newgens[i])
                reprs[i] = repr
                for j in range(len(newgens)):
                    newgens[j] = newgens[j].clear()
                next = i - 1
                for g in tt:
                    (h, j) = self.strip(base, reprs, i + 1, g)
                    if not h.isID:
                        next = max(next, j)
                        for k in range(i + 1, j + 1):
                            groups[k] = groups[k] + h + h.inv
                            newgens[k] = newgens[k].update({h, h.inv})
                        if j == len(base):
                            y = h.movedpt()
                            base.append(y)
                            groups.append(PermGroup({h, h.inv}))
                            newgens.append({h, h.inv})
            return getlevels(base, groups, newgens, reprs, next)


        groups = partialbsgs(base, perms)
        newgens = []
        reprs = {}
        for i in range(len(groups)):
            newgens[i] = set()
            reprs[i] = {}

        return getlevels(base, groups, newgens, reprs, len(groups) - 1)

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
            gens1.add(self.identity.prod(g))
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
            gens1.add(self.identity.gridFromseq(g))
        return PermGroup(gens0.union(gens1))

    def gridFromseqinv(self):
        gens0 = set()
        for g in self.gens:
            gens0.add(g.gridFromseqinv)
        return PermGroup(gens0)

    def strip(self, base, reprs, start, g):
        def go(h, l):
            repr = reprs.get(start + l)
            if repr is None:
                return (h, start + l)
            else:
                u = repr.get(h.act[base[start + l]])
                if u is None:
                    return (h, start + l)
                else:
                    return go(h * u.inv, l + 1)
        return go(g, 0)


class BSGS:

    def __init__(self, base, groups, reprs):
        self.base = base
        self.groups = groups
        self.reprs = reprs

    def __str__(self):
        print("Base: {}, Groups: {}, Reprs: {}".format(self.base, self.groups, self.reprs))

    def contains(self, g):
        return PermGroup.strip(self.base, self.reprs, 0, g)




































