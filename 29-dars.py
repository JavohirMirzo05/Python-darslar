import json
# # JSON (JavaScript Objekt Notation).

# # indent=4
# x=10
# x_json = json.dumps(x)

# .......................................

# y=5.5
# y_json = json.dumps(y)

# ........................................

# m=True
# m_json = json.dumps(m)
# m3 = json.loads(m_json)

# ......................................

# familiya = "davlatov"
# familiya_json = json.dumps(familiya)
# ism_json = json.dumps("davlat")

# ........................................

# sonlar = (12, 45, 23, 67)
# sonlar_json = json.dumps(sonlar)

# # python file qaytarish
# son2 = json.loads(sonlar_json)

# ..........................................

# bemor = {
#     "ism": "Alijon Valiev",
#     "yosh": 30,
#     "oila": True,
#     "farzandlar": ("Axmad", "Bonu"),
#     "allergiya": None,
#     "dorilar": [
#         {"nomi": "Tremol", "miqtori": 0.5},
#         {"nomi": "Pandol", "miqtori":1.2},
#         ],
#     }

# bemor_json = json.dumps(bemor)
# print(bemor_json)

# # yozish
# with open("bemor_j.json", "w") as f:
#     json.dump(bemor, f)
    
# .....................................     
    
# with open("sonlar_j.json", "w") as f:
#     json.dump(sonlar, f)

# ..........................................

# filename = "bemor_j.json"
# with open(filename) as f:
#     bemor = json.load(f)
# print(bemor)
# print(type(bemor))

# ...............................................

# uy ishi 

oquvchi = {
    "ism": "Durbek Davlatov",
    "yosh": 16,
    "oila": True,
    "otasi":True,
    "onasi":True,
    "farzandlar": None,
    "allergiya": None,
    "kitoblar": [
        {"kitob nomi": "Ufq", "varag'i": 369},
        {"kitob nomi": "O'tgan kunlar", "varag'i":410},
        ],
    }

oquvchi_json = json.dumps(oquvchi)
print(oquvchi_json)

# yozish
with open("oquvchi_j.json", "w") as f:
    json.dump(oquvchi, f)
    
















