"""----------  SET -> iterable  ----------
    Turli xil ma'lumot turlarini saqlay oladi lekin iterablelardan faqat tuple va stringni saqlay oladi va tuplening ichida boshqa iterablelar bo'lmasligi kerak
    Tartiblanmagan
    Indekslanmagan
    Ham o'zgaruvchan ham o'zgarmas chunki SET indekslanmagan shuning uchun SETni ichidagi aniq bir ma'lumotni o'zgartirib bo'lmaydi
    Dublikat ma'lumotlarni saqlamaydi
    Shaxsiy qavusi yo'q set dictionaryning qavusidan foydalanadi shuning uchun SETni e'lon qilayotganda uni hohlagan nom = set() holda e'lon qilish kerak lekin qavus
    bilan e'lon qilmoqchi bo'lsak qavusni ichi bo'sh bo'lmasligi va qavusni ichida bittadan ko'p ma'lumot bo'lishi kerak
"""

# st = {"Apple", 12, 3.4, True, (2, 4)}
# print(st)


"""---------- SET methods ----------"""

st = {"Apple", "Microsoft", "Amazon", "Samsung"}

# st.add(46)  # .add() -> SETning ichiga list, tuple va dictionarydan tashqari har qanday ma'lumot turini qabul qila oladi
# print(st)


# st.clear()    # .clear() -> SETni ichini tozalab yuboradi
# print(st)


# st2 = st.copy()   # .copy() -> bir SETdagi barcha ma'lumotlarni ikkinchi SETga klon qilib beradi
# print(st2)


# result = st.pop() # .pop() -> ni ichiga hechqanday ma'lumot berilmaydi pop SETni ichidagi birinchi ma'lumotni o'chiradi agar SET bo'sh bo'lsa ERROR beradi
# print(st, result)


# st.remove("Apple")    # .remove() -> ni ichiga SETni ichida mavjud bo'lgan ma'lumot berilsa uni o'chiradi agar mavjud bo'lmagan ma'lumot berilsa ERROR beradi
# print(st)


# st.discard('Amazon')  # .discard() -> SETni ichida mavjud bo'lgan ma'lumotni o'chiradi agar mavjud bo'lmagan ma'lumot berilsa ERROR bermaydi
# print(st)


# st2 = {1, 2, 3, 4}

# st.update(st2)    # .update() -> ni ichida berilgan iterableni SETga qo'shadi 
# print(st)


# st2 = {1, 2, 3, 4}

# result = st.union(st2)    # .union() -> ni ichida berilgan iterableni SETga qo'shadi lekin SETga ta'sir qilmaydi va natija qaytaradi
# print(result)


# st = {'salom', 'kim', 'jj', 'well'}
# st2 = {'qalisan', 'kim', 'gg', 'salom'}

# print(st.isdisjoint(st2)) # .isdisjoint() -> ga murojat qilayotgan iterablening biror ma'lumoti .isdisjoint() ga berilgan iterableni ichida bor yoki yo'qligini aniqlaydi


# st = {'salom', 'kim', 'jj', 'well'}
# st2 = {'qalisan', 'kim', 'gg', 'salom'}

# print(st.issubset(st2))   # .issubset() -> ga murojat qilayotgan iterablening barcha ma'lumotlari .isdisjoint() ga berilgan iterableni ichida bor yoki yo'qligini aniqlaydi


"""---------- SET exercices ----------"""

# st = {"Apple", "Microsoft", "Amazon", "Samsung"}
# st2 = set()

# for i in st:
    # st2.add("".join(sorted(i)))

# print(st2)



"""----------  DICTIONARY -> iterable  ----------
    Ma'lumotlarni key va value ko'rinishida saqlaydi
    Key faqat primitive va tuple qabulqiladi
    Value har qanday ma'lumot turini qabul qiladi
    Tariblangan
    Indekslanmagan
    o'zgaruvchan
    Keylari dublikat bo'lmaydi        
"""


dct = {
    "Name" : "Corvette",
    "Color" : "black",
    "Max_speed" : "400 km"
}

# print(dct.get("Name"))

# print(dct["Max_speed"])
# print(dct)