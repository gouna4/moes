

# # def mijn_functie_1(tabel, target):
   
# #     for i in range(len(tabel)):
# #         if tabel[i][0] == target:
# #             #print("found index", i, " tabel[]", tabel[i])
# #             return i
    
# #         #print("not found index", i, " tabel[]", tabel[i])
# #     return -1

# # # Example usage:
# # tabel = [
# #     [2,4],
# #     [4, 16],
# #     [10, 100],
# #     [12, 144]
# # ]

# # target_value = 10
# # result = mijn_functie_1(tabel, target_value)

# # if result != (-1):
  
# #     print(f" {tabel[result][1]}") #(Target value {target_value} found at index {result} with value {tabel[result][1]}")
# # else:
# #     print(f"Target value {target_value} not found in the array")

# # def mijn_functie_1(tabel, target):
   
# #     for i in range(len(tabel)):
# #         if tabel[i][0] == target:
# #             #print("found index", i, " tabel[]", tabel[i])
# #             return i
    
# #         #print("not found index", i, " tabel[]", tabel[i])
# #     return -1

# # # Example usage:
# # tabel = [
# #     ["12,3",[15, 9, 36, 4]],
# #     ["12,2",[14, 10, 24, 6]],
# #     ["10,5", [15, 5, 50, 2]],
# #     ["100,20", [120, 80, 2000, 5]]
# # ]

# # target_value = "12,3"
# # result = mijn_functie_1(tabel, target_value)

# # if result != (-1):
  
# #     print(f" {tabel[result][1]}") #(Target value {target_value} found at index {result} with value {tabel[result][1]}")
# # else:
# #     print(f"Target value {target_value} not found in the array")


# def mijn_functie_1(Nummer):
#     Tabel = {2:4 ,
#              4:16,
#             10:100,
#             12:144 }
#     if Nummer in Tabel:
#         return Tabel[Nummer]
#     else:
#         print('Nummer komt niet voor in tabel ')
# print(mijn_functie_1(10))


# def mijn_functie_2(Nummer):
#     Tabel = {((12,3)):[15, 9, 36, 4] ,
#              ((12,2)):[14, 10, 24, 6],
#             ((10,5)):[15, 5, 50, 2],
#             ((100,20)):[120, 80, 2000, 5] }
#     if Nummer in Tabel:
#         return Tabel[Nummer]
#     else:
#         print('Nummer komt niet voor in tabel ')



# def aanbieding_1(smaak, prijs ,korting):
#     prijs_korting = prijs*korting
#     te_betalen = prijs - prijs_korting
#     return f'Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak} van {prijs} euro voor {te_betalen} euro.'


# inkomsten_per_dag = [220,430,125,160,205,90,345]

# def inkomsten_totaal(inkomsten):
#     return sum (  inkomsten)


# Btw_te_betalen = 0.9
# def btw_inkomsten_totaal(inkomsten, btw):
#     return (sum(inkomsten) * (btw))







# def start():
#     print(mijn_functie_2((10,5)))
#     print(mijn_functie_1(10))
#     print(aanbieding_1('aardbei',4,0.1))
#     print("de inkomsten van de week: ",inkomsten_totaal(inkomsten_per_dag))
#     print("de btw over inkomsten van de week: ", btw_inkomsten_totaal(inkomsten_per_dag, Btw_te_betalen))







# if __name__ == "__main__":
#     start()

# reclame.py

def hoog_en_laag(mijn_lijst):
    """
    Geeft een lijst terug met de hoogste en laagste waarde van de inputlijst.
    """
    return [max(mijn_lijst), min(mijn_lijst)]

def laag_en_hoog(mijn_lijst):
    """
    Geeft een lijst terug met de laagste en hoogste waarde van de inputlijst.
    Gebruikt hiervoor de functie hoog_en_laag().
    """
    return hoog_en_laag(mijn_lijst)

def gemiddelde(mijn_lijst):
    """
    Geeft het gemiddelde van de inputlijst terug als een string.
    """
    gemiddelde_bedrag = sum(mijn_lijst) / len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde_bedrag:.2f} euro."

def meervoudig(invoer_lijst):
    """
    Geeft een lijst terug van de hoogste en laagste waarde van de inputlijst.
    Gebruikt hiervoor de functie hoog_en_laag().
    """
    return hoog_en_laag(invoer_lijst)

# Voorbeeldgebruik:
inkomsten_per_dag = [220, 430, 125, 160, 205, 90, 345]
andere_inkomsten = [10, 5, 3, 2, 1, 2, 9]

resultaat_laag_hoog = laag_en_hoog(inkomsten_per_dag)
print("Laagste en hoogste inkomsten:", resultaat_laag_hoog)

resultaat_gemiddelde = gemiddelde(inkomsten_per_dag)
print(resultaat_gemiddelde)

resultaat_meervoudig = meervoudig(andere_inkomsten)
print("Laagste en hoogste waarden:", resultaat_meervoudig)



tessssssssssssssssssssssssssssss
print("Van deze regel krijg ik later spijt")