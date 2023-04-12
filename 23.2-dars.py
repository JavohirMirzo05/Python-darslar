
# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self, ism, familya, tyil):
#         """Talabaning xususiyatlari"""
#         self.ism=ism
#         self.familya=familya
#         self.tyil=tyil
#         self.bosqich=1
        
#     def get_info(self):
#         """Talaba haqida malumotlar"""
#         return f"""{self.ism} {self.familya} {self.tyil} da tug'ulgan. {self.bosqich}-bosqich talabasi"""
    
#     def set_bosqich(self, bosqich):
#         """Talabaning kursini yangilovchi metod"""
#         self.bosqich=bosqich
        
#     def update_bosqich(self):
#         """Talabani bosqichini 1taga oshirish"""
#         self.bosqich += 1
            
# talaba1=Talaba("Alijon", "Valiev", 2000)
# print(talaba1.get_info())
        
# talaba1.update_bosqich() #1ta bosqichga oshiramiz
# print(talaba1.get_info())

# talaba1.update_bosqich() #1ta bosqichga oshiramiz
# print(talaba1.get_info())

# ............................................................................

# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self, ism, familya, tyil):
#         """Talabaning xususiyatlari"""
#         self.ism=ism
#         self.familya=familya
#         self.tyil=tyil
#         self.bosqich=1
        
#     def get_info(self):
#         """Talaba haqida malumotlar"""
#         return f"""{self.ism} {self.familya} {self.tyil} da tug'ulgan. {self.bosqich}-bosqich talabasi"""
    
#     def set_bosqich(self, bosqich):
#         """Talabaning kursini yangilovchi metod"""
#         self.bosqich=bosqich
        
#     def update_bosqich(self):
#         """Talabani bosqichini 1taga oshirish"""
#         self.bosqich += 1

# class Fan():
#     """Talabalar fani"""
#     def __init__(self, nomi):
#         """Oliy matematika"""
#         self.nomi=nomi
#         self.talabalar_soni=0
#         self.talabalar=[]
        
#     def get_student(self):
#         """Nom haqida malumot"""
#         return self.nomi
    
#     def add_student(self, talaba):
#         """Yangi talaba qoshish"""
#         self.talabalar.append(talaba)
#         self.talabalar_soni += 0
    
#     def get_students(self):
      
#         return [x.get_info() for x in self.talabalar]
    
#     def get_students_num(self):
      
#         return self.talabalar_soni
    
    
# matematika=Fan("Oliy matematika")
# talaba1=Talaba("Alijon", "Valiev", 2000)
# talaba2=Talaba("Hasan", "Aliev", 2001)
# talaba3=Talaba("Akbar", "Jumanov", 2003)
        
# talaba1.update_bosqich()
# talaba2.update_bosqich()
# talaba3.update_bosqich()

# matematika.add_student(talaba1)
# matematika.add_student(talaba2)            
# matematika.add_student(talaba3)
                      
# print(matematika.get_students_num())
# # print(matematika.talabalar)

# mat_talabalar=matematika.get_students()
# print(mat_talabalar)

# .............................................

# def see_methods(klass):
#     return [method for method in dir(klass) if method.startswith('__') is False]

# print(see_methods(Talaba))
# print(see_methods(talaba1))

# print(talaba1.__dict__)

# print(talaba1.__dict__.keys())
# print(talaba1.__dict__.values())


# .............................................................................
# uy ishi
class Avto:
    """Avto nomli klas"""
    def __init__(self, model, rang, karobka, narh):
        """Avtolar hususiyatlari"""
        self.model=model
        self.rang=rang
        self.karobka=karobka
        self.narh=narh
        self.kilametr=0
        
    def get_info(self):
        """Avtolar maluumoti"""
        return f"""{self.model} {self.rang} {self.karobka} {self.nath}da. {self.kilametr} yurgan."""
    
    def update_km(self,kilametr):
        """Avtomabil yurgan km """
        self.kilametr=kilametr
        
    def update_km_yurgan(self):
        """Avtomabil yurgan 1km oshirish"""
        self.kilametr +=1
        
class Yavtolar():
    """Yavtolar ro'yhati"""
    def __init__(self, salon_nomi, manzil, sotuvdagi_avtolar):
        
        self.salon_nomi=salon_nomi
        self.manzil=manzil
        self.sotuvdagi_avtolar=sotuvdagi_avtolar
        self.avtolar_soni=0
        self.avtolar=[]
        
    def get_yavto(self):
        """Yangi avtolar nomi haqida malumot"""
        return self.salon_nomi
               
    def add_avto(self,avto):
        """Yangi avto qo'shish"""
        self.avtolar.append(avto)
        self.avtolar_soni +=0

    def get_yavtolar(self):

        return [x.get_info() for x in self.avtolar]

    def get_avto_num(self):
        
        return self.avtolar_noni


avtomabillar=Yavtolar("GM", "yashil", "salafan", 100000)
avto1=Avto("GM", "qora", "qog'oz", 110000)
avto2=Avto("GM", "oq", "tunika", 159000)
avto3=Avto("GM", "jigar", "salafan", 200000)
avto4=Avto("GM", "fo'k", "yog'och", 390000)
        
avto1.update_km_yurgan()
avto2.update_km_yurgan()
avto3.update_km_yurgan()
avto4.update_km_yurgan()

avtomabillar.add_avto(avto1)
avtomabillar.add_avto(avto2)            
avtomabillar.add_avto(avto3)
avtomabillar.add_avto(avto4)
                      
print(avtomabillar.get_avto_num())

sa_avtolar=avtomabillar.get_avto_num()
print(sa_avtolar)




# def see_methods(klass):
#     return [method for method in dir(klass) if method.startswith('__') is False]

# print(see_methods(Talaba))
# print(see_methods(talaba1))

# print(talaba1.__dict__)

# print(talaba1.__dict__.keys())



# print(talaba1.__dict__.values())
      
      
      
      
      
      
      
      
      