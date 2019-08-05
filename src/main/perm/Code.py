from .PermCoset import PermCoset
from .PermGroup import PermGroup
from .Grid import Grid


class Code:
    def __init__(self, pi, codegrid):
        self.pi = pi
        self.codegrid = codegrid

    def trans(self, coset, grid):
        def union(cc):
            L = None
            z = None
            for c in cc:
                if not c.isEmpty:
                    if L is None:
                        L = c.L
                        z = c.z
                    else:
                        L.add(c.z * z.inv)
            if L is None:
                return PermCoset(PermGroup(set()), cc[0].z.id)
            else:
                return PermCoset(L, z)
        if coset.isEmpty: PermCoset(PermGroup(set()), coset.z.id)
        else:
            I = grid.points(self.pi)
            J = coset.z.act[grid].points(self.pi)
            if len(I) != len(J):
                return PermCoset(PermGroup(set()), coset.z.id)
            elif len(I) == 0:
                return coset
            elif len(I) == 1:
                i = I.pop()
                j = J.pop()
                tt = coset.L.orbitStab(Grid([i[0]], [i[1]]))
                target = coset.z.inv.act[Grid([j[0]], [j[1]])]
                g = tt[0].get(target)
                if g == None:
                    return PermCoset(PermGroup(set()), coset.z.id)
                else:
                    return PermCoset(PermGroup(tt[1]), g * coset.z)
            else:
                grid0, grid1 = grid.split()
                tt = coset.L.orbitStab(grid0)
                cosets = []
                for t in tt[0].values:
                    cosets.append(self.trans(self.trans(PermCoset(PermGroup(tt[1]), t * coset.z), grid0), grid1))
                return union(cosets)

    def stabilizer(self, coset):
        return self.trans(coset, self.codegrid)









