# file=open("pi.txt")
# PI=file.read()
# print(PI)
# file.close()

# ..........................................


# # yopilishi
# with open("pi.txt") as file:
#     pi=file.read()
    
# print(pi)


# .......................................................


# with open("pi.txt") as file:
#     pi=file.read()
    

# pi=pi.rstrip() #yangi qator olib tashlaydi
# pi=pi.replace("\n", "") #o'rniga almashtirai
# pi=float(pi)
# print(pi)

# .................................................

# filename="data/text.txt"
# with open(filename) as file:
#     for line in file:
#         print(line)
        
# # ro'yhar ichiga saqlash

# with open(filename) as file:
#     talabalar=file.readlines()
    
# print(talabalar)

# talabalar=[talaba.rstrip() for talaba in talabalar]
# print(talabalar)


# ........................................................

# filename="Fayil/talaba.txt"
# with open(filename) as file:
#     for line in file:
#         print(line)
        
# with open(filename) as file:
#     talabalar=file.readlines()
    
# # print(talabalar)

# talabalar=[talaba.rstrip() for talaba in talabalar]
# print(talabalar)

# for talaba in talabalar:
#     print(f'{talaba} salom')

# ......................................................

# # yozish "w" write ustidan yozib yuboradi
fayilnomi="new_file.txt"
# ism ="Umar Hasan"
# tyil=1999
# with open(fayilnomi, "w") as fayl:
#     fayl.write(ism+ "\n")
#     fayl.write(str(tyil) + "\n")

# .......................................................

# # qo'shish yoki yangi yasash"a" apend

# with open(fayilnomi, "a") as fayl:
#     fayl.write("Alijon Valiev")
#     fayl.write("2000")

# .......................................

import pickle

talaba1 = {"ism": "hasan", "familiya": "husanov", "tyil": "2000", "kurs": "3"}

with open("info1", "wb") as file:
    pickle.dump(talaba1, file)
    
with open("info1", "rb") as file:
    talaba_1=pickle.load(file)
    # talaba_2=pickle.load(file)

print(talaba_1)
# print(talaba_2)











