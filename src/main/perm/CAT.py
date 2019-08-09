class CAT:
    def prod(self, other):
        pass

    def prodinv(self):
        pass

    def seq(self):
        pass

    def seqinv(self):
        pass

    def gridFromseq(self, other):
        pass

    def gridFromseqinv_phi(self):
        pass

    def gridFromseqinv_psi(self):
        pass

    def grid(self, other):
        return self.seq().gridFromseq(other.seq())

    def gridinv_0(self):
        return self.gridFromseqinv_phi().seqinv()

    def gridinv_1(self):
        return self.gridFromseqinv_psi().seqinv()




