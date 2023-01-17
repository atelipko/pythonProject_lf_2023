
def linkID(my_List):
    id = 0
    for i in range(len(my_List)-1):
        if i == 0:
            id += 1
            my_List[i].LinkID = id
        elif my_List[i].get_flag_end() and my_List[i].LinkID == -1:
            if my_List[i].name==my_List[i+1].name:
                my_List[i].LinkID = id
            else:
                if my_List[i].f_BC or my_List[i].f_RM:
                    my_List[i].LinkID = id
                id += 1
        elif my_List[i].LinkID == -1:
            my_List[i].LinkID = id

    if my_List[int(len(my_List)-1)].LinkID == -1:
        my_List[len(my_List)-1].LinkID = my_List[len(my_List)-2].LinkID





def LogicLines(my_list):
    for i in range(len(my_list)):
        my_list[i].numelemlist = i
        for j in range(len(my_list)):
            if my_list[i].name == my_list[j].name:
                my_list[j].ListLine.append(my_list[i].namber)
                my_list[j].posMyList.append(i)

    print(my_list[0].posMyList)
    print(my_list[1].posMyList)
    print(my_list[2].posMyList)
    print(my_list[3].posMyList)
    print(my_list[4].posMyList)
    print(my_list[5].posMyList)
    print(my_list[6].posMyList)
    print(my_list[10].posMyList)
    print(my_list[11].posMyList)


    print("_______________")


    LogicS(my_list)
    #linkID(my_list)
    linkID(my_list)
    print("end")

def LogicS(my_list):
    for i in range(len(my_list)):
        if my_list[i].f_strings == -1:
            for j in range(i, len(my_list)):
                if my_list[i].namber == my_list[j].namber:
                    if my_list[i].f_BC == 1 and my_list[j].f_BC == 1:
                        my_list[i].f_strings = 5
                        my_list[j].f_strings = 5
                    elif my_list[i].f_RM == 1 and my_list[j].f_RM == 1:
                        my_list[i].f_strings = 3
                        my_list[j].f_strings = 3
                    elif my_list[i].f_M == 1 and my_list[j].f_M == 1:
                        my_list[i].f_strings = 2
                        my_list[j].f_strings = 2
                    elif my_list[i].f_RM == 1 and my_list[j].f_BC == 1:
                        my_list[i].f_strings = 4
                        my_list[j].f_strings = 4
                    elif my_list[i].f_BC == 1 and my_list[j].f_RM == 1:
                        my_list[i].f_strings = 4
                        my_list[j].f_strings = 4
                    elif my_list[i].f_BC == 1 and my_list[j].f_M == 1:
                        my_list[i].f_strings = 0
                        my_list[j].f_strings = 0
                    elif my_list[i].f_M == 1 and my_list[j].f_BC == 1:
                        my_list[i].f_strings = 0
                        my_list[j].f_strings = 0
                    elif my_list[i].f_RM == 1 and my_list[j].f_M == 1:
                        my_list[i].f_strings = 1
                        my_list[j].f_strings = 1
                    elif my_list[i].f_M == 1 and my_list[j].f_RM == 1:
                        my_list[i].f_strings = 1
                        my_list[j].f_strings = 1








