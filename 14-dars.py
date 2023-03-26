# print("Kritilgan sonning kvadiratini qaytaruvchi dastur. ")
# savol="Istalgan son kriting. "
# savol+="(dasturni to'xtatish uchun 'exit' deb yozing )"
# qiymat=""
# while qiymat != "exit":
#     qiymat=input(savol)
#     if qiymat == "exit":
#         print(float(qiymat)**2)
# print("Dastur tugadi.") 



print("Kritilgan sonning kvadiratini qaytaruvchi dastur\n ")
savol="Istalgan son kriting\n>>> "
savol+="(dasturni to'xtatish uchun 'exit' deb yozing )\n"
ishora=True
while ishora:
    qiymat=input(savol)
    if qiymat == "exit":
        ishora=False
    else:
        print(float(qiymat)**2)
print("Dastur to'xtatildi! ")



print("Kritilgan sonning kvadiratini qaytaruvchi dastur\n ")
savol="Istalgan son kriting\n "
savol+="(dasturni to'xtatish uchun 'exit' deb yozing )\n"
ishora=True
while ishora:
    qiymat=input(savol)
    if qiymat != "exit":
        break
    else:
        print(float(qiymat)**2)
print("Dastur to'xtatildi! ")





# sonlar=list(range(1, 11))
# for son in sonlar:
#     if son == 5:
#         break
#     print(f"{son} ning kvadirati {son**2} ga teng")


# sonlar=list(range(1, 11))
# for son in sonlar:
#     if son ==5:
#         continue
#     print(f"{son} ning kvadirati {son**2} ga teng")




# from random import randint
# while True:
#     a=randint(1, 30)
#     b=randint(1, 30)
#     c=input("Javobni kriting: {a} * {b} dasturni to'xtatish uchun 'exit' deb yozing)\n>>> "
#     if c != "exit":
#         if c == int(a*b):
#             print("to'g'ri")
#         else:





