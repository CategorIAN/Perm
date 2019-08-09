from .PermGroup import PermGroup
from .Perm import Perm


class SymGroup(PermGroup):
    def __init__(self, n):
        g0act = {}
        for i in range(n):
            g0act[i] = (i + 1) % n
        gens = [Perm(g0act)]

        if n > 1:
            g1act = {0: 1, 1: 0}
            for i in range(2, n):
                g1act[i] = i
            gens.append(Perm(g1act))
        super().__init__(gens)



