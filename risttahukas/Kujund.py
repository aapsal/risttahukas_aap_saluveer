class Kujund:
    def __init__(self, pikkus, laius, korgus):
        self.pikkus = pikkus
        self.laius = laius
        self.korgus = korgus

    def arvuta_taispindala(self):
        return 2 * (self.pikkus * self.laius + self.pikkus * self.korgus + self.laius * self.korgus)

    def arvuta_ruumala(self):
        return self.pikkus * self.laius * self.korgus

    def arvuta_diagonaal(self):
        return (self.pikkus ** 2 + self.laius ** 2 + self.korgus ** 2) ** 0.5