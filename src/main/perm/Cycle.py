from .Perm import Perm

class Cycle(Perm):
    """
    A class used to create a permutation from a list of integers

    ...

    Attributes
    -------
    aa: list
        a list of integers that represent the nontrivial orbit of the cycle permutation

    """

    def __init__(self, aa):
        """

        :param aa: nontrivial orbit of the cycle
        :type: list
        """
        act = {}
        n = len(aa)
        degree = 0
        for i in range(n):
            degree = max(aa[i] + 1, degree)
            act[aa[i]] = aa[(i + 1) % n]
        for i in range(degree):
            if act.get(i) is None:
                act[i] = i
        super().__init__(act)

    def __call__(self, a):
       return self.act[a]





