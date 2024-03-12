# f = open("first.txt", 'w')

# f.write("Welcome\n")
# f.write("Hi\n")

# lst = [1,2,3,4,5]

# s = "".join([str(i) for i in lst])

# f.write(f"{s}\n")

# f.write(f"Name -> {input('Name: ')}\n")
# f.write(f"Surename -> {input('Surename: ')}\n")

# f.writelines(s)

# f.close()


"""-----------------------------------------------------------------------"""


# f = open("first.txt", "r")

# result = f.read()
# count = 1

# for i in result.split("\n"):
    # if count != 3:
        # print(i)
    # count += 1

# print(f.read().lower().count('a'))

# result = f.read(7)
# result = f.read(9)
# result = f.read(15)
# print(result)

# result = f.readline()
# print(result)

# lst = f.read().split('\n')
# print(lst[4][::-1])

# f.close()


"""-----------------------------------------------------------------------"""


# f = open("first.txt", 'r')
# fmus = open("musbat.txt", 'w')
# fman = open("manfiy.txt", "w")
# fnul = open("null.txt", "w")

# for i in f.read().split(" "):
    # if int(i) > 0:
        # fmus.write(f"{str(i)} ")
    # elif int(i) < 0:
        # fman.write(f"{str(i)} ")
    # else:
        # fnul.write(f"{str(i)} ")

# f.close()
# fmus.close()
# fman.close()
# fnul.close()


"""-----------------------------------------------------------------------"""


# f = open("first.txt", "r")

# print(f.read())

# f.seek(0)

# print(f.read())

# f.close()


"""-----------------------------------------------------------------------"""

# st = set()

# f = open("emails.txt", "r")

# for i in f.read().split("\n"):
    # find = i.rfind('.')
    # st.add(i[find:])

# print(st)


# f.close()


"""-----------------------------------------------------------------------"""


# f = open("phone_numbers.txt", "r")

# st1 = set()
# lst = list()

# for i in f.read().split("\n"):
    # find = i.find(" ")
    # st1.add(i[find:find+3])
    # if len(set(i[8:])) == 8:
        # lst.append(i)

# print(st1)
# print(lst)

# f.close()


"""-----------------------------------------------------------------------"""


# with open("name_surename.txt", 'r') as f:
    # lst = f.read().split("\n")
    # lst = sorted(lst, key=lambda x: x[1][0])

    # for i in lst:
        # print(i)


"""-----------------------------------------------------------------------"""


# with open("map.txt", "r") as f:
    # dct = dict()

    # lst = list()

    # for i in f.read().split('\n'):
        # lst.append(i.split(','))      

    # for i in lst:
        # if i[0].isdigit():
            # dct[i[-1]] = i[0]

    # print(dct)


"""-----------------------------------------------------------------------"""


# with open("internet.txt", "r") as f:
    # st = set()
    # lst = list()
    # dct = dict()

    # for i in f.read().split('\n'):
        # lst.append(i.split(","))

    # for i in lst:
        # find = i[0].rfind('.')
        # st.add(i[0][find:])

    # f.seek(0)

    # s = f.read()

    # for i in st:
        # dct[i] = s.count(i)

    # print(dct)


"""-----------------------------------------------------------------------"""