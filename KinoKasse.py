from datetime import date

def eingabe(message, datatyp):
    a=0
    if(datatyp=="String"):
        a=input(message)
    elif(datatyp=="Int"):
        a=int(input(message))
    elif(datatyp=="Float"):
        a=float(input(message))
    return a


def filmpreisNachAnzahl(film, anzahl):
    preis=0
    normalPreis=15*anzahl
    if(film=="V" or film=="v" or film=="C" or film=="c"):
        preis = normalPreis
    elif(film=="A" or film=="a"):
        preis = normalPreis*1.3
    return preis


def welcherTag(preis, tag):
    #print("tag", tag)
    if(tag == 2): # Wenn Mittwoch, dann Kinotag
        #print("kommt an")
        return preis*0.5
    else:
        return preis


def loge(sitzArt, preis):
    if(sitzArt == "L" or sitzArt=="l"):
        #print("berechneter logenpreis", preis)
        return preis*1.2
    elif(sitzArt == "N" or sitzArt=="n"):
        return preis


def bezahlen(preis, film):
    print("Bitte zahlen Sie", preis,"€")
    bezahlt=eingabe("Zahlen Sie das Geld bitte jetzt ein: ", "Float")
    
    if(bezahlt==preis):
        print("Hier Ihr Ticket.")
    elif(bezahlt>preis):
        rueckGeld=bezahlt-preis
        print("Hier ist Ihr Ticket und Ihr Rückgeld von", rueckGeld, "€")
    else:
        differenz=preis-bezahlt
        #rekursive Funktion
        bezahlen(differenz, film)


def main():
    print("Kino Kasse")
    #normaler Preis für eine Kino Karte ist 15€
    #Wir unterscheiden Filme in 3D und Normal, 3D Filme sind 30% teurer
    # Filme sind: Avatar(3D), Violent (Normaler Film) und Call Jane (Normaler Film)
    film=eingabe("Welchen Film wollen sie sehen? [A]vatar3D, [V]iolent oder [C]allJane ", "String")
    anzPersonen=eingabe("Wieviele Personen möchten Sie auswählen? ", "Int")
    
    #Sitzart kann Loge oder Normal sein Loge ist 20% teurer
    sitzArt=eingabe("[L]oge oder [N]ormal? ", "String")

    #Montag ist Kino Tag und alle Filme Kosten nur die hälfte
    tag=date.today().weekday()

    #print("tag", tag)
    preis=filmpreisNachAnzahl(film, anzPersonen)
    preis=loge(sitzArt, preis)
    preis=welcherTag(preis, tag)
    preis=bezahlen(preis, film)

    # 1) Preis berechnen 2) bezahlen 

main()