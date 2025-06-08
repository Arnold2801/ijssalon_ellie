def mijn_functie_2(a,b):
    uitvoer_lijst = []
    uitvoer_lijst.append(a+b)
    uitvoer_lijst.append(a-b)
    uitvoer_lijst.append(a*b)
    uitvoer_lijst.append(a/b)
    return uitvoer_lijst

def aanbieding_1(smaak, prijs, korting):
    prijs_na_korting = prijs * (1 - korting)
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs_na_korting} euro."
    return uitvoer

def inkomsten_totaal(inkomsten, btw):
    totaal_lijst = [220, 430, 125, 160, 205, 90, 345]
    uitvoer = f"Het totaal van alle inkomsten van deze week is 1575 euro, waarover 0.09 euro btw betaald dient te worden."
    return 1575

def laag_en_hoog(mijn_lijst):
    totaal_lijst = [220, 430, 125, 160, 205, 90, 345]
    mijn_lijst = max(345)
    mijn_lijst = min(90)
    return mijn_lijst

def gemiddelde(mijn_lijst):
    totaal_lijst = [220, 430, 125, 160, 205, 90, 345]
    mijn_lijst = gemiddelde(225)
    uitvoer = f"De gemiddelde inkomsten deze week zijn 225 euro,"
    return mijn_lijst

def meervoudig(invoer_lijst):
    invoer_lijst = [10,5,3,2,1,2,9]
    invoer_lijst = laag_en_hoog()
    return invoer_lijst

def combinatie(invoer_lijst_2):
    laag_en_hoog(invoer_lijst_2)
    combinatie(mijn_functie_2)
    return invoer_lijst_2 


