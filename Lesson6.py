# def create_dict(s:str):
    # dct = dict()

    # for i in s:
        # dct[i] = s.count(i)

    # return dct

# s = input("-> ")

# dct = create_dict(s)
# print(dct)


"""---------------------------------------------------------"""


# def reversed_int(i : int):
    # l = i
    # l = str(l)
    # print(l[::-1])

                 
# i = int(input("-> "))

# reversed_int(i)


"""---------------------------------------------------------"""


# def change(s : str):
    # lst = s.split()
    # for i in range(len(lst)):
        # lst[i] = list(lst[i])
        # lst[i][0], lst[i][-1] = lst[i][-1], lst[i][0]
        # lst[i] = "".join(lst[i])
        # lst[i] = lst[i] + " "

    # return "".join(lst)

# s = input("-> ")

# s = change(s)

# print(s)


"""---------------------------------------------------------"""


# def BooL(i : int):
    # i = str(i)
    # if i == i[::-1]:
        # print(True)
    # else:
        # print(False)

# i = int(input("-> "))

# BooL(i)


"""---------------------------------------------------------"""


# def changed_num(K : int, n : int):
    # K = str(K)
    # n = str(n)
    # n = K + n
    # n = int(n)
    # return n

# K = int(input("-> "))
# n = int(input("-> "))

# n = changed_num(K, n)

# print(n)


"""---------------------------------------------------------"""


# def change(gap : str):
    # w1 = input("-> ")
    # w2 = input("-> ")
    # w3 = input("-> ")

    # lst2 = list()
    # lst2.append(w1)
    # lst2.append(w2)
    # lst2.append(w3)

    # lst = gap.split()

    # for i in range(len(lst)):
        # for l in lst2:
            # if lst[i] == l:
                # lst[i] = "*" * len(l)

    # for i in range(len(lst)):
        # lst[i] = lst[i] + " "
    # 
    # return "".join(lst)

# gap = "salom bolalar kimdir Jama nimadir qachon sen va u kim Jamshid"
# print(change(gap))


"""---------------------------------------------------------"""


# def change(num : int):
    # lst = list(str(num))

    # for i in range(len(lst)):
        # print("".join(lst))
        # fr = lst[0]
        # lst.remove(fr)
        # lst.append(fr)

# num = 36985
# change(num)


"""---------------------------------------------------------"""


# def DicT(l1 : list, l2 : list, l3 : list):
    # dct = dict()
    # for i in range(len(l1)):
        # dct[l1[i]] = {l2[i] : l3[i]}     

    # return dct

# l1 = ["S001", "S002", "S003", "S004"]
# l2 = ["Ali", "Vali", "Sali", "Gali"]
# l3 = [86, 87, 88, 89]

# lst = [DicT(l1, l2, l3)]
# print(lst)


"""---------------------------------------------------------"""


# def DicT():
    # dct = dict()
    # while True:
        # s = input("-> ")
        # if s == 'exit':
            # break
        # l = 1
        # dct[l] = s
        # l += 1

    # return dct

# print(DicT())