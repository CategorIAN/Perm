from .PermGroup import PermGroup
from .CAT import CAT
from .Grid import Grid
from copy import copy


class Code:
    def __init__(self, pi, codegrid):
        self.pi = pi
        self.codegrid = codegrid

    def __repr__(self):
        return "Code: {} / {}".format(self.pi, self.codegrid)

    def trans(self, coset, grid, stop):
        #if stop == 2: return coset
        #print("==========================================================")
        #print("Coset is {}".format(coset.gridinv_0()))
        #print("Other Coset is {}".format(coset.gridinv_1()))
        #print("Grid is {}".format(grid))
        def union(cc):
            L = None
            z = None
            for c in cc:
                if not c.isEmpty():
                    if L is None:
                        L = copy(c.L)
                        z = copy(c.z)
                    else:
                        L + (c.z * z.inv())
            if L is None:
                return PermCoset(PermGroup([]), cc[0].z.id())
            else:
                return PermCoset(L, z)

        if coset.isEmpty():
            #print("Stabilizer of Empty Coset is Empty")
            return PermCoset(PermGroup([]), coset.z.id())

        else:
            I = grid.points(self.pi)
            J = coset.z(grid).points(self.pi)
            if len(I) != len(J):
                #print("Different Sizes of Points")
                return PermCoset(PermGroup([]), coset.z.id())
            elif len(I) == 0:
                #print("No points to preserve so it is the full coset.")
                return coset
            elif len(I) == 1:
                #print("Point Stabilizer")
                i = I.pop()
                j = J.pop()
                (x, gx, tt) = coset.L.orbitstab(Grid((i[0],), (i[1],)))
                target = coset.z.inv()(Grid((j[0],), (j[1],)))
                if target in x:
                    g = gx[x.index(target)]
                    return PermCoset(PermGroup(tt), g * coset.z)
                else:
                    return PermCoset(PermGroup([]), coset.z.id())
            else:
                #print("Take union of cosets.")
                grid0, grid1 = grid.split()
                (x, gx, tt) = coset.L.orbitstab(grid0)
                cosets = []
                for g in gx:
                    #print("~~~~~~~~~~~~~~~~")
                    c1 = self.trans(PermCoset(PermGroup(tt), g * coset.z), grid0, stop + 1)
                    #print("---------------")
                    c2 = self.trans(c1, grid1, stop + 1)
                    #print("add to union")
                    cosets.append(c2)
                return union(cosets)

    def stabilizer(self, coset):
        return self.trans(coset, self.codegrid, 0)



class PermCoset(CAT):
    def __init__(self, L, z):
        self.L = L
        self.z = z
        self.degree = max(self.L.degree, self.z.degree)

    def __repr__(self):
        if len(self.L.gens) == 0: return "None"
        else: return 'PermCoset: {} with rep {}'.format(self.L, self.z)

    def intersection(self, other):
        pi = set()
        phi = tuple(range(self.degree))
        psi = tuple(range(other.degree))
        degree = min(self.degree, other.degree)

        for i in range(degree):
            pi.add((i, i))

        coset = self.grid(other)
        print(coset)
        c = Code(pi, Grid(phi, psi))
        print(c)
        newgridcoset = c.stabilizer(coset)
        print(newgridcoset)
        print(newgridcoset.gridFromseqinv_phi())
        return Code(pi, Grid(phi, psi)).stabilizer(coset).gridinv_0()

    def isEmpty(self):
        return len(self.L.gens) == 0

    def prod(self, other):
        return PermCoset(self.L.prod(other.L), self.z.prod(other))

    def diag(self, other):
        return PermCoset(self.L.diag(), self.z.diag())

    def prodinv(self):
        return PermCoset(self.L.prodinv(), self.z.prodinv())

    def seq(self):
        return PermCoset(self.L.seq(), self.z.seq())

    def seqinv(self):
        return PermCoset(self.L.seqinv(), self.z.seqinv())

    def gridFromseq(self, other):
        return PermCoset(self.L.gridFromseq(other.L), self.z.gridFromseq(other.z))

    def gridFromseqdiag(self):
        return PermCoset(self.L.gridFromseqdiag(), self.z.gridFromseqdiag())

    def griddiag(self):
        return PermCoset(self.L.griddiag(), self.z.griddiag())

    def gridFromseqinv_phi(self):
        return PermCoset(self.L.gridFromseqinv_phi(), self.z.gridFromseqinv_phi())

    def gridFromseqinv_psi(self):
        return PermCoset(self.L.gridFromseqinv_psi(), self.z.gridFromseqinv_psi())












