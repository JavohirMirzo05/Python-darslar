# # VORISLIK VA POLIMORFIZM
# class Shaxs:
#     """Shaxslar haqida ma'lumot"""

#     def __init__(self, ism, familiya, passport, tyil):
#         """Shaxsning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil
        
#     def get_info(self):
#         """Shaxs haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya} "
#         info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
#         return info

#     def get_age(self, yil):
#         """Shaxsning yoshini qaytaruvchi fuksiya"""
#         return yil - self.tyil
    
    
# class Talaba(Shaxs):
#     """Talaba class"""
#     def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
#         """Talabaning xususiyatlari"""
#         super().__init__(ism, familiya, passport, tyil)
#         self.idraqam = idraqam
#         self.bosqich = 1
#         self.manzil=manzil
        
#     def get_id(self):
#         """Talabaning ID raqami"""
#         return self.idraqam
    
#     def get_bosqich(self):
#         """Talabaning o'qish bosqichi"""
#         return self.bosqich
    
    
#     def get_info(self):
#         """Talaba haqida malumot"""
#         info = f"{self.ism.title()} {self.familya.title()}. Manzil:"
#         info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
#         return info
    
# talaba2 = Talaba("javohir", "abdugafurov", "AB3457261", 2006, "ID56782", "yangiyer")    



# class Manzil:

#     def __init__(self, uy, kocha, tuman, viloyat):
        
#         self.uy = uy
#         self.kocha = kocha
#         self.tuman = tuman
#         self.viloyat = viloyat

#     def get_manzil(self):
        
#         manzil = f"{self.viloyat} viloyati, {self.tuman} tumani "
#         manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
#         return manzil

# talaba1_manzil = Manzil(22, "Chamanzor", "Obodyurt", "Sirdaryo")
# talaba1 = Talaba("javohir", "abdugafurov", "FA112299", 2006, "0000012", talaba1_manzil)





# ......................................................................
        
    
# class Manzil:

#     def __init__(self, uy, kocha, tuman, viloyat):
        
#         self.uy = uy
#         self.kocha = kocha
#         self.tuman = tuman
#         self.viloyat = viloyat

#     def get_manzil(self):
        
#         manzil = f"{self.viloyat} viloyati, {self.tuman} tumani "
#         manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
#         return manzil

# talaba1_manzil = Manzil(22, "Chamanzor", "Obodyurt", "Sirdaryo")
# talaba1 = Talaba("javohir", "abdugafurov", "FA112299", 2006, "0000012", talaba1_manzil)

# ..........................................................................................

class Shaxs:
    """Shaxslar haqida ma'lumot"""

    def __init__(self, ism, familiya, passport, tyil):
        """Shaxsning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya} "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info

    def get_age(self, yil):
        """Shaxsning yoshini qaytaruvchi fuksiya"""
        return yil - self.tyil
    
    
class Talaba(Shaxs):
    """Talaba class"""
    def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil=manzil
        
    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam
    
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich
    
    
    def get_info(self):
        """Talaba haqida malumot"""
        info = f"{self.ism.title()} {self.familya.title()}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info
    
talaba2 = Talaba("javohir", "abdugafurov", "AB3457261", 2006, "ID56782", "yangiyer")    



class Manzil:

    def __init__(self, uy, kocha, tuman, viloyat):
        
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat

    def get_manzil(self):
        
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani "
        manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
        return manzil

talaba1_manzil = Manzil(22, "Chamanzor", "Obodyurt", "Sirdaryo")
talaba1 = Talaba("javohir", "abdugafurov", "FA112299", 2006, "0000012", talaba1_manzil)






class Talaba:
    """Shaxslar haqida ma'lumot"""

    def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
        """Shaxsning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        self.idraqam=idraqam
        self.bosqich=1
        self.manzil=manzil
        
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya} "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info

    def get_age(self, yil):
        """Shaxsning yoshini qaytaruvchi fuksiya"""
        return yil - self.tyil

class Fan(Talaba):
    





