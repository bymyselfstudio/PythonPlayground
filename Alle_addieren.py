"""Schreiben Sie eine Funktion namens sum, der man einen positiven
ganzzahligen Wert übergibt und die dann die Summe aller Zahlen von 
1 bis einschließlich des Wertes zurückliefert.
Übergibt man zum Beispiel die Zahl 5, wird der Wert 15 zurückgeliefert,
weil 1-2-3-4-5=15 ist. Die Funktion soll dabei Variablen vom Typ int
verwenden.
Schreiben Sie dazu eine main-Funktion, mit der Sie die sum-Funktion
überprüfen können."""


def sum(n):
    if n == 1:
        return 1
    else:
        return sum(n-1) + n

def main():
    num = int(input("Geben Sie eine ganze positive Zahl ein: "))
    print("Die Summe aller Zahlen von 1 bis", num, "=", sum(num))

main()

