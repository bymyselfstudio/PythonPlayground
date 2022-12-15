"""Schreiben Sie eine Funktion namens zero2, der Sie eine Zahl größer 100 oder
kleiner -100 übergeben und die dann die beiden rechten Ziffern der Zahl auf
Null setzt und wieder zurückgibt. Aus 134 wird 100, aus -1635 wird -1600 usw.

Schreiben Sie auch hier wieder eine main-Methode, mit der Sie das Ergebnis
überprüfen können."""

def zero2(x):
    tmp=x
    if(x>100):
        tmp=x%100    
    elif(x<100):
        tmp=x%-100
    return x-tmp


def main():
    print("Zahl formatieren")
    zahl = int(input("Geben Sie eine Zahl groesser 100 oder kleiner -100 ein: "))
    print(zero2(zahl))

main()
    