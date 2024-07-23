class Boty:
    def __init__(self, pohlavi, typ, barva, cena, znacka, velikost):
        self.pohlavi = pohlavi
        self.typ = typ
        self.barva = barva
        self.cena = cena
        self.znacka = znacka
        self.velikost = velikost

    def zobraz_info(self):
        return f"Boty: {self.pohlavi}, {self.typ}, Barva: {self.barva}, Cena: {self.cena}, Značka: {self.znacka}, Velikost: {self.velikost}"

    def nastav_cenu(self, nova_cena):
        self.cena = nova_cena

    def nastav_barvu(self, nova_barva):
        self.barva = nova_barva

    def nastav_velikost(self, nova_velikost):
        self.velikost = nova_velikost



class BotyModel:
    def __init__(self):
        self.boty = []

    def pridat_boty(self, boty):
        self.boty.append(boty)

    def smazat_boty(self, index):
        if 0 <= index < len(self.boty):
            del self.boty[index]

    def zobraz_vsechny_boty(self):
        return [boty.zobraz_info() for boty in self.boty]


class BotyView:
    def zobraz_vsechny_boty(self, boty_list):
        for boty in boty_list:
            print(boty)

    def zobraz_zpravu(self, zprava):
        print(zprava)

    def ziskej_podrobnosti_boty(self):
        pohlavi = input("Zadej pohlaví (muž/žena): ")
        typ = input("Zadej typ bot (sneakers, boty, sandály, společenské boty, atd.): ")
        barva = input("Zadej barvu: ")
        cena = float(input("Zadej cenu: "))
        znacka = input("Zadej značku: ")
        velikost = int(input("Zadej velikost: "))
        return Boty(pohlavi, typ, barva, cena, znacka, velikost)

    def ziskej_index_boty(self):
        return int(input("Zadejte index boty, kterou chcete smazat: "))


class BotyController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def pridat_boty(self):
        nove_boty = self.view.ziskej_podrobnosti_boty()
        self.model.pridat_boty(nove_boty)
        self.view.zobraz_zpravu("Boty byly úspěšně přidány.")

    def smazat_boty(self):
        index = self.view.ziskej_index_boty()
        self.model.smazat_boty(index)
        self.view.zobraz_zpravu("Boty byly úspěšně smazány.")

    def zobraz_vsechny_boty(self):
        boty_list = self.model.zobraz_vsechny_boty()
        self.view.zobraz_vsechny_boty(boty_list)


def menu():
    model = BotyModel()
    view = BotyView()
    controller = BotyController(model, view)

    while True:
        print("\nMenu:")
        print("1. Přidat boty")
        print("2. Smazat boty")
        print("3. Zobrazit všechny boty")
        print("4. Konec")

        volba = input("Vyberte akci (1-4): ")

        if volba == '1':
            controller.pridat_boty()
        elif volba == '2':
            controller.smazat_boty()
        elif volba == '3':
            controller.zobraz_vsechny_boty()
        elif volba == '4':
            print("Ukončuji program.")
            break
        else:
            print("Neplatná volba. Zkuste to znovu.")

if __name__ == "__main__":
    menu()