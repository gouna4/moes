# def Mijn_lijst_1(Lijst):
#     Nummer= {2:4,
#           4:16,
#           10:100,
#           12:144 }
    
#     if Lijst in Nummer:
#         return Nummer [Lijst]
#     else:
#         print('waarde komt niet voor in lijst')
# print (Mijn_lijst_1(10))



# def Mijn_lijst_2 (Lijst_1):
#     Nummer_2 = {((12,3)):[15,9,36,4],
#               ((12,2)):[14,10,24,6],
#               ((10,5)):[15,5,50,2],
#               ((100,20)):[120,80,2000,5]}
#     if Lijst_1 in Nummer_2:
#         return Nummer_2 [Lijst_1]
#     else:
#         print('Komt niet voor in lijst_1')
# Mijn_lijst_2 ((12,3))
# print (Mijn_lijst_2 ((12,3)))


# reclame.py

def aanbieding_1(smaak, prijs, korting):
    """
    Genereert een tekst voor een specifieke aanbieding.

    Parameters:
    - smaak: De smaak van het product.
    - prijs: De oorspronkelijke prijs van het product.
    - korting: De toegepaste korting op het product.

    Returns:
    Een tekstuele beschrijving van de aanbieding.
    """
    nieuwe_prijs = prijs - (prijs * korting)
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs} euro."

# Voorbeeldgebruik
aanbieding_1_text = aanbieding_1("aardbei", 4, 0.1)
print(aanbieding_1_text)
