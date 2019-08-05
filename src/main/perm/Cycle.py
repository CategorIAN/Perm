from perm import Perm

class Cycle(Perm):

    def __init__(self, aa):
        act = {}
        n = len(aa)
        degree = 0
        for i in range(n):
            degree = max(aa[i], degree)
            act[aa[i]] = aa[(i + 1) % n]
        for i in range(degree):
            if act.get(i) is None:
                act[i] = i
        super().__init__(act)

    def __call__(self, a):
       return self.act[a]

    def __mul__(self, other):
        prodact = {}
        mindegree = min(self.degree, other.degree)
        maxdegree = max(self.degree, other.degree)
        for i in range(mindegree):
            prodact[i] = other(self(i))
        for i in range(mindegree, maxdegree):
            prodact[i] = i
        return Perm(prodact)




