import random

def szamok():
    list = []
    for i in range(5):
        list.append(random.randint(1, 15))
    
    return list

def kiiras_1(lista):
    print("ii/A, B, C")
    print("\t", end="")

    for i in range(len(lista)-1):
            print(list[i], end=",")
    print(lista[-1])

def egyjegyuek_szama(lista):
     db = 0
     for i in range(len(lista)):
          if len(str(lista[i])) == 1:
               db += 1
    #return db


def konzol_kiir(db):
     print("ii\F:")
     print(f"\tAz egyjegyűek száma {db}")

def file_kiir(db):
     f = open("szamok.txt", "w", encoding="UTF8")
     f.write(f"ii/F:\n\tAz egyjegyűek száma: {db}.")
     f.close()

def teljes():
    lista = szamok()
    print(lista)
    kiiras_1()
    
    db = egyjegyuek_szama(lista)
    konzol_kiir(db)

    file_kiir(db)