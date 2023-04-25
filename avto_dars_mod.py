



# def avto_info(konpaniya, model, rangi, korabka, yil, narhi=None):
#     """Avtomabil haqidagi malumotlarni"""
#     avto ={
#         "konpaniyasi": konpaniya,
#         "modeli": model,
#         "rangi": rangi,
#         "korobkasi": korabka,
#         "yili": yil,
#         "narh": narhi,
#         }

#     return avto


# def avto_kirit():
#     print("Avtomabillar ro'uhati:")
#     avtolar=[]
#     while True:
#         print("Quyidagilarni kriting\n ", end= "")
#         konpaniya = input("Konpaniya nomini kriting\n>>> ")
#         model = input("Modelini kriting\n>>> ")
#         rangi = input("Rangini kriting\n>>> ")
#         korabka = input("Koropkasini kriting\n>>> ")
#         yil = input("Yilini kriting\n>>> ")
#         narhi = input("Narhini kriting\n>>> ") 
#         avtolar.append(avto_info(konpaniya, model, rangi, korabka, yil, narhi))
#         savol = input("Avtolarni yana qo'shasizmi (ha|yuq)\n ")
#         if savol == "yuq":
#             break
#     return avtolar

# def info_print(avto_info):
#     """Avtomabillar haqida malumotlar saqlangan lug'atni konsilga chiqaruvchi funksiya"""
#     print(
#         f"{avto_info['color'].title()} {avto_info['konpaniyasi'].upper()} "
#         f"{avto_info['modeli'].upper()}, {avto_info['korobkasi']} korobka, "
#         f"{avto_info['yili']}-yil, {avto_info['narh']}$"
#         )





def avto_info(kompaniya, model, rang, korobka, yil, narh=None):
    """Avtomobil ma'lumotlari"""
    avto = {
        "company": kompaniya,
        "model": model,
        "color": rang,
        "box": korobka,
        "year": yil,
        "price": narh
        }
    return avto
def avto_kirit():
    avtolar = []
    while True:
        print("\nQuyidagi ma'lumotlarni kiriting:   ")
        kompaniya = input("Ishlab chiqaruvchini kiriting:  ")
        model = input("Modelini kiriting:  ")
        rang = input("Rangini liriting:  ")
        korobka = input("Korobkasini kiriting:  ")
        yil = input("Yilini kiriting:  ")
        narh = input("Narhi:  ")
        avtolar.append(avto_info(kompaniya, model, rang, korobka, yil, narh))
        j = input("Yana avto qo'shamizmi (ha|yuq):  ")
        if j == 'yuq':
            break
    return avtolar
def info_print(avto_info):
    print(
        'Saytimizga qo\'shgan ma\'lumotlaringiz:  \n'
        f"{avto_info['color'].title()} {avto_info['company'].upper()} "
        f"{avto_info['model'].upper()}, {avto_info['box']} korobka, "
        f"{avto_info['year']} - yil, {avto_info['price']}$")





















