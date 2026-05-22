import osztaly


def beolvasas():
    diakok = []
    f = open("tizedikesek.txt", "r", encoding="utf8")
    # első sor eldobása
    f.readline()
    # maradék sorok listába
    sorok = f.readlines()
    f.close()
    return sorok

def obj_lista(sorok: list[str]) -> list[osztaly.Diak]:
    diakok = []
    for i in range(len(sorok)):
        darabok = sorok[i].split("/")
        diak = osztaly.Diak(
            nev=darabok[0],
            eletkor=darabok[1],
            atlag=darabok[2])
        diakok.append(diak)
    return diakok

def atlag(diakok: list[osztaly.Diak]) -> float:
    osszeg = 0
    meret = len(diakok)
    for i in range(meret):
        osszeg += diakok[i].atlag
    return round(osszeg/meret, 2)

def megszamlalas(diakok: list[osztaly.Diak]) -> int:
    db = 0
    for i in range(len(diakok)):
        if 18 > diakok[i].eletkor:
            db += 1
    return db
    


def teljes():
    sorok = beolvasas()
    print(sorok)
    diakok = obj_lista(sorok)
    #print(diakok[2].nev)
    print(f"A diákok átlagának az átlaga: {atlag(diakok)}.")
    print(f"A 18 alati diákok darabja: {megszamlalas(diakok)}.")
