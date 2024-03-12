lst = [12, 3.4, "good", True]

lst_s = ["welcome", "wel", "good", "ternary"]

lst_n = [12, 34, 56, 78]

# lst_a = lst[:]
# lst_a = lst.copy()

# print(lst_a)


# print(reversed(lst_s))


"""funksiyalardagi "key" -> parametri o'ziga metod, funksiya yoki class qabulqiladi"""

lst = ['1', "23", "45", "67", "89", "98", "76", "54", "32"]

# len = max(lst)

# len = max(lst, key=int)

# print(len)

# result = max(lst, key=lambda x: x[0])

# result = max(lst, key=lambda x: sum([int(i) for i in x]))

# print(result)


lst = ["baa", "aaa", "bba", "bbb", "aab", "aba"]

# result = sorted(lst, key= lambda x: x[::-1])

# print(result)

# result = sorted(lst, key=lambda x: "".join(sorted(x)))

# print(result)

# result = sorted(lst, key=lambda x: x.count('a'))

# print(result)



"""--------- tuple ----------"""


# tuple -> non primitive , tuple shaklanishi uchun tuple ning ichi bo'sh bo'lishi yoki kamida 2 ta ma'lumot bo'lishi kerak,
#  tuple ning ichida list mavjud bo'lsa uni o'zgartirish mumkin lekin tuple ning ichidagi stringni o'zgartirib bo'lmaydi 
    # tartiblangan
    # indekslangan
    # o'zgarmas
    # har qanday turdagi ma'lumotlarni saqlay oladi
    # ()

# tuple ni e'lon qilish turlari

tpl = tuple()
tpl = ()
tpl = (1, 2.3, "good", True)
tpl = 1, 2, 3, 4, "bad", False

# tpl = ([1, 2, 3], {2, 4, 6}, {"rang" : 2, "golos" : 3})
# tpl[1].add(45)
# tpl[2][1] = 34
# print(tpl)
# print(tpl[4].replace("a", "aa"))



"""---------------------------------------------------"""

# print(tpl.count(6))  # yo'q ma'lumot berilsa "0" qaytaradi
# print(tpl.index(6))  # yo'q ma'lumot berilsa ERROR beradi

"""---------------------------------------------------"""

tpl = (3, 2, 5, 1, 4)
# tpl = tuple(sorted(tpl))
# print(tpl)


# tpl = list(tpl)
# tpl.append("welcome")
# tpl = tuple(tpl)
# print(tpl)

"""---------------------------------------------------"""
"""---------- Exercice - 1 ----------"""


# tpl = (3, 2, 5, 1, 4)
# print(sum(tpl))



"""---------- Exercice - 2 ----------"""


# tpl = (2, 4, 6, 8)

# tpl = list(tpl)
# tpl.remove(max(tpl))
# tpl = tuple(tpl)

# print(tpl)



"""---------- Exercice - 3 ----------"""


# tpl = (3, 2, 5, 1, 4)

# result = max(tpl) - min(tpl)
# print(result)



"""---------- Exercice - 4 ----------"""


# tpl = ("welcome", "hello", "hi", "good", "starttt", "finish")
# lst = []

# for i in tpl:
    # if len(i) > 5:
        # lst.append(i)

# print(lst)



"""---------- Exercice - 5 ----------"""


# tpl = ((3, 1), (0, 0, 2), (1, 1, 1), (0, 4), (1, 9))
# lst = []

# for i in tpl:
    # lst.append(sum(i))

# print(lst)



"""---------- Exercice - 6 ----------"""


# tpl = ((1, 2, 3), (2, 2), (3, 0, 0))

# tpl = list(tpl)
# tpl.reverse()
# tpl = tuple(tpl)

# print(tpl)



"""---------- Exercice - 7 ----------"""


# tpl = ((1, 2), (3, 4), (8, 9))
# tpl_l1 = []
# tpl_l2 = []
# tpl_l3 = []

# for i in tpl:
    # tpl_l1.append(i[0])
    # tpl_l2.append(i[1])

# tpl_l1 = tuple(tpl_l1)
# tpl_l2 = tuple(tpl_l2)

# tpl_l3.append(tpl_l1)
# tpl_l3.append(tpl_l2)

# tpl_l3 = tuple(tpl_l3)

# print(tpl_l3)



"""---------- Exercice - 8 ----------"""


# lst = [[1, 2, 3], [4, 5, 6], [23, 45], [7, 8, 9]]

# result = max(lst, key= lambda x: sum(i for i in x))

# print(result)



"""---------- Exercice - 9 ----------"""


# lst = [(0, 2, 0, 0), (0, 3, 2, 2), (1, 3, 2, 4, 3), (4, 1, 2, 4)]

# for i in range(len(lst)):
    # lst[i] = list(lst[i])




"""---------- Exercice - 10 ----------"""


# lst = [(1,2), (3,4), (5,6)]

# for i in range(len(lst)):
    # lst[i] = list(lst[i])

# print(lst)



"""---------- Exercice - 11 ----------"""


# tpl = ("ada", 212, False, "aziza", 12.3)

# tpl = list(tpl)

# for i in range(len(tpl)):
    # tpl[i] = str(tpl[i])

# for i in tpl:
    # if i == i[::-1]:
        # print(f"{i} = palindrom")
    # else:
        # print(f"{i} = palindrom emas")



"""---------- Exercice - 12 ----------"""


# lst = [1, 2, 3]

# for i in range(len(lst)):
    # lst[i] = str(lst[i])

# lst = "".join(lst)
# lst = int(lst) + 1
# lst = str(lst)
# lst = list(lst)

# print(lst)



"""---------- Exercice - 13 ----------"""


# lst_a = [1, 2, 4, 5, 7, 3 , 12]
# lst_b = [2, 3, 6, 4, 12, 9, 7]
# new = []

# for i in lst_a:
    # for l in lst_b:
        # if i == l:
            # new.append(i)

# print(new)



"""---------- Exercice - 14 ----------"""


# lst = [5, 7, 8, 10]
# lst2 = []

# lst2.extend(lst)
# lst2.sort()

# if lst2 == lst:
    # print("tartiblangan")
# else:
    # print("tartiblanmagan")



"""---------- Exercice - 15 ----------"""


# tpl = ((1, 2, 3), (23, 54, 86, 99, 101), (3, 3, 3), (1, 2))
# lst = []

# tpl = list(tpl)

# result = max(tpl, key=lambda x: len(x))

# tpl.remove(result)

# for i in tpl:
    # lst.extend(i)

# tpl = tuple(lst)

# print(tpl)