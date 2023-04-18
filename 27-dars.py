class Avto:
    
    __num_avto = 0
    
    def __init__(self, make, model, rang, yil, narh, km=0):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.km = km
        Avto.__num_avto += 1
        
    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto
       
    def get_km(self):
        return self.__km
    
    def __str__(self):
        return f"Avto: {self.make} {self.model}. {self.narh}$"
    
    def repr(self):
        return f"Avto: {self.make} {self.model}. {self.narh}$"
    
    def __gt__(self, y):
        return self.narh > y.narh
    
    def __lt__(self, y):
        return self.narh > y.narh
    
    def __le__(self, boshqa_avto):
        return self.narh >= boshqa_avto.narh
    
    def __ge__(self, boshqa_avto):
        return self.narh >= boshqa_avto.narh
    
    def __eq__(self, boshqa_avto):
        return self.narh == boshqa_avto.narh
    
    def __ne__(self, boshqa_avto):
        return self.narh != boshqa_avto.narh
    
    def get_info(self):
        return (
            f"{self.rang} {self.make} {self.model}. {self.yil} - yil. Narhi: {self.narh}$")


avto1 = Avto("GM", "Malibu", "Qora", 2020, 40000, 1000)
avto2 = Avto("GM", "Captiva", "Oq", 2016, 31000, 1000)
avto3 = Avto("GM", "Lacetti", "Qora", 2010, 11000, 1000)
avto4 = Avto("GM", "Tracker", "Qora", 2021, 35000, 1000)
avto5 = Avto("GM", "Nexia 3", "Qizil", 2013, 9000, 1000)



















