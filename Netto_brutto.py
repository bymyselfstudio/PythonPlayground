def add_mwst(netto):
    brutto=round(netto*1.19, 2)
    return brutto

def main():
    netto=float(input("Geben Sie einen Betrag ein: "))
    brutto=add_mwst(netto)
    print("Der Bruttobetrag von", netto, "€ beträgt", brutto, "€")

main()