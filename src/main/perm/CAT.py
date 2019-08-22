class CAT:
    """
    An abstract class used for categories

    'Perm', 'PermGroup', and 'PermCoset' subclass from 'CAT'.

    ...

    Abstract Methods
    -------
    prod(other)
        The product of this and another object

    diag
        The diagonal product of this object

    prodinv_0
        The first projection of a product

    prodinv_1
        The second projection of a product

    seq
        Transformation to work with sequence objects

    seqinv
        Pseudoinverse transformation of 'seq'

    gridFromseq(other)
        Transformation to work with grid objects by taking product
        of this sequence object and another sequence object

    gridFromseqdiag
        The diagonal grid product from this sequence object

    gridFromseqinv_phi
        The first projection of the 'gridFromseq' transformation

    gridFromseqinv_psi
        The second projection of the 'gridFromseq' transformation

    griddiag:
        The diagonal grid product from this object

    Implemented Methods
    -------
    grid(other)
        Transformation to work with grid objects with taking a product
        with this object and another object

    gridinv_0
        The first projection of the 'grid' transformation

    gridinv_1
        The second projection of the 'grid' transformation

    """
    def prod(self, other):
        pass

    def diag(self):
        pass

    def prodinv_0(self):
        pass

    def prodinv_1(self):
        pass

    def seq(self):
        pass

    def seqinv(self):
        pass

    def gridFromseq(self, other):
        pass

    def gridFromseqdiag(self):
        pass

    def gridFromseqinv_phi(self):
        pass

    def gridFromseqinv_psi(self):
        pass

    def griddiag(self):
        pass

    def grid(self, other):
        return self.seq().gridFromseq(other.seq())

    def gridinv_0(self):
        return self.gridFromseqinv_phi().seqinv()

    def gridinv_1(self):
        return self.gridFromseqinv_psi().seqinv()




