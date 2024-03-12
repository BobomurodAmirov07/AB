import random
"""----------qiymat qaytaruvchi methodlar----------"""
# word1 = "Pythyon"
# word2 = "qonday"

# print(word2.capitalize())   #.capitalize() -> stringning 0-indeksida kichkinina harf bo'lsa uni katta harfga o'tkazadi

# print(word1.count("o"))    #.count() -> stringni ichida siz ko'rsatayotgan string nechi marta qatnashganini aniqlaydi

# print(word1.find("t"))    #.find() -> foydalanuvchi kiritgan string e'lon qilingan stringning qaysi indeksidaligini aniqlaydi

# print(word1.index("o"))    #.index() -> foydalanuvchi kiritgan string e'lon qilingan stringning qaysi indeksidaligini aniqlaydi (.find()) dan farqi agarda mavjud bo'lmagan string kiritilsa error qaytaradi

# print(word1.isalpha())    #.isalpha() -> string to'liqligicha harflardan tashkil topgan yoki yo'qligini aniqlaydi

# print(word1[3].isalpha())    #.isalpha() -> bilan stringning biror bir indeksi harf yoki yo'q ekanligini ham tekshirsa bo'ladi

# print(word1.upper())    #.upper() -> stringni ichidagi barcha harflarni katta harfga o'tkazadi

# print(word1.lower())    #.lower() -> stringni ichidagi barcha harflarni kichik harfga o'tkazadi

# ls = word1.split("y")
# print(ls)
# ls = word1.split("y", 1)
# print(ls)
# ls = word1.split(maxsplit=1)
# print(ls)

# word3 = "welcome replace"
# print(word3.title())    #.title() -> stringdagi har bir so'zning birinchi harfini katta harfga o'tkazadi

# word4 = "salom qonday gg salom salom"
# print(word4.replace("salom", "hi", 2))

# word5 = " + ".join("123456")
# print(word5)

# word6 = "1+2+3+4+5+6+7+8*9"
# print(eval(word6))    #eval() -> string faqat matematik amallardan tashkil topgan bo'lsa o'sha matematik amalni yechib beradi

# ls = ["12", "gg"]
# word7 = " ".join(ls)
# print(word7)



"""----------if, elif, else----------"""


# son = 4.5
# if son == int(son):
    # print(True)
# else:
    # print(False)


# son = int(input(">>> "))
# word = "FizzBuzz"
# 
# if son % 5 == 0 and son % 3 == 0:
    # print(word)
# elif son % 5 == 0:
    # print("Fizz")
# elif son % 3 == 0:
    # print("Buzz")
# else:
    # print(word[::-1])


# word = input(">>> ")

# if len(word) % 2 == 0:
    # print(word)
# else:
    # print(word[::-1])


# word = input(">>> ")

# if word == word.capitalize():
    # print(word.upper())
# else:
    # print(word[::-1])


# num = int(input(">>> "))
# 
# i = 1
# while i <= num:
    # j = 1
    # while j <= i:
        # print("*", end="")
        # j += 1
    # print()
    # i += 1


# word = input(">>> ")
# numbers = 0
# latters = 0
# 
# i = 0
# while i < len(word):
    # if word[i].isdigit():
        # numbers += 1
    # elif word[i].isalpha():
        # latters += 1
    # i += 1
# 
# print(f"Numbers -> {numbers}\nLatters -> {latters}")



# num = random.randint(1, 6)
# print(num)


# num = input(">>> ")
# num2 = num[::-1]
# num = int(num)
# num2 = int(num2)
# sum = num + num2
# print(f"{num} + {num2} = {sum}")


# word = input(">>> ")
# n = int(input(">>> "))

# print(word.replace(word[n], ""))