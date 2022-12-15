def eingabe(message, datentyp):
    a=0
    if(datentyp=="String"):
        a=input(message)
    elif(datentyp=="Int"):
        a=int(input(message))
    elif(datentyp=="Float"):
        a=float(input(message)) 
    return a 

def volumen(b, l, h):
   vol=round(b*l*h,2)
   return vol
   #print(b, l, h)

def raumdiagonale(a, b, c):
    #print("Vorher: a", a, "b", b, "c", c)
    a**=2
    b**=2
    c**=2
    #print("Nachher: a", a, "b", b, "c", c)
    diag=round((a+b+c)**0.5, 2)
    #print(diag)
    return diag

def oberfl(a, b, c):
    o=2*(a*b+a*c+b*c)
    rounded_o=round(o,2)
    return rounded_o

def main():
    breite=eingabe("Breite eingeben: ", "Float")
    laenge=eingabe("Länge eingeben: ", "Float")
    hoehe=eingabe("Höhe eingeben: ", "Float")
    print("Das Volumen beträgt", volumen(breite, laenge, hoehe))
    print("Die Raumdiagonale beträgt", raumdiagonale(breite, laenge, hoehe))
    print("Die Oberfläche beträgt", oberfl(breite, laenge, hoehe))

main()