def bekeres():
    print("i/A:")
    autonev = input("\Autó neve: ")
    gyartas = int(input("\Gyártási dátum: "))
    print("i/B:")
    if gyartas == 2026:
        print(f"\tEz az {autonev} friss gyártás")
    elif gyartas < 2000:
        print(f"\tEz az {autonev} öreg autó")
    else:
        print(f"\tEz az {autonev} átlagos korú")
