from .Perm import Perm

class Cycle(Perm):

    def __init__(self, aa):
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





