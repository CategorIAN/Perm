from .PermCoset import Code
from .Grid import Grid
from .Perm import Perm
from .PermCoset import PermCoset
from .PermGroup import PermGroup
from .Cycle import Cycle
from copy import copy


class Graph(Code):
    """
    A class used to represent a graph of integers by its adjacency matrix

    ...

    Attributes
    -------
    n: int
        the number of vertices of the graph

    vertices: set
        a set of integers representing the vertices of the graph

    edges: set
        a set of size 2 tuples of integers that represent directed edges

    Methods
    -------
    id(degree)
        Returns the identity permutation of a given degree

    flip
        Returns a vertex permutation that permutes two graphs of size n

    iso(other)
        Returns the edge preserving permutation coset that permutes this and another graph

    """
    def __init__(self, n, edges):
        """

        :param n: the number of vertices of the graph
        :type n: int
        :param edges: the set of directed edges
        :type edges: set
        """
        self.n = n
        self.vertices = set(range(n))
        self.edges = edges
        grid = Grid(tuple(range(n)), tuple(range(n)))
        symedges = set()
        for e in edges:
            symedges.update({e, (e[1], e[0])})
        super().__init__(symedges, grid)

    def __repr__(self):
        return "Vertices: {}, Edges: {}".format(self.vertices, self.edges)

    def id(self, degree):
        """ Returns the identity permutation of a given degree

        :param degree: size of the domain of permutation
        :type degree: int
        :return: identity permutation
        :rtype: Perm
        """
        idact = {}
        for i in range(degree):
            idact[i] = i
        return Perm(idact)

    def flip(self):
        """ Returns a vertex permutation that permutes two graphs of size n

        :return: permutation of integers
        :rtype: Perm
        """
        flipact = {}
        for i in self.codegrid.phi:
            flipact[i] = i + self.n
            flipact[i + self.n] = i
        return Perm(flipact)

    def iso(self, other):
        """ Returns the edge preserving permutation coset that permutes this and another graph

        :param other: another graph
        :type other: Graph
        :return: the graph isomorphism coset
        :rtype: PermCoset
        """
        if self.n != other.n:
            return PermCoset(PermGroup([]), self.id(self.n + other.n))
        else:
            gens = [Cycle(list(range(0, self.n))).extend(2 * self.n), Cycle(list(range(self.n, 2 * self.n)))]
            if self.n > 1:
                gens = gens + [Cycle([0, 1]).extend(2 * self.n), Cycle([self.n, self.n + 1]).extend(2 * self.n)]
            L = PermGroup(gens).griddiag()
            z = self.flip().griddiag()
            coset = PermCoset(L, z)
            pi = copy(self.pi)
            for p in other.pi:
                pi.add((p[0] + self.n, p[1] + self.n))
            phi = tuple(range(2 * self.n))
            psi = tuple(range(2 * self.n))
            grid = Grid(phi, psi)
            return Code(pi, grid).stabilizer(coset).gridinv_0()







