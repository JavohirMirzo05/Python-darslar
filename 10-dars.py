# yosh = "18"
# print(yosh.isdigit)



# yosh=input("Yoshingiz nechida? ")
# if yosh.isdigit():
#     yosh=float(yosh)
# else:
#     print("Matinli raqam")


# from random import randint

# a=randint(1, 11)
# b=randint(1,11)

# c=int(input("{} + {}=". format(a,b)))

# if c ==(a + b):
#     print("To'g'ri!")
# else:
#     print("Xato?")


from random import randint
print("O'zingizni Matematikada sinab ko'ring! ")
print("Matematikadan amallardan birini tanlang: ")
amallar=["ayirish", "bo'lish", "qo'shish", "kopaytirish" ]

son=1
for amal in amallar:
    print(son, "-", amal, end=("\n"))
    son += 3
    
amal=input("Tanlagan amalingizni kriting!\n>>> ")
if amal == "1":
    a=randint(50, 100)
    b=randint(1, 10)
    print("misol javobini kriting")
    c=int(input("{} - {} =".format(a,b)))
    if c ==(a - b):
        print("Javob to'g'ri!") 
# else:
#         print("Javob hato")

elif amal =="2":
    
    a=randint(50, 100)
    b=randint(1, 10)
    
    print("misol javobini kriting")
    c=int(input("{} / {} =".format(a,b)))
    if c ==(a / b):
        print("Javob to'g'ri!") 
# else:
#         print("Javob hato")

if amal == "3":
    
    a=randint(1, 100)
    b=randint(1, 100)
    print("misol javobini kriting")
    c=int(input("{} + {} =".format(a,b)))
    if c ==(a + b):
        print("Javob to'g'ri!") 
# else:
        # print("Javob hato")


if amal == "4":
    
    a=randint(1, 100); b=randint(1, 100); print("misol javobini kriting")
    c=int(input("{} * {} =".format(a,b)))
    if c ==(a * b):
        print("Javob to'g'ri!") 
        
else:
        print("Javob hato")







