def beolvasas():
    f = open("auto.txt", "r", encoding="UTF8")
    f.readline()
    sorok = f.readlines

    f.close()

    return sorok

def obj_beolvasa(sorok):
    lista = []
    for i in range(sorok):
        sor = sorok[i].split("$")
        objektum = osztaly.Auto(darabok[0], darabok[1])
        lista.append(objektum)
    return lista

def atlag_kor(lista):
    osszeg = 0
    for i in range (len(lista)):
        osszeg += lista[i].kor

    return 2026 -(osszeg / len(lista))

def teljes():
    sorok = beolvasas()
    lista = obj_beolvasa(sorok)
    
    print(atlag_kor(lista))

