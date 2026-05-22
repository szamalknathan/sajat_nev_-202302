class Diak:
    def __init__(self, nev:str, eletkor:str, atlag: str):
        self.nev = nev
        self.eletkor = int(eletkor)
        self.atlag = float(atlag.replace(",", "."))


def __str__(self):
    return (f"Név: {self.nev}\n"
            f"Életkor: {self.eletkor}\n"
            f"Átlag: {self.atlag}\n")