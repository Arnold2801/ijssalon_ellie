from presentatie import toon_inkomsten
import csv 
from helper import bereken_totaal 

inkomsten_dict = {
    "Aardbeien-ijs-totaal" : 1000,
    "Vanille-ijs-totaal" : 2000,
    "Chocolade-ijs-totaal" : 1500,
    "Waterijsjes-totaal" : 750
}

totaal_inkomsten = sum(inkomsten_dict.values())

toon_inkomsten(inkomsten_dict, totaal_inkomsten)


with open('boekhouding.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    for item, bedrag in inkomsten_dict.items():
        writer.writerow([item, bedrag])










