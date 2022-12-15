def isSchaltjahr(_jahr):
    if(_jahr % 4 == 0 and _jahr % 100 != 0 or _jahr % 400 == 0):
        return True
    else:
        return False

def main():
    print("Schaltjahr")
    jahr = int(input("Bitte Jahr eingeben: "))

    if(isSchaltjahr(jahr)):
        print("Das Jahr", jahr, "ist ein Schaltjahr")
    else:
        print("Das Jahr", jahr, "ist kein Schaltjahr")

main()