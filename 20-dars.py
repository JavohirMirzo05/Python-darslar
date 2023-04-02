talabalar=["ali", "vali", "hasan", "xusan"]

def bahola(ismlar):
    
    baholar={}
    while ismlar:
        ism = ismlar.pop()
        baho=input(f"Talaba {ism.title()}ni baholang\n>>> ")
        
        baholar[ism]=baho
    return baholar

baholar = bahola(talabalar[:])
print(baholar)
print(talabalar)


for baho in baholar.velues:
    print(f"{talabalar.pop().title()}ning baholari {baho}")

# .............................................................................


# def summa(*sonlar):
#     """kritilgan sonni yig'indisini hisoblovchi funksiya"""
#     yigindi=0
#     for son in sonlar:
#         yigindi +=son
#     return yigindi

# print(summa(1,2,3,4,5,6,7,8,9,10))


# def summa(*sonlar):
#     """kritilgan sonni yig'indisini hisoblovchi funksiya"""
#     return sum(sonlar)

# print(summa(1,2,3,4,5))
# print(summa(1,2,3,9,10))



# def summa(x, y,*sonlar):
#     """kritilgan sonni yig'indisini hisoblovchi funksiya"""
#     return x + y + sum(sonlar)

# print(summa(2,2))
# print(summa(1,2,3,4,5))
# print(summa(9,11))



# def avto_info(konpaniya, model, **malumotlar):
#     """Avto haqida malumotlar lug'at ko'rinishida qaytaradi lug'at"""
#     malumotlar["konpaniya"]=konpaniya
#     malumotlar["model"]=model
#     return malumotlar
    
# avto1=avto_info("GM", "malibul", rang="qorq", yil=2020)
# avto2=avto_info("Kia", "K5", rang="qizil",narh=54218, yil=2020, korobka="ko'k")





# Uy ishi


# import math

# def fibonacci(kopaytmalar):
#     """Harbir son bir biriga ko'paytiriluvchi funksiya"""
#     sonlar=[]
#     int(input())
#     for i in range (kopaytmalar):
#         if i==0 or i==1:
#             sonlar.append()
#         else:
#             sonlar.append(sonlar[i-1]+sonlar[i-2])
#         return sonlar

# print(math.factorial(10))



# def fibonacci(n):
    
#     sonlar=[]
#     for i in range (n):
#         if i==0 or i==1:
#             sonlar.append(1)
#             # print(sonlar)
#         else:
#             # print(sonlar[1], sonlar[2])
#             sonlar.append(sonlar[i-1]+sonlar[i-2])
#     return sonlar

# print(fibonacci(10))



