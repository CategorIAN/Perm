from perm import CAT, Code, Grid

class PermCoset(CAT):
    def __init__(self, L, z):
        self.L = L
        self.z = z
        self.degree = max(L.degree, z.degree)

    def intersection(self, other):
        pi = set()
        phi = []
        psi = []
        degree = min(self.degree, other.degree)

        for i in range(degree):
            pi.add((i, i))
        for i in range(self.degree):
            phi.append(i)
        for i in range(other.degree):
            psi.append(i)

        coset = self.grid(other)
        return Code(pi, Grid(phi, psi)).stabilizer(coset)


    def sum(self, other):
        return PermCoset(self.L.sum(other.L), self.z.sum(other))

    def prod(self, other):
        return PermCoset(self.L.prod(other.L), self.z.prod(other))

    def prodinv(self):
        return PermCoset(self.L.prodinv, self.z.prodinv)

    def seq(self):
        return PermCoset(self.L.seq, self.z.seq)

    def seqinv(self):
        return PermCoset(self.L.seqinv, self.z.seqinv)

    def gridFromseq(self, other):
        return PermCoset(self.L.gridFromseq(other.L), self.z.gridFromseq(other.z))

    def gridFromseqinv(self):
        return PermCoset(self.L.gridFromseqinv, self.z.gridFromseqinv)

    def isEmpty(self):
        return len(self.L.gens) == 0










