



def avto_info(konpaniya, model, rangi, korabka, yil, narhi=None):
    """Avtomabil haqidagi malumotlarni"""
    avto ={
        "konpaniyaa": konpaniya,
        "modell": model,
        "rangg": rangi,
        "korobkaa": korabka,
        "yili": yil,
        "narh": narhi,
        }

    return avto


def avto_kirit():
    print("Avtomabillar ro'uhati:")
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
    return avtolar

def info_print(avto_info):
    """Avtomabillar haqida malumotlar saqlangan lug'atni konsilga chiqaruvchi funksiya"""
    print(
        f"{avto_info['rang'].title()} {avto_info['konpaniya'].upper()} "
        f"{avto_info['model'].upper()}, {avto_info['korobka']} korobka, "
        f"{avto_info['yil']}-yil, {avto_info['narh']}$"
        )

print(avto_kirit())


























