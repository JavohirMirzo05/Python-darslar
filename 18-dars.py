def talaba_haqida_malumot(ism, familya):
    """Talabalar haqida yo'qlama malumotlari"""
    talaba_haqida = f"{ism}, {familya}"
    return talaba_haqida

talaba1 = talaba_haqida_malumot("ali", "valiev")
talaba2 = talaba_haqida_malumot("olim", "olimov")
print(f"Darsga kelmagan talabalar: {talaba1.title()} va {talaba2.title()}")
print(f"Darsga {talaba2.title()} kechikib keldi")


# .............................................................................

# def toliq_ism(ism, familya, otasining_ism=""):
#     """To'liq ism qaytaruvchi malumot"""
#     if otasining_ism:
#         toliq_ism_haqida= f"{ism}, {familya}, {otasining_ism} "
#     else:
#         toliq_ism_haqida=f"{ism}, {familya} "
#     return toliq_ism_haqida

# talaba1 = toliq_ism("ali", "valiev")
# talaba2 = toliq_ism("oli", "valiev", "dilshod")
# print(f"malumot: {talaba1.title()} va {talaba2.title()}")

# .............................................................................

# def aftomabillar(kanpaniyasi, rangi, nomi, yili, narhi=None):
    
#     avto={
#         "a": kanpaniyasi,
#         "b": rangi,
#         "d": nomi,
#         "e":yili,
#         "price":narhi
#         }
#     return avto

# avto1=aftomabillar("GM", "oq", "koblt", 2020)
# avto2=aftomabillar("GM", "oq", "koblt", 2020)
# avtolar=[avto1, avto2]

# print("Onlayin bozordagi onlayn avtomabillar")
# for avto in avtolar:
#     if avto["price"]:
#         narh = f'{avto["price"]}$'
#     else:
#         narh="Nomalum"
# print(f"{avto['b']} {avto['d']} {avto['d']} {avto['e']}. Narhi:{narh} ")

# ...................................................


# def oraliq(min, max):
#     sonlar=[]
#     while min < max:
#         sonlar.append(min)
#         min +=1
#     return sonlar

# print(oraliq(0, 10))
# print(oraliq(10, 21))

# ..........................................................................



