# from avto_dars_mod import avto_info, info_print    

# avto1 = avto_info("GM", "Malibu", "Qora", "avtomat", 2000, 4000)
# info_print(avto1)


# from avto_dars_mod import avto_info as ainfo, info_print as iprint

# avto1 = ainfo("GM", "Malibu", "Qora", "avtomat", 2000, 4000)
# iprint(avto1)



# from avto_dars_mod import * 

# avto1 = avto_info("GM", "Malibu", "Qora", "avtomat", 2000, 4000)
# info_print(avto1)



# import math 



# uzunlik = lambda pi, r : 2*pi*r

# print(uzunlik(math.pi, 10))

# kvadrat = lambda x, y: x  y
# print(kvadrat(3, 2))
    
# def daraja(n):
#     return lambda x : x ** n

# kvadrat = daraja(2)
# kub = daraja(3)
# print(kvadrat(10))
# print(kub(10))
# print(f"3-ning kvadrati {kvadrat(3)}, "f"3-ning kubi {kub(3)}  ga teng")



# from math import sqrt

# sonlar=list(range(11))
# ildizlar=list(map(sqrt, sonlar))
# print(ildizlar)

# ildizlar=list(map(sqrt, sonlar))
# print(list(map(lambda x: x * x, sonlar)))



# a=[4,5,6]
# b=[7,8,9]
# a_puls_b = list(map(lambda x, y: x + y, a, b))
# print(a_puls_b)



# ismlar=["hasa", "husan", "olim", "umid"]
# print(list(map(lambda matn:matn.upper(), ismlar))





import random as r
sonlar=r.sample(range(100),(10))
print(sonlar)


juft_sonlar = list(filter(lambda x: x % 2==0, sonlar))
print(juft_sonlar)



# mevalar = ["olma", "anor", "anjir", "shaftoli", "o'rik", "tarvuz", "qovun", "banan"]
# harf = "a"
# mevalar_b = list(filter(lambda meva: meva. startswith(harf), mevalar))
# print(mevalar_b)

# mevalar2 = list(filter(lambda meva: len(meva) <=5, mevalar))
# print(mevalar2)

# print(list(filter(lambda meva: (meva.startswith("a") and meva.andswith("r")), mevalar)))

# import random as r

# sonlar=r.sample(range(100),(10))

# juft = [son for son in sonlar if son%2==0]
