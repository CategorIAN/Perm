from .CAT import CAT
from .Grid import Grid
from .Combinatorics import Combinatorics as C
from copy import copy


class Perm(CAT):
    """
    A class representing a permutation of values

    ...

    Attributes
    -------
    act: dict
        a dictionary mapping keys to values of the same type which encodes the action of the permutation

    degree: int
        the size of the domain of this permutation

    Methods
    -------
    extend(deg)
        Extends the degree of this permutation by adding fixed points to the domain

    id
        Returns the identity permutation of this permutation's degree

    inv
        Returns the inverse permutation of this permutation

    movedpt
        Returns a point in the domain moved by the permutation

    isID
        Determines whether this permutation is the identity permutation

    strip(base, xs, gxs, l)
        Returns the residue permutation and drop out level for the Schreier-Sims algorithm

    prod(other)
        Returns a permutation that acts on tuples of values according to this and another permutation

    diag
        Returns the diagonal product of this permutation

    prodinv_0
        Returns the first projection of this permutation of tuples

    prodinv_1
        Returns the second projection of this permutation of tuples

    seq
        Returns permutation of sequences of points according to this permutation of points

    seqinv
        Returns permutaton of points according to this permutation of sequences of points

    gridFromseq(other)
        Returns permutation of grids from this sequence permutation and another sequence permutation

    gridFromseqdiag
        Returns the grid product from this sequence permutation

    griddiag
        Returns the diagonal grid product from this permutation

    gridFromseq_phi
        Returns the row sequence permutation of this grid permutation

    gridFromseq_psi
        Returns the column sequence permutation of this grid permutation

    """
    def __init__(self, act):
        """

        :param act: the action of the permutation
        :type act: dict
        """
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

    def extend(self, deg):
        """ Extends the degree of this permutation by adding fixed points to the domain

        :param deg: the new degree of the permutation
        :type deg: int
        :return: permutation with new degree
        :rtype: Perm
        """
        for i in range(self.degree, deg):
            self.act[i] = i
        self.degree = deg
        return self

    def id(self):
        """ Returns the identity permutation of this permutation's degree

        :return: identity permutation
        :rtype: Perm
        """
        idact = {}
        for i in self.act:
            idact[i] = i
        return Perm(idact)

    def inv(self):
        """ Returns the inverse permutation of this permutation

        :return: inverse permutation
        :rtype: Perm
        """
        invact = {}
        for k, v in self.act.items():
            invact[v] = k
        return Perm(invact)

    def movedpt(self, seq = None):
        """ Returns a point in a domain that is not fixed by the permutation

        :param seq: optional subcollection of points to act on instead of its full domain
                    (default is None)
        :type seq: list, optional
        :return: point not fixed by permutation
        :rtype: the type of the points of this permutation
        """
        if seq == None:
            pts = self.act
        else:
            pts = seq
        for i in pts:
            if self(i) != i:
                return i
        return None

    def isID(self):
        """ Determines whether this permutation is the identity permutation

        :return: True iff this is the identity on its domain
        :rtype: bool
        """
        return self.movedpt() is None

    def strip(self, base, xs, gxs, l):
        """ Returns the residue permutation and drop out level of a stabilizer transversal chain

        :param base: base points for the group action
        :type base: list
        :param xs: list of base point orbits
        :type xs: list
        :param gxs: list of base point transporter permutations
        :type gxs: list
        :param l: starting base point level
        :type l: int
        :return: residue permutation and drop out level
        :rtype: tuple
        """
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
        """ Returns a permutation that acts on tuples of values according to this and another permutation

        :param other: another permutation
        :type other: Perm
        :return: direct product of two permutations
        :rtype: Perm
        """
        prodact = {}
        for i in self.act:
            for j in other.act:
                prodact[(i, j)] = (self(i), other(j))
        return Perm(prodact)

    def diag(self):
        """ Returns the diagonal product of this permutation

        :return: diagonal product of this permutation
        :rtype: Perm
        """
        return self.prod(self)

    def prodinv_0(self):
        """ Returns the first projection of this permutation of tuples

        :return: permutation that acts on values of the first coordinate type
        :rtype: Perm
        """
        prodinvact = {}
        for i in self.act:
            prodinvact[i[0]] = self(i)[0]
        return Perm(prodinvact)

    def prodinv_1(self):
        """ Returns the second projection of this permutation of tuples

        :return: permutation that acts on values of the second coordinate type
        :rtype: Perm
        """
        prodinvact = {}
        for i in self.act:
            prodinvact[i[1]] = self(i)[1]
        return Perm(prodinvact)

    def seq(self):
        """ Returns permutation of sequences of points according to this permutation of points

        :return: permutation of sequences
        :rtype: Perm
        """
        n = self.degree
        seqact = {}
        for i in range(pow(2, n)):
            x = C().tuple(n, i)
            y = ()
            for j in x:
                y = y + (self(j),)
            seqact[x] = tuple(sorted(y))
        return Perm(seqact)

    def seqinv(self):
        """ Returns permutaton of points according to this permutation of sequences of points

        :return: permutation of points
        :rtype: Perm
        """
        x = ()
        for i in self.act:
            if len(x) < len(i):
                x = i
        seqinvact = {}
        for i in range(len(x)):
            seqinvact[x[i]] = self((x[i],))[0]
        return Perm(seqinvact)

    def gridFromseq(self, other):
        """ Returns permutation of grids from this sequence permutation and another sequence permutation

        :param other: another permutation of sequences
        :type other: Perm
        :return: permutation of grids
        :rtype: Perm
        """
        gridact = {}
        for i, j in self.act.items():
            for k, l in other.act.items():
                gridact[Grid(i, k)] = Grid(j, l)
        return Perm(gridact)

    def gridFromseqdiag(self):
        """ Returns the grid product from this sequence permutation

        :return: diagonal product permutation of grids
        :rtype: Perm
        """
        return self.gridFromseq(self)

    def griddiag(self):
        """ Returns the diagonal grid product from this permutation

        :return: diagonal product permutation of grids
        :rtype: Perm
        """
        return self.grid(self)

    def gridFromseqinv_phi(self):
        """ Returns the row sequence permutation of this grid permutation

        :return: permutation of row sequences
        :rtype: Perm
        """
        seqact = {}
        for i, j in self.act.items():
           seqact[i.phi] = j.phi
        return Perm(seqact)

    def gridFromseqinv_psi(self):
        """ Returns the column sequence permutation of this grid permutation

        :return: permutation of column sequences
        :rtype: Perm
        """
        seqact = {}
        for i, j in self.act.items():
            seqact[i.psi] = j.psi
        return Perm(seqact)




































