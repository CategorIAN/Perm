class CAT:
    def sum(self, other):
        pass

    def sumdiag(self):
        return self.sum(self)

    def prod(self, other):
        pass

    def prodinv(self):
        pass

    def proddiag(self):
        return self.prod(self)

    def seq(self):
        pass

    def seqinv(self):
        pass

    def gridFromseq(self, other):
        pass

    def gridFromseqinv(self):
        pass

    def grid(self, other):
        return self.seq.gridFromseq(other.seq)

    def gridinv(self):
        return self.gridFromseqinv.seqinv

    def griddiag(self):
        return self.grid(self)




