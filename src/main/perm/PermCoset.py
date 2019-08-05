from .PermGroup import PermGroup
from .CAT import CAT
from .Grid import Grid


class Code:
    def __init__(self, pi, codegrid):
        self.pi = pi

    def trans(self, coset, grid):
        def union(cc):
            L = None
            z = None
            for c in cc:
                if not c.isEmpty:
                    if L is None:
                        L = c.L
                        z = c.z
                    else:
                        L.add(c.z * z.inv)
            if L is None:
                return PermCoset(PermGroup(set()), cc[0].z.id)
            else:
                return PermCoset(L, z)
        if coset.isEmpty: PermCoset(PermGroup(set()), coset.z.id)
        else:
            I = grid.points(self.pi)
            J = coset.z.act[grid].points(self.pi)
            if len(I) != len(J):
                return PermCoset(PermGroup(set()), coset.z.id)
            elif len(I) == 0:
                return coset
            elif len(I) == 1:
                i = I.pop()
                j = J.pop()
                tt = coset.L.orbitStab(Grid([i[0]], [i[1]]))
                target = coset.z.inv.act[Grid([j[0]], [j[1]])]
                g = tt[0].get(target)
                if g == None:
                    return PermCoset(PermGroup(set()), coset.z.id)
                else:
                    return PermCoset(PermGroup(tt[1]), g * coset.z)
            else:
                grid0, grid1 = grid.split()
                tt = coset.L.orbitStab(grid0)
                cosets = []
                for t in tt[0].values:
                    cosets.append(self.trans(self.trans(PermCoset(PermGroup(tt[1]), t * coset.z), grid0), grid1))
                return union(cosets)

    def stabilizer(self, coset):
        return self.trans(coset, self.codegrid)



class PermCoset(CAT):
    def __init__(self, L, z):
        self.L = L
        self.z = z
        self.degree = max(L.degree, z.degree)

    def __str__(self):
        return 'PermCoset: {} with rep {}'.format(self.L, self.z)

    def intersection(self, other):
        pi = set()
        phi = []
        psi = []
        degree = min(self.degree, other.degree)

        for i in range(degree):
            pi.add((i, i))
        for i in range(self.degree):
            phi.append(i)
        for i in range(other.degree):
            psi.append(i)

        coset = self.grid(other)
        return Code(pi, Grid(phi, psi)).stabilizer(coset)


    def sum(self, other):
        return PermCoset(self.L.sum(other.L), self.z.sum(other))

    def prod(self, other):
        return PermCoset(self.L.prod(other.L), self.z.prod(other))

    def prodinv(self):
        return PermCoset(self.L.prodinv, self.z.prodinv)

    def seq(self):
        return PermCoset(self.L.seq, self.z.seq)

    def seqinv(self):
        return PermCoset(self.L.seqinv, self.z.seqinv)

    def gridFromseq(self, other):
        return PermCoset(self.L.gridFromseq(other.L), self.z.gridFromseq(other.z))

    def gridFromseqinv(self):
        return PermCoset(self.L.gridFromseqinv, self.z.gridFromseqinv)

    def isEmpty(self):
        return len(self.L.gens) == 0










