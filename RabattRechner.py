def rabatt(betr, proz):
   #print(betr, proz)
   rabattBetrag=betr*proz/100
   #print(rabattBetrag)
   return rabattBetrag

def main():
    betrag=float(input("Bitte geben Sie den Betrag ein: "))
    rabattProzent=float(input("Bitte geben Sie den Rabatt ein: "))
    ergebnis=rabatt(rabattProzent,betrag)
    print("Ursprünglicher Betrag:", betrag, "€,")
    print("Rabatt:", ergebnis, "€,")
    print("Endbetrag:", betrag-ergebnis, "€.")
    
main()