class Avto: 
    __num_avto = 0 
    """Avtomobil klassi""" 
 
 
    def __init__(self, make, model, rang, yil, narh, km=1000): 
        """Avtomobillarning xususiyati""" 
        self.make = make 
        self.model = model 
        self.rang = rang 
        self.yil = yil 
        self.narh = narh 
        self.__km = km 
        Avto.__num_avto += 1 
         
    @classmethod 
    def get_num_avto(cls): 
        return cls.__num_avto 
     
    def get_km(self): 
        return self.__km 
     
    def __str__(self): 
        """Obyekt haqida ma`lumot""" 
        return f"Avto: {self.make} {self.model} {self.narh}$" 
     
    def __repr__(self): 
        """Obyekt haqida ma`lumot""" 
        return f"Avto: {self.make} {self.model} {self.narh}$" 
     
    def __gt__(self, y):  # x > y 
        return self.narh > y.narh 
     
    def __lt__(self, y): # x < y 
        return self.narh < y.narh 
 
    def __le__(self, boshqa_avto): # x <= y 
      return self.narh <= boshqa_avto.narh 
 
    def __ge__(self, boshqa_avto): # x >= y 
      return self.narh >= boshqa_avto.narh 
 
    def __eq__(self, boshqa_avto): # x == y 
          return self.narh == boshqa_avto.narh 
 
    def __ne__(self, boshqa_avto):  # x != y 
          return self.narh != boshqa_avto.narh 
 
    def get_info(self): 
        return( 
            f"{self.rang} {self.make} {self.model} {self.yil}-yil. Narh:{self.narh}$" 
            ) 
 
avto = Avto ("BMW", "x7", "qora", 2020, 40000) 
avto1 = Avto ("toyota", "x7", "qora", 2020, 60000) 
avto2 = Avto ("BMW", "x7", "qora", 2020, 70000) 
avto3 = Avto ("kaptiva", "x7", "qora", 2020, 410000) 
avto4 = Avto ("BMW", "7", "qora", 2020, 4220000) 
avto5 = Avto ("kaptiva", "x7", "qora", 2020, 410000) 
avto6 = Avto ("toyota", "x7", "qora", 2020, 60000) 
 
class AvtoSalon: 
    """Avtolar klassi""" 
     
    def __init__(self, name): 
        self.name = name 
        self.kitoblar = [] 
         
    def __repr__(self): 
        return f"{self.name} avto salon1" 
     
    def __getitem__(self, index): 
        return self.avtolar[index] 
 
    def __setitem__(self, index, value): 
        if isinstance(value, Avto): 
            self.avtolar[index] = value 
     
    def __add__(self, qiymat): 
        if isinstance(qiymat, AvtoSalon): 
            yangi_salon = AvtoSalon(f"{self.name}{qiymat.name}") 
            yangi_salon.avtolar = self.avtolar + qiymat.avtolar 
            return yangi_salon 
        elif isinstance(qiymat, Avto): 
            self.add_avto(qiymat) 
        else: 
                return(f"AvtoSalon ga {type(qiymat)} qo`shib bo`lmaydi") 
             
    def __call__(self, *param): 
        if param: 
            for avto in param: 
                self.add_avto(avto) 
        else: 
            return [avto for avto in self.avtolar] 
    def add_avto(self, *qiymat): 
        for avto in qiymat: 
            if isinstance(avto, Avto): 
                self.avtolar.append(avto) 
            else: 
                return("Avto obyektini kiriting") 
             
    def get_list(self): 
        return [avto for avto in self.avtolar] 
     
 
salon1 = AvtoSalon("MaxAvto") 
salon2 = AvtoSalon("Avto lider") 
salon3 = AvtoSalon("Avto loy")

 
 
salon1.add_avto(avto1, avto2, avto3) 
salon2.add_avto(avto4, avto5, avto6) 
 
salon3.add_avto(avto2)

