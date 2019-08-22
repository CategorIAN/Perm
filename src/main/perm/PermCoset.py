from .PermGroup import PermGroup
from .CAT import CAT
from .Grid import Grid
from copy import copy


class Code:
    """
    A class representing a colored code

    ...

    Attributes
    -------
    pi: set
        a set of tuples of integers that determine what values of the code grid are colored

    codegrid: Grid
        a grid of integers for the code colorings

    Methods
    -------
    def trans(coset, grid)
        Returns permutation subcoset that maps the given subgrid's colors to colors of the code grid

    def stabilizer(coset)
        Returns permutation subcoset that preserves the code grid's colors

    """
    def __init__(self, pi, codegrid):
        """

        :param pi: the colored points of the code grid
        :type pi: set
        :param codegrid: the grid for the code
        :type codegrid: Grid
        """
        self.pi = pi
        self.codegrid = codegrid

    def __repr__(self):
        return "Code: {} / {}".format(self.pi, self.codegrid)

    def trans(self, coset, grid):
        """ Returns permutation subcoset that maps the given subgrid's colors to colors of the code grid

        :param coset: coset that can act on the code
        :type coset: PermCoset
        :param grid: subgrid of the code grid
        :type grid: Grid
        :return: subcoset that maps the given subgrid's colors to colors of the code grid
        :rtype: PermCoset
        """
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
                    c1 = self.trans(PermCoset(PermGroup(tt), g * coset.z), grid0)
                    #print("---------------")
                    c2 = self.trans(c1, grid1)
                    #print("add to union")
                    cosets.append(c2)
                return union(cosets)

    def stabilizer(self, coset):
        """ Returns permutation subcoset that preserves the code grid's colors

        :param coset: coset that can act on the code
        :type coset: PermCoset
        :return: the stabilizer coset
        :rtype: PermCoset
        """
        return self.trans(coset, self.codegrid)



class PermCoset(CAT):
    """
    A class representing a permutation coset

    ...

    Attributes
    -------
    L: PermGroup
        the permutation group of the coset

    z: Perm
        the coset representative

    degree: int
        the size of the domain of the permutations

    Methods
    -------
    intersection(other)
        Returns the intersection of this coset and another coset

    isEmpty
        Determines whether this coset's group has no generators

    prod(other)
        Returns a coset that acts on tuples of values according to this and another coset

    diag
        Returns the diagonal product of this coset

    prodinv_0
        Returns the first projection of this coset that acts on tuples

    prodinv_1
        Returns the second projection of this coset that acts on tuples

    seq
        Returns coset that acts on sequences of points according to how this coset acts on points

    seqinv
        Returns coset that acts on points according to how this coset acts on sequences of points

    gridFromseq(other)
        Returns coset that acts on grids according to how this coset and another coset acts on sequences

    gridFromseqdiag
        Returns the diagonal grid product from this sequence-acting coset

    griddiag
        Returns the diagonal grid product from this point-acting coset

    gridFromseq_phi
        Returns the coset that acts on row sequences from this coset that acts on grids

    gridFromseq_psi
        Returns the coset that acts on column sequences from this coset that acts on grids

    """
    def __init__(self, L, z):
        """

        :param L: the permutation group of the coset
        :type L: PermGroup
        :param z: the coset representative
        :type z: Perm
        """
        self.L = L
        self.z = z
        self.degree = max(self.L.degree, self.z.degree)

    def __repr__(self):
        if len(self.L.gens) == 0: return "None"
        else: return 'PermCoset: {} with rep {}'.format(self.L, self.z)

    def intersection(self, other):
        """ Returns the intersection of this coset and another coset

        :param other: another coset
        :type other: PermCoset
        :return: intersection of the cosets
        :rtype: PermCoset
        """
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
        """ Determines whether this coset's group has no generators

        :return: True iff its group has no generators
        :rtype: bool
        """
        return len(self.L.gens) == 0

    def prod(self, other):
        """ Returns a coset that acts on tuples of values according to this and another coset

        :param other: another coset
        :type other: PermCoset
        :return: direct product of cosets
        :rtype: PermCoset
        """
        return PermCoset(self.L.prod(other.L), self.z.prod(other))

    def diag(self):
        """ Returns the diagonal product of this coset

        :return: diagonal product coset
        :rtype: PermCoset
        """
        return PermCoset(self.L.diag(), self.z.diag())

    def prodinv_0(self):
        """ Returns the first projection of this coset that acts on tuples

        :return: coset acting on the first coordinates
        :rtype: PermCoset
        """
        return PermCoset(self.L.prodinv_0(), self.z.prodinv_0())

    def prodinv_1(self):
        """ Returns the second projection of this coset that acts on tuples

        :return: coset acting on the second coordinates
        :rtype: PermCoset
        """
        return PermCoset(self.L.prodinv_0(), self.z.prodinv_0())

    def seq(self):
        """ Returns coset that acts on sequences of points according to how this coset acts on points

        :return: coset of permutations of sequences
        :rtype: PermCoset
        """
        return PermCoset(self.L.seq(), self.z.seq())

    def seqinv(self):
        """ Returns coset that acts on points according to how this coset acts on sequences of points

        :return: coset of permutations of points
        :rtype: PermCoset
        """
        return PermCoset(self.L.seqinv(), self.z.seqinv())

    def gridFromseq(self, other):
        """ Returns coset that acts on grids according to how this coset and another coset act on sequences

        :param other: another coset of permutations of sequences
        :return: product of cosets that acts on grids
        :rtype: PermCoset
        """
        return PermCoset(self.L.gridFromseq(other.L), self.z.gridFromseq(other.z))

    def gridFromseqdiag(self):
        """ Returns the diagonal grid product from this sequence-acting coset

        :return: diagonal product of this coset that acts on grids
        :rtype: PermCoset
        """
        return PermCoset(self.L.gridFromseqdiag(), self.z.gridFromseqdiag())

    def griddiag(self):
        """ Returns the diagonal grid product from this point-acting coset

        :return: diagonal product of this coset that acts on grids
        :rtype: PermCoset
        """
        return PermCoset(self.L.griddiag(), self.z.griddiag())

    def gridFromseqinv_phi(self):
        """ Returns the coset that acts on row sequences from this coset that acts on grids

        :return: coset of permutations of row sequences
        :rtype: PermCoset
        """
        return PermCoset(self.L.gridFromseqinv_phi(), self.z.gridFromseqinv_phi())

    def gridFromseqinv_psi(self):
        """ Returns the coset that acts on column sequences from this coset that acts on grids

        :return: coset of permutations of column sequences
        :rtype: PermCoset
        """
        return PermCoset(self.L.gridFromseqinv_psi(), self.z.gridFromseqinv_psi())












