from perm import PermGroup

class BSGS:

    def __init__(self, base, groups, reprs):
        self.base = base
        self.groups = groups
        self.reprs = reprs

    def __str__(self):
        print("Base: {}, Groups: {}, Reprs: {}".format(self.base, self.groups, self.reprs))

    def contains(self, g):
        return PermGroup.strip(self.base, self.reprs, 0, g)



