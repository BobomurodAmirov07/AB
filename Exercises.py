# lst = []
# lst_a = [i for i in range(101)]
# count = 0

# for i in range(len(lst_a)):
    # lst_a[i] = str(lst_a[i])

# for i in lst_a:
    # for l in i:
        # if l == "3":
            # lst.append(i)
            # count += 1
# print(lst, count)


"""-------------------------------"""


# lst = [i for i in range(101)]

# for i in range(len(lst)):
    # lst[i] = str(lst[i])

# lst_a = [i for i in range(101)]

# for i in range(len(lst_a)):
    # lst_a[i] = str(lst_a[i])

# print(type(lst[4]))

# for index, data in enumerate(lst):
    # for i in lst_a:
        # if index % 2 != 0 and data[::-1] == i or i[::-1] == data:
            # print(f"{data} -> {i}\n")


"""-------------------------------"""


# num = input(">>> ")

# lst = []

# for i in num:
    # lst.append(int(i))

# for i in lst:
    # if i % 2 != 0:
        # print(i, end=" ")


"""-------------------------------"""


# lst = []

# while True:
    # num = input(">>> ")
    # if num == "c":
        # break
    # lst.append(num)

# for i in range(len(lst)):
    # lst[i] = int(lst[i])

# print(sum(lst))


"""-------------------------------"""


# lst = [1,2.4, "hi", True]

# for i in range(len(lst)):
    # lst[i] = type(lst[i])

# print(lst)


"""-------------------------------"""


# lst = [1, 2, 3, 5, 6, 0, 0, 0, 2, 4, 0]

# for i in range(len(lst)):
    # for l in range(i + 1, len(lst)):
        # if lst[i] == 0:
            # lst[i], lst[l] = lst[l], lst[i]

# print(lst)


"""-------------------------------"""


# lst = [11, 22, True, "ollo", "aziza"]

# for i in range(len(lst)):
    # lst[i] = str(lst[i])

# for i in lst:
    # if i == i[::-1]:
        # print(f"{i} -> palindrom")
    # else:
        # print(f"{i} -> not palindrom")


"""-------------------------------"""


# lst = ["abc", "xyz", "bo'lib" "aba", 1221]
# count = 0

# for i in range(len(lst)):
    # lst[i] = str(lst[i])

# for i in lst:
    # if len(i) > 2 and i[0] == i[-1]:
        # print(i)
        # count += 1

# print(count)


"""-------------------------------"""


# lst = [11, 22 ,33 ,44]

# for i in range(len(lst)):
    # lst[i] = str(lst[i])

# lst = ["".join(lst)]

# num = int(lst[0])

# print(num)


"""-------------------------------"""


# lst = [11, 22, 33, 44 ,55 ,66, 77, 88, 99]

# for i in lst:
    # if i % 2 == 0:
        # lst.remove(i)

# print(lst)