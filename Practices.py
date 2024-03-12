# with open("first.txt", "r") as f:
    # lst = f.read().split()
    # lst.sort()
    # print(lst)


"""---------------------------------------------------------"""


# with open("booking.txt", "r") as file:
    # lst = file.read().split()

    # for i in range(len(lst)):
        # lst[i] = lst[i].split(',')

    # money = int((input(">>> ")))

    # lst_ex = list()
    # lst_che = list()

    # for i in range(len(lst)):
        # lst[i][-1] = lst[i][-1].replace("$", "")
        # lst[i][-1] = float(lst[i][-1])
        # lst[i][-1] = int(lst[i][-1])
        # if lst[i][-1] == money - 50:
            # lst_che.append(lst[i])
        # elif lst[i][-1] == money + 100:
            # lst_ex.append(lst[i])
            
    # print(f"100 $ more expensive tickets\n{lst_ex}")
    # print(f"50 $ cheaper tickets\n{lst_che}")


"""---------------------------------------------------------"""


# with open("booking.txt", "r") as file:
    # lst = file.read().split()

    # for i in range(len(lst)):
        # lst[i] = lst[i].split(',')

    # lst2 = list()
    # for i in range(12, 22):
        # lst2.append(i)

    # country = input("Enter name of country in this mode 'RU', 'UZ', 'US' and etc: ")

    # lst_coun = list()

    # for i in lst:
        # for l in lst2:
            # find = i[2].find(':')
            # if country == i[3] and int(i[2][:find]) == l:
                # lst_coun.append(i)

    # print(lst_coun)


"""---------------------------------------------------------"""


# with open("booking.txt", "r") as file:
    # lst = file.read().split()

    # for i in range(len(lst)):
        # lst[i] = lst[i].split(',')

    # country = input("Enter name of country in this mode 'RU', 'UZ', 'US' and etc: ")

    # lst_ar = list()

    # for i in lst:
        # find = i[4].find(':')
        # if i[3] == country and int(i[4][:find]) == 20:
            # lst_ar.append(i)

    # print(lst_ar)


"""--------------------------------------------------------"""


# with open("numbers.txt", "r") as file:
    # lst = file.read().split("+")
    # lst.pop(0)
    # print(lst[10])

    # for i in range(len(lst)):
        # lst[i] = "+" + lst[i]
        # print(lst[i])


"""--------------------------------------------------------"""


# with open("numbers.txt", "r") as file:
    # lst = file.read().split("+")
    # lst.pop(0)

    # for i in range(len(lst)):
        # lst[i] = "+" + lst[i]

    # print(f"1.Beelineni tanlash uchun 1ni bosing\n2.Uzmobileni tanlash uchun 2ni bosing\n3.MobiUz tanlash uchun 3ni bosing\n4.Humansni tanlash uchun 4ni bosing\n")
    # choice = input(">>> ")

    # s = str()

    # if choice == '1':
        # print("90\n91\nshulardan birini tanlang")
        # n = input(">>> ")
        # if n == '90' or n == '91':
            # s = n
    # elif choice == '2':
        # print("95\n99\nshulardan birini tanlang")
        # n = input(">>> ")
        # if n == '95' or n == '99':
            # s = n
    # elif choice == '3':
        # print("88\n97\nshulardan birini tanlang")
        # n = input(">>> ")
        # if n == '88' or n == '97':
            # s = n
    # elif choice == '4':
        # s = '33'

    # s_phone = str()

    # lst_phone = list()

    # for i in range(len(lst)):
        # lst[i] = lst[i].replace("\n", "")

    # for i in lst:
        # if i[5:7] == s:
            # lst_phone.append(i)

    # print(f"{lst_phone} choose one of them: ")
    # s_phone2 = input(">>> ")

    # for i in lst_phone:
        # find = i.find(" ")
        # if i[find:-1] == s_phone2:
            # s_phone = i

    # for i in lst:
        # find = i.find(" ")
        # if s_phone == i[find:-1]:
            # lst.remove(i)

    # f = open("numbers.txt", "w")
    
    # for i in lst:
        # f.write(f"{i}\n")

    # f.close()


"""--------------------------------------------------------"""


# with open("countrys.txt", "r") as file:
    # lst = file.read().split("\n")

    # for i in lst:
        # find = i.find(",")
        # rfind = i.rfind(",")
        # if int(i[find+1:rfind]) > 1000000:
            # print(i)


"""--------------------------------------------------------"""


# with open("products.txt", "r") as f:
    # lst = f.read().split("\n")

    # for i in range(len(lst)):
        # lst[i] = lst[i].split(",")

    # for i in lst:
        # i[-2] = i[-2].replace("$", "")
        # i[-2] = float(i[-2])
        # i[-2] = int(i[-2])
        # if i[-2] >= 500 and i[-2] <= 1000 and i[-1] == 'true':
            # print(f"{i[0]} {i[-3]}\n")

    # product = input("Enter name of product: ")
    # lst_p = list()

    # product = product.capitalize()

    # for i in lst:
        # i[-2] = i[-2].replace("$", "")
        # i[-2] = float(i[-2])
        # if product == i[-3] and i[-1] == 'true':
            # lst_p.append(i[-2])

    # lst_p.sort()

    # if len(lst_p) > 0:
        # print(f"Here are all price of products which is made of {product}\n{lst_p}")
    # else:
        # print("There is no products that is made of", product)

    # for i in lst:
        # i[-2] = i[-2].replace("$", "")
        # i[-2] = float(i[-2])
        # if i[-2] < 1000 and i[-1] == "false":
            # print(i[-2])


"""--------------------------------------------------------"""

# try:
    # print('2' + 2)+
# except Exception as e:
    # print(f"Nimadir hatolik bor {e}")



"""--------------------------------------------------------"""

# n = int(input())

# if n < 10:
    # print(n + 3)
# else:
    # raise Exception("Fuck you, enter number greater than 10 bitch")



"""--------------------------------------------------------"""

# num1 = int(input("Raqam kiriting: "))
# shart = input("Matematik amal kiriting: ")
# num2 = int(input("Raqam kiriting: "))

# try:
    # if shart == "+":
        # print(num1 + num2)
    # elif shart[1] == "-":
        # print(num1 - num2)
    # elif shart[1] == "/":
        # print(num1 // num2)
    # elif shart[1] == "*":
        # print(num1 * num2)
    # else:
        # raise Exception("Matematik shart kiritilmadi")
# except ZeroDivisionError:
    # print(ZeroDivisionError)
# except TypeError:
    # print(TypeError)
# except ValueError:
    # print(ValueError)
# except Exception as e:
    # print(e)
# else:
    # print("Good job")



"""--------------------------------------------------------"""

# lst = [1, 2, 3, 4, 5, " "]
# count = 0

# for i in lst:
    # if isinstance(i, int):
        # count +=1

# if len(lst) != count:
    # raise Exception("List raqamlardan tashkil topmagan")



"""--------------------------------------------------------"""