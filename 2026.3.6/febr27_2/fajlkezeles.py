def fajlba_ir():
    f = open("proba.txt", "w", encoding="utf8")
    f.write("\n10. osztály")
    f.close()

def fajlba_olvas():
    f = open("proba.txt", "r", encoding="utf8")
    print(f.read())
    f.seek(0)
    print(f.read(3))
    f.seek(0)
    lista = f.readlines()
    print(lista[1])