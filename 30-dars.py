# # try-except
# yosh = input("Yoshingizni kriting\n>>> ")
# try:
#     yosh = int(yosh)
#     print(f"Siz {2022-yosh} yilda tug'ilgansiz")
# except ValueError:
#     print("Butun son kriting")
    
# # try-except-else
# print("Dastur tugadi!")
    
# ...........................................................

# yosh = input("Yoshingizni kriting\n>>> ")
# try:
#     yosh = int(yosh)
# except ValueError:
#     print("Butun son kriting")
# else:
#     print(f"Siz {2022-yosh} yilda tug'ilgansiz")    

# ...................................................................

# x, y = 3, 10
# try:
#     print(y/(x-3))
# except ValueError:
#     print("0 ga bolib bo'lmaydi")    

# ...................................................

# mevalar = ["olma", "anor", "anjir", "uzum"]
# a= int(input("index kriting: "))
# index = a - 1
# try:
#     if len(mevalar) <= index:
#         mevalar[index]
# except IndexError:
#     print(f"Royhatda {len(mevalar)} ta meva bor xolos ")
# else:
#     print(mevalar[index])

# .............................................................................

# user = {"username": "sariqdev",
#         "status": "admin",
#         "email": "admin@sariq.dev",
#         "phone":99897123456}
# key = "adress"
# try:
#     print(f"Foydalanuvchi: {user[key]}")
# except KeyError:
#     print("bunday kalit mavjud emas")

# ...........................................................................

# filename = "pi.txt" 
# try:
#     with open(filename) as f:
#         text = f.read()
#         print(text)
# except FileNotFoundError:
#     print(f"Kechitasiz, {filename} fayil mavjud emas")

# ..........................................

# n = input("Butun son kriting\n>>> ")
# try:
#     n = int(n)
#     x=20/n
# except ValueError:
#     print("Butun son ktitmadingiz") 
# except ZeroDivisionError:
#     print("0 ga bo'lib bo'lmaydi")
# else:
#     x=20%n
#     print(x)    

# ...........................................................

# while True:
#     yosh = input("Yoshingizni kriting ")
#     if yosh .isdigit():
#         yosh = int(yosh)
#         break
# print(f"Siz {2022-yosh} yilda tug'ulgansiz")

# ......................................

# try:
#     x = int(input("Son kiriting\n>>> "))
#     y = int(input("Son kiriting\n>>> "))
#     print(x, "/", y, "=", x/y)
# except ZeroDivisionError:
#     print("0 ga bo'lib bo'lmaydi")
# except ValueError:
#     print("Bu son emas")
# except:
#     print("Xato yuz berdi")
        