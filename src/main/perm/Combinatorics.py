from math import factorial

class Combinatorics:
    """"
    A class used for functions that enumerate subcollections for collections of integers.

    Methods
    -------
    nCk(n, k)
        The number of subsets of size k from a set of size n

    ksubset(n, k, i)
        The ith subset of size k of the set {0, ... , n - 1}

    subset(n, i)
        The ith subset of the set {0, ... , n - 1}

    ktuple(n, k, i)
        The ith ordered subtuple of size k of the tuple (0, ... , n - 1)

    tuple(n, i)
        The ith ordered subtuple of the tuple (0, ... , n - 1)

    """
    def nCk (self, n, k): #This computes the number of k-subsets from a set of size n.
        """ The number of subsets of size k from a set of size n

        :param n: the size of the set
        :type n: int
        :param k: the size of the subsets
        :type k: int
        :return: number of subsets of size k from a set of size n
        :rtype: int
        """
        f = factorial
        return f(n) // f(k) // f(n-k)


    def ksubset(self, n, k, i): #This returns the subset of a given index.
        """ The ith subset of size k of the set {0, ... , n - 1}

        :param n: the size of the set
        :type n: int
        :param k: the size of the subsets
        :type k: int
        :param i: the order
        :type i: int
        :return: the ith subset of size k of the set {0, ... , n - 1}
        :rtype: set
        """
        s = 0
        S = set()
        p = 0
        while len(S) < k:
            p += self.nCk(n - s - 1, k - len(S) - 1)
            if i < p:
                p -= self.nCk(n - s - 1, k - len(S) - 1)
                S.add(s)
            s += 1
        return S

    def subset(self, n, i):
        """ The ith subset of the set {0, ... , n - 1}

        :param n: the size of the set
        :type n: int
        :param i: the order
        :type i: int
        :return: the ith subset of the set {0, ... , n - 1}
        """
        j = i
        k = 0
        while True:
            if j < self.nCk(n, k):
                return self.ksubset(n, k, j)
            j -= self.nCk(n, k)
            k += 1

    def ktuple(self, n, k, i):
        """ The ith ordered subtuple of size k of the tuple (0, ... , n - 1)

        :param n: the size of the tuple
        :type n: int
        :param k: the size of the ordered subtuples
        :type k: int
        :param i: the order
        :type i: int
        :return: the ith ordered tuple of size k of the tuple (0, ... , n - 1)
        :rtype: tuple
        """
        s = 0
        S = ()
        p = 0
        while len(S) < k:
            p += self.nCk(n - s - 1, k - len(S) - 1)
            if i < p:
                p -= self.nCk(n - s - 1, k - len(S) - 1)
                S = S + (s,)
            s += 1
        return S

    def tuple(self, n, i):
        """ The ith ordered tuple of the tuple (0, ... , n - 1)

        :param n: the size of the ordered tuple
        :type n: int
        :param i: the order
        :type i: int
        :return: the ith ordered tuple of the tuple (0, ... , n - 1)
        """
        j = i
        k = 0
        while True:
            if j < self.nCk(n, k):
                return self.ktuple(n, k, j)
            j -= self.nCk(n, k)
            k += 1