class Grid:
    """
    A class used to represent a grid of integers

    ...

    Attributes
    -------
    phi: tuple
        tuple of integers encoding the row numbers of the grid

    psi: tuple
        tuple of integers encoding the column numbers of the grid

    Methods
    -------
    points(Pi)
        Returns subset of points that are contained in this grid

    split
        Returns a pair of halves of this grid

    """

    def __init__(self, phi, psi):
        """

        :param phi: the row numbers of the grid
        :type phi: tuple
        :param psi: the column numbers of the grid
        :type psi: tuple
        """
        self.phi = phi
        self.psi = psi

    def __eq__(self, other):
        return self.phi == other.phi and self.psi == other.psi

    def __repr__(self):
        return "Grid:({}, {})".format(self.phi, self.psi)

    def __hash__(self):
        return hash((self.phi, self.psi))

    def __lt__(self, other):
        if self.phi != other.phi:
            return self.phi < other.phi
        else:
            return self.psi < other.psi


    def points(self, Pi):
        """ Returns the set of points that are contained in this grid

        :param Pi: set of tuples of integers
        :type Pi: set
        :return: subset of Pi contained in this grid
        :rtype: set
        """
        S = set()
        for p in Pi:
            if p[0] in self.phi and \
            p[1] in self.psi:
                S.add(p)
        return S

    def split(self):
        """ Returns a pair of halves of this grid

        :return: pair of grids by splitting this grid in half
        :rtype: tuple
        """
        m1 = len(self.phi) // 2
        if m1 > 0:
            return (Grid(self.phi[:m1], self.psi), Grid(self.phi[m1:], self.psi))
        else:
            m2 = len(self.psi) // 2
            return (Grid(self.phi, self.psi[:m2]), Grid(self.phi, self.psi[m2:]))



