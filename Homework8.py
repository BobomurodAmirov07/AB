"""---------- Homework - 1 ----------"""

# with open("cars.tx", "r") as f:
    # f.seek(0)
    # lst = [i for i in f.read().split('\n') if i[0].isdigit()]
    
    # lst_s = list()

    # for i in range(len(lst)):
        # lst[i] = lst[i].split(",")
        # if lst[i][4] not in lst_s:
            # lst_s.append(lst[i][4])
        # lst[i] = ",".join(lst[i])

    # dct = dict()

    # s = "".join(lst)

    # for i in lst_s:
        # dct[i] = s.count(i)

    # max1 = max(dct, key=lambda x: dct[x])

    # lst_country = list()

    # for i in range(len(lst)):
        # lst[i] = lst[i].split(",")
        # if lst[i][4] == max1 and lst[i][-1] not in lst_country:
            # lst_country.append(lst[i][-1])

    # dct2 = dict()

    # lst2 = list()

    # for i in lst_country:
        # dct2[i] = s.count(i)
        # lst2.append(s.count(i))

    # max2 = max(dct2, key=lambda x: dct2[x])
    # min1 = min(dct2, key=lambda x: dct2[x])

    # max3 = max(lst2)
    # min2 = min(lst2)

    # print(f"Most of {max1}s is in the {max2} there are {max3} {max1} there\nMinimum of {max1} is in the {min1}there are {min2} {max1} there")

    # with open("letters_to_people.txt", "a") as f:

        # for i in range(len(lst)):
            # lst[i][5] = int(lst[i][5])
            # if lst[i][5] < 2005:
                # f.write(f"Kimdan : Auto Test Corp\nKimga : {lst[i][1]} {lst[i][2]}\nJoriy davlat : {lst[i][-1]}\n\nHurmatli {lst[i][1]} {lst[i][2]} {lst[i][4]} tomonidan {lst[i][5]} da ishlab chiqarilgan {lst[i][-2]} rangli autoulovingiz Texnik Holatni tekshirish maqsadida mahalliy Auto Test Corpga murojat qilishingizni so'raymiz\n\n\n---------------------------------------------------------------------------------------------------\n\n\n")
