class Grid:
    def __init__(self, phi, psi):
        self.phi = phi
        self.psi = psi

    def points(self, Pi):
        S = set()
        for p in Pi:
            if self.phi.contains(p[0]) and \
            self.psi.contains(p[1]):
                S.add(p)
        return S

    def split(self):
        m1 = len(self.phi) // 2
        if m1 > 0:
            return (Grid(self.phi[:m1], self.psi), Grid(self.phi[m1:], self.psi))
        else:
            m2 = len(self.psi) // 2
            return (Grid(self.phi, self.psi[:m2]), Grid(self.phi, self.psi[m2:]))



