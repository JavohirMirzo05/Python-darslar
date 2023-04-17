# class Avto:
#     __num_avto =0
#     """Avtomabil class"""
   
    
#     def __init__(self, make, model, rang, yil, narh, km=1000):
#         """Avtomabilning xususiyati"""
#         self.make=make
#         self.model=model
#         self.rang=rang
#         self.yil=yil
#         self.narh=narh
#         self.__km=km
#         Avto.__num_avto +=1
        
#     @classmethod
#     def get_num_avto(cls):
#         return cls.__num_avto

#     def get_km(self):
#         return self._km
    
#     def __str__(self):
#         """obyekt haqida malumot"""
#         return f"Avto: {self.make} {self.model} {self.narh}$"
    
#     def __repr__(self):
#         """obyekt haqida malumot"""
#         return f"Avto: {self.make} {self.model} {self.narh}$"
    
#     def __gt__(self,y):
#         return self.narh > y.narh # x > y

#     def __it__(self,y):
#         return self.narh < y.narh # x < y

#     def __le__(self,boshqa_avto):
#         return self.narh <= boshqa_avto.narh # x <= y

#     def __ge__(self,boshqa_avto):
#         return self.narh >= boshqa_avto.narh # x >= y

#     def __eq__(self,boshqa_avto):
#         return self.narh == boshqa_avto.narh # x == y

#     def __ne__(self,boshqa_avto):
#         return self.narh != boshqa_avto.narh # x != y
    
#     def get_info(self):
#         return(
#             f"{self.rang} {self.make} {self.model} {self.yil}-yil. Varh:{self.narh}$"
#             )

    
# avto=Avto("BMW", "x7", "qora", 2020, 40000)
# avto1=Avto("GM", "molibul", "oq", 2020, 50000)
# avto2=Avto("GM", "xkoblt", "ko'k", 2020, 30000)
# avto3=Avto("Toyotto", "tiko", "qora", 2020, 20000)
# avto4=Avto("Mazda", "6", "qora", 2020, 10000)


# class AvtoSalon:
#     """Avtolar classi"""
    
#     def __init__(self, name):
#         self.name=name
#         self.avtolar=[]

#     def __repr__(self):
#         return f"{self.name} avto saloni"
    
#     def __getitem__(self, index): #salon1[2] index ko'rish uchun
#         return self.avtolar[index]
   
#     def __setitem__(self, index, value): #salon1[0] =avto("BMW", "x7", "qora", 2020, 40000)
#         if isinstance(value, Avto):
#             self.avtolar[index] = value
            
#     def add_avto(self, *qiymat): # *args, # **kwargs == *key, *
#         for avto in qiymat:
#             if isinstance(avto, Avto):
#                 self.avtolar.append(avto)
#             else:
#                 return"avto obyektni kriting"
 
# salon1=AvtoSalon("MaxAvto")
# salon2=AvtoSalon("Avto Lider")
# salon3=AvtoSalon("Sam Avto")


# salon1.add_avto(avto1, avto2, avto3)
# salon2.add_avto(avto4)
# salon3.add_avto(avto)


# salon1[2] =Avto("BMW", "x7", "qora", 2020, 40000)
    

# ....................................................................
