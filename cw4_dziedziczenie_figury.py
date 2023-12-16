class Prostokat():
    def __init__(self, szerokosc, wysokosc):
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc

    def pole_powierzchni(self):
        return self.szerokosc * self.wysokosc


class Kwadrat(Prostokat):
    def __init__(self, bok):
        super().__init__(bok, bok)


class Szescian(Kwadrat):
    def pole_powierzchni(self):
        return super().pole_powierzchni() * 6



moj_szescian = Szescian(2)

print(moj_szescian.pole_powierzchni())