# klasa główna = bazowa = rodzic = nadrzędna
class Pojazd:
    def __init__(self, kolor, marka):
        self.kolor = kolor
        self.marka = marka

    def wyswietl_info(self):
        print("To jest POJAZD marki: ", self.marka, "o kolorze: ", self.kolor)


# klasa dziecko, któa dziedziczy z klasy Pojad
class Samochod(Pojazd):
    def __init__(self, kolor, marka, model):
        super().__init__(kolor, marka)
        self.model = model

    def wyswietl_info(self):
        print("To jest SAMOCHOD", self.marka, "model: ", self.model)


moj_pojazd = Pojazd("czerwony", "Toyota")
moj_pojazd.wyswietl_info()


moj_samochod = Samochod("czerwony", "Toyota", "Yaris")
moj_samochod.wyswietl_info()
