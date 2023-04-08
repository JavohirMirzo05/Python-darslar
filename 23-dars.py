# class Talaba:
#     """Talaba nomli klas yaratamiz"""
    
#     def __init__(self, ism, familya, tyil, tel):
#         """Talabaning hususuyatlari"""
#         self.ism=ism
#         self.familya=familya
#         self.tyil=tyil
#         self.tel=tel
        
#     def get_f_name(self):
#         return f"To'liq ism familyasi: {self.ism} {self.familya}"
    
#    def get_tel(self):
#      return self.tel
    
#     def tanishtir(self):
#         print(f"""Ismim {self.ism} {self.familya} {self.tyil} yilda tug'ulganman, {self.tel}""")


#     def get_name(self):
#         """Talabaning ismini qaytaradi"""
#         return self.ism
    
#     def get_lastname(self):
#         """Talabaning ismini qaytaradi"""
#         return self.familya
    
#     def get_fullname(self):
#         """Talabaning ism-familyasi qaytaradi"""
#         return f"{self.ism} {self. familya}"

#     def get_age(self, yil):
#         """Talabaning yoshini qaytaradi"""
#         return yil-self.tyil
    
#     def tanishtir(self):
#         print(f"""Ismim {self.ism} {self.familya} {self.tyil} yilda tug'ulganman""")


# talaba1=Talaba("Alijon", "Valiyev", 2000, 99893208399)
# talaba2=Talaba("Hasan", "Umarov", 1995, 9983737593)

# print(talaba1.ism)
# print(talaba1.familya)
# # talaba2.tanishtir()

# # talaba2.get_age(2022)

# ................................

# class Avtolar:

#     def __init__(self, madeli, nomi, rangi, yili):
#         """Avtolar hususuyatlari"""
#         self.madeli=madeli
#         self.nomi=nomi
#         self.rangi=rangi
#         self.yili=yili

#     def get_tel(self):
#         return self.modeli

#     def get_name(self):
#         return self.nomi
    
#     def get_name(self):
#         return self.rangi
    
#     def get_name(self):
#         return self.yili
    
#     def tanishtir(self):
#         print(f"""Avtolar malumoti {self.madeli} {self.nomi} {self.rangi} {self.yili} da ishlab chiqarilgan""")
    
# avto1=Avtolar("GM", "neksiya1","ko'k", 2015)
# avto2=Avtolar("GM", "Koblt", "oq", 2020)

# print(avto1.madeli)
# print(avto1.nomi)
# # avto2.malumot ber

# .................................

# uy ishi

class Malumotlar:
    """Foydalanuvchi malumotlari"""
    
    def __init__(self, ism, familya, emailpochta, tel, parol, yil, yosh):
        """Foydalanuvchining hususiyatlari"""
        self.ism=ism
        self.familya=familya
        self.emailpochta=emailpochta
        self.tel=tel
        self.parol=parol
        self.yil=yil
        self.yosh=yosh
        
    def get_f_name(self):
        """Foydalanuvchining ism va familyasi haqida malumot"""
        return f"Toliq ism va familya:\n>>> {self.ism.title()} {self.familya.title()}"
    
    def get_email(self):
        """Foydalanuvchinig emailpochtasi"""
        return self.emailpochta
    
    def get_tel(self):
        """Foydalanuvchinig telefon raqami"""
        return self.tel
    
    def get_parol(self):
        """Foydalanuvchinig paroli"""
        return self.parol
    
    def get_yil(self):
        """Foydalanuvchinig tug'ilgan yili"""
        return self.yil
    
    def get_yosh(self,yil):
        """Foydalanuvchinig yoshi"""
        return yil-self.yosh
    
    def malumot(self):
        """Foydalanuvchinig barcha malmoti"""
        return f"Ism\n>>> {self.ism.title()}\n>>> Familya\n>>> {self.familya.title()}\n>>> Email pochta\n>>> {self.emailpochta}\n>>> Telefon raqami\n>>> {self.tel}\n>>> Email proli\n>>> {self.parol}\n>>> Tug'ilgan yili\n>>> {self.yil}\n>>> Hoirgi yoshi\n>>> {self.yosh}"


talaba1=Malumotlar("ali", "aliev", "abdujavoohir05@gmal.com", 971735555, 574084357, 2006, 16)
talaba2=Malumotlar("vali", "umarov", "dilshodkaxxarov05@gmail.com", 998885999, 359966556, 2005, 17)

print(talaba1. ism)
print(talaba1. familya)







