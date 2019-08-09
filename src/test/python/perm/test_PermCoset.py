from src.main.perm.SymGroup import SymGroup
from src.main.perm.RandomPerm import RandomPerm as R
from src.main.perm.Cycle import Cycle
from src.main.perm.Grid import Grid
from src.main.perm.PermCoset import Code, PermCoset

def codestabilizer(ii = 10, d = 10):
    for i in range(ii):
        print("=====================")
        grid = Grid((0, 1), (0, 1, 2, 3))
        pi = {(0, 0), (0, 2), (1, 1), (1, 3)}
        code = Code(pi, grid)
        gridgroup = SymGroup(list(range(2))).grid(SymGroup(list(range(4))))
        gridid = Cycle([1]).grid(Cycle([3]))
        gridcoset = PermCoset(gridgroup, gridid)
        print(code)
        gg = code.stabilizer(gridcoset)
        for i in gg.L.gens:
            print("---")
            print((i.gridinv_0(), i.gridinv_1()))

def intersection(ii = 10, a = 5, b = 5):
    for i in range(ii):
        print("=====================")
        c1 = R().permcoset(a)
        c2 = R().permcoset(b)
        print(c1)
        print(c2)
        print(c1.intersection(c2))


if __name__ == "__main__":
    intersection(1, 6, 6)



