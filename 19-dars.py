# def oraliq(min, max, qadam=1 ):
#     sonlar=[]
#     while min<max:
#         sonlar.append(min)
#         min += qadam
#     return sonlar

# print(oraliq(1,21,4))

# .................................................................................



# def avto_info(konpaniya, model, rangi, korabka, yil, narhi=None):
#     avto ={
#         "konpaniyaa": konpaniya,
#         "modell": model,
#         "rangg": rangi,
#         "korobkaa": korabka,
#         "yili": yil,
#         "narh": narhi,
#         }

#     return avto

# print("\n Saytimizdagi avtomabillar ro'yhati:")
# avtolar=[]
# while True:
#     print("\nQuyidagilarni kriting\n ", end= "")
#     konpaniya = input("Konpaniya nomini kriting\n>>> ")
#     model = input("Modelini kriting\n>>> ")
#     rangi = input("Rangini kriting\n>>> ")
#     korabka = input("Koropkasini kriting\n>>> ")
#     yil = input("Yilini kriting\n>>> ")
#     narhi = input("Narhini kriting kriting\n>>> ") 
#     avtolar.append(avto_info(konpaniya, model, rangi, korabka, yil, narhi))
#     savol = input("Avtolarni yana qo'shasizmi (yes/no)\n ")
#     if savol == "no":
#         break 
#     print("\n Onlayin bozordagi onlayn avtomabillar")
# for avto in avtolar:
#     if avto["narh"]:
#         narh = f'{avto["narh"]}$'
#     else:
#         narh="Nomalum"
# print(f"{avto['konpaniyaa']} {avto['modell']} {avto['rangg']} {avto['korobkaa']} {avto['yili']}. Narhi:{narh} ")

# .............................................................................

# def talabani_baholang(isimlar):
#     baholar={}
#     while isimlar:
#         ism = isimlar.pop()
#         baho = input(f"Talaba {ism.title()}ning bahosini kriting:\n>>> ")
#         baholar[ism] = int(baho)
#     return baho

# baho = talabani_baholang(["ali", "vali", "olim", "xusan"])
# print(baho)























