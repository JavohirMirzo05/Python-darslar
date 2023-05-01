class Kitob:
    """kitob haqida"""
     
    __num_kitob=0
    
    def __init__(self, title, part, page, isbn, narhi=0):
        self.title=title
        self.page=page
        self.part=part
        self.__isbn=isbn
        self.__narhi=narhi
        
        @classmethod
        def get_num_kitob(cls):
            return cls.__num_kitob
        
    def get_isbn(self):
        return self.__isbn
    
    def get_narh(self):
        return self.__narh

    def get_info(self):
        return f"{self.title} kitob nomi. {self.part}. {self.page} dan iborat. "
            
kitob1 = Kitob("Uvq", "Uch qism", 325, 125825985)    
    
            
     
             
            