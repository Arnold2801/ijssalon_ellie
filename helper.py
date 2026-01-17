def decoreer(tekst=""):
    lengte = len(tekst) + 4   
    print()    
    print(lengte * "*")    
    print(f"* {tekst} *")   
    print(lengte * "*")    
    print()
 
def fooi_pp(bedrag, personen):
    bedrag_pp = bedrag/personen
    return f"Het bedrag per persoon is {bedrag_pp} euro"

def onderstreep(tekst=""):
    uit = []
    uit.append(tekst)
    uit.append(len(tekst) * "=")
    return uit

inkomsten_dict = {
    "aardbeien": 1000,
    "vanille": 2000,
    "chocolade": 1500,
    "waterijsjes": 750
}

totaal_inkomsten = sum(inkomsten_dict.values())

def bereken_totaal(inkomsten_dict):
    totaal = sum(inkomsten_dict.values())
    return totaal





   

