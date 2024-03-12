# list -> iterable
        # tartiblangan
        # indekslangan
        # o'zgaruvchan
        # harqanday ma'lumot turalrini saqlay oladi
        # []



# lst = [12, 3.4, "qonday", True]

# for i in lst[2]:
    # print(i, end=" ")


# lst = [23, 45, 6, "12", "4", "78"]
# print(sum(lst[:3]))

# for i in range(len(lst)):
    # lst[i] = int(lst[i])

# print(sum(lst))
# print(type(lst[4]))


# lst = [i for i in input(">>> ").split()]
# print(lst)


# num = int(input(">>> "))
# print("Musbat") if num > 0 else print("Manfiy") if num < 0 else print("0")


# lst = [i if i % 2 == 0 else i * 2 for i in range(1, 11)]
# print(lst)


# lst = [12, 45] * 10
# print(lst)


# lst = ["Alik", "saLoM"]
# nat = [j for i in lst if isinstance(i, str) for j in i if j.isupper()]
# print(nat)


# lst = [12, 45, 67]
# lst2 = ["gg", "cc"]
# lst2.reverse()
# print(lst2)
# lst3 = lst + lst2
# print(lst3)

# gg = "".join(lst2)
# print(gg)


# lst = [1, 2, 3]
# lst2 = ["wer", "wel"]

# lst.extend(lst2)
# lst.insert(1, 56)

# print(lst)


# lst = [7, 2, 0, 3, 4, 4, 2, 5, 0]
# lst2 = []

# for i in lst:
    # if i not in lst2:
        # lst2.append(i)

# for i in lst:
    # if lst.count(i) > 1 and i not in lst2:
        # lst2.append(i)

# print(lst2)


# lst = ["ALi", "Well", "qOndAy", "Is", 23, 56, True]
# count = 0

# for i in lst:
    # if isinstance(i, str):
        # if i[0].isupper():
            # count += 1

# print(count)


# lst = [12, 4, 6 ,3 ,78, -9, -123, "welcome", "shet"]
# max = 0
# max_index = 0
# min = 0
# min_index = 0

# for index, data in enumerate(lst):
    # if isinstance(data, int):
        # max = data
        # min = data
        # break

# for index, data in enumerate(lst):
    # if isinstance(data, int):
        # if max < data:
            # max = data
            # max_index = index
        # if min > data:
            # min = data
            # min_index = index

# print(f"Max -> {max}\nMin -> {min}")

# print(lst)

# lst[max_index], lst[min_index] = lst[min_index], lst[max_index]

# print(lst)



"""---------- Ternary if ----------"""


# num = int(input(">>> "))
# 
# print("Juft") if num % 2 == 0 else print("Toq")

# print("Musbat") if num > 0 else print("Manfiy") if num < 0 else print("This number is", 0)