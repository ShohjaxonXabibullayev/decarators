#1
# def deco(func):
#     def wrapper(*args):
#         for i in args:
#             result = i * 2
#             func(result)
#     return wrapper
#
# @deco
# def kopaytirish(a):
#     print(a)
#
# kopaytirish(2, 5, 10, 6)

#2
# def deco(func):
#     def wrapper(*args):
#         for i in args:
#             result = f"Xush kelibsiz {i}"
#             func(result)
#     return wrapper
#
# @deco
# def salom(a):
#     print(a)
#
# salom('Shohjaxon', 'Zafar')

#3
# def manfiy_tekshiruvchi(func):
#     def wrapper(*args, **kwargs):
#         for arg in args:
#             if isinstance(arg, (int, float)) and arg < 0:
#                 print("Manfiy son bor — funksiya bajarilmadi.")
#                 return
#         return func(*args, **kwargs)
#     return wrapper
#
# @manfiy_tekshiruvchi
# def salom(a, b, c):
#     print(f"Natija: {a + b + c}")
#
# salom(1, 2, 3)
# salom(1, -2, 3)

#4
# def deco(func):
#     def wrapper(*args):
#         for i in args:
#             if i < 10:
#                 func(i)
#             else:
#                 print("10 dan katta son qabul qilinmaydi")
#     return wrapper
#
# @deco
# def kichik(a):
#     print(a)
#
# kichik(50, 5, -2, 1, 80)

#5
# import math
# def deco(func):
#     def wrapper(*args):
#         for r in args:
#             if r > 0:
#                 result = math.pi*(r**2)
#                 func(result)
#             else:
#                 print("Siz xato son kiritidingiz")
#     return wrapper
#
# @deco
# def doira(a):
#     print(a)
#
# doira(7, 9, -5, 4)

#6
# database = ['Shohjaxon0525', 'Shahriyor19', 'Javohir12']
# def deco(func):
#     def wrapper(*args):
#         for i in args:
#             if i[0].isdigit() or i[-1].isalpha():
#                 print("Siz xato username yozdingiz")
#             else:
#                 if i in database:
#                     result = f"Tabriklaymiz {i} siz tizimga kirdingiz"
#                     func(result)
#                 else:
#                     print("siz hali ro'yhatdan o'tmagan ekansiz")
#     return wrapper
#
# @deco
# def identification(a):
#     print(a)
#
# identification('Shohjaxon0525', 'Javohir', 'Alisher18')

#7
# def harf_oraliq(start, end):
#     start, end = sorted([start, end])
#     for code in range(ord(start), ord(end) + 1):
#         yield chr(code)
#
# for harf in harf_oraliq('c', 'h'):
#     print(harf, end=' ')

#8
# def fayl_generator(fayl_nomi):
#     with open(fayl_nomi, 'r') as fayl:
#         for satr in fayl:
#             yield satr.strip()
#
# for satr in fayl_generator('matn.txt'):
#     print(satr)

#9
# def temple_strings(obj, feature):
#     return f"{obj} are {feature}"

#10
# def repeat_str(repeat, string):
#     return string.replace(string, repeat*string)

#12
# def get_drink_by_profession(profession):
#     drinks = {
#         "jabroni": "Patron Tequila",
#         "school counselor": "Anything with Alcohol",
#         "programmer": "Hipster Craft Beer",
#         "bike gang member": "Moonshine",
#         "politician": "Your tax dollars",
#         "rapper": "Cristal"
#     }
#
#     return drinks.get(profession.lower(), "Beer")

















