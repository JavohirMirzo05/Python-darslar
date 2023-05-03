# import math
# print("Aqil charhlovchi matematik misollar.")
# print("h")





def avto_info(konpaniya, model, rangi, korabka, yil, narhi=None):
    avto ={
        "konpaniyaa": konpaniya,
        "modell": model,
        "rangg": rangi,
        "korobkaa": korabka,
        "yili": yil,
        "narh": narhi,
        }

    return avto

print("\n Saytimizdagi avtomabillar ro'yhati:")
avtolar=[]
while True:
    print("Quyidagilarni kriting\n ", end= "")
    konpaniya = input("Konpaniya nomini kriting\n>>> ")
    model = input("Modelini kriting\n>>> ")
    rangi = input("Rangini kriting\n>>> ")
    korabka = input("Koropkasini kriting\n>>> ")
    yil = input("Yilini kriting\n>>> ")
    narhi = input("Narhini kriting kriting\n>>> ") 
    avtolar.append(avto_info(konpaniya, model, rangi, korabka, yil, narhi))
    savol = input("Avtolarni yana qo'shasizmi (yes/no)\n ")
    if savol == "no":
        break 
    print("\n Onlayin bozordagi onlayn avtomabillar")
for avto in avtolar:
    if avto["narh"]:
        narh = f'{avto["narh"]}$'
    else:
        narh="Nomalum"
print(f"{avto['konpaniyaa']} {avto['modell']} {avto['rangg']} {avto['korobkaa']} {avto['yili']}. Narhi:{narh} ")































