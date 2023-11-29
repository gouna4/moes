def aanbieding_1(smaak, prijs ,korting):
    prijs_korting = prijs*korting
    te_betalen = prijs - prijs_korting
    return f'Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak} van {prijs} euro voor {te_betalen} euro.'

print(aanbieding_1('aardbei',4,0.1))


def inkomsten_totaal(inkomsten,btw):
    
     
        return f"Het totaal van alle inkomsten van deze week is {Week} euro, waarover {Btw_betalen } euro btw betaald dient te worden"

inkomsten_per_dag = [220,430,125,160,205,90,345]
btw= 0.09
Week= sum (inkomsten_per_dag)
Btw_betalen= btw * sum(inkomsten_per_dag)
print(inkomsten_totaal(inkomsten_per_dag,Btw_betalen))

def laag_en_hoog(mijn_lijst):

    return max(lijst) ,min (lijst)
lijst = [220,430,125,160,205,90,345]   

print(laag_en_hoog(lijst))


def gemiddelde(mijn_lijst):
    gemiddelde_waarde_lijst = sum(inkomsten_per_dag) / len(inkomsten_per_dag)
    
    return gemiddelde_waarde_lijst

inkomsten_per_dag = [220, 430, 125, 160, 205, 90, 345]

mijn_lijst = gemiddelde(inkomsten_per_dag)

print("De gemiddelde inkomste deze week zijn",gemiddelde(mijn_lijst),"euro")

def meervoudig(invoer_lijst):
 
    return max(lijst) ,min (lijst)
lijst = [10,5,3,2,1,2,9] 

print(laag_en_hoog(lijst))
     


