import random
from src.main.perm.Cycle import Cycle
from src.main.perm.PermGroup import PermGroup
from src.main.perm.PermCoset import PermCoset
from src.main.perm.Grid import Grid
from src.main.perm.PermCoset import Code

class RandomPerm:
    """
    A class used to create random algebraic objects and codes
    ...

    Methods
    -------
    cycle(degree)
        Returns a random cycle of the given degree

    perm(degree)
        Returns a random permutation of the given degree

    permgroup(degree)
        Returns a random permutation group of the given degree

    permcoset(degree)
        Returns a random permutation coset of the given degree

    code(a, b)
        Returns a random code of the given height and length

    """

    def cycle(self, degree):
        """ Returns a random cycle of the given degree

        :param degree: degree of the cycle
        :type degree: int
        :return: random cycle
        :rtype: Cycle
        """
        x = set(range(degree))
        c = []
        i = random.randint(0, degree)
        while i in x:
            c.append(i)
            x.remove(i)
            i = random.randint(0, degree)
        return Cycle(c)

    def perm(self, degree):
        """ Returns a random permutation of the given degree

        :param degree: degree of the permutation
        :type degree: int
        :return: random permutation
        :rtype: Perm
        """
        f = random.randint(0, degree)
        g = Cycle([])
        g.extend(degree)
        for i in range(f):
            g = g * self.cycle(degree)
        return g

    def permgroup(self, degree):
        """ Returns a random permutation group of the given degree

        :param degree: degree of the group
        :type degree: int
        :return: random permutation group
        :rtype: PermGroup
        """
        f = random.randint(0, degree)
        gens = []
        if f == 0 and degree > 0:
            f += 1
        for i in range(f):
            gens.append(self.perm(degree))
        return PermGroup(gens)

    def permcoset(self, degree):
        """ Returns a random permutation coset of the given degree

        :param degree: degree of the coset
        :type degree: int
        :return: random permutation coset
        :rtype: PermCoset
        """
        return PermCoset(self.permgroup(degree), self.perm(degree))

    def code(self, a, b):
        """ Returns a random code of the given height and length

        :param a: height of the code
        :type a: int
        :param b: length of the code
        :type b: int
        :return: random code
        :rtype: Code
        """
        c = random.randint(0, a * b)
        aa = tuple(range(a))
        bb = tuple(range(b))
        phi = set()
        for i in range(c):
            phi.add((random.choice(aa), random.choice(bb)))
        codegrid = Grid(aa, bb)
        return Code(phi, codegrid)


