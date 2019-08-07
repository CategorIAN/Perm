from math import factorial

class Combinatorics:
    def nCk (self, n, k): #This computes the number of k-subsets from a set of size n.
        f = factorial
        return f(n) // f(k) // f(n-k)

    def nCks(self, n):
        N = 0
        for k in range(n + 1):
            N += self.nCk(n, k)
        return N

    def ksubset(self, n, k, i): #This returns the subset of a given index.
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
        j = i
        k = 0
        while True:
            if j < self.nCk(n, k):
                return self.ksubset(n, k, j)
            j -= self.nCk(n, k)
            k += 1