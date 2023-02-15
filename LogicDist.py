import Class_Note
import OutData
import OutDataHTML

from main import my_list_notes


def linkID(my_List):
    id = 0
    for i in range(len(my_List)-1):
        if i == 0:
            id += 1
            my_List[i].LinkID = id
            s = Class_Note.Note(id)
            my_list_notes.append(s)
        elif my_List[i].get_flag_end() and my_List[i].LinkID == -1:
            if my_List[i].name==my_List[i+1].name:
                my_List[i].LinkID = id
            else:
                if my_List[i].f_BC or my_List[i].f_RM:
                    my_List[i].LinkID = id
                id += 1
                s = Class_Note.Note(id)
                my_list_notes.append(s)
        elif my_List[i].LinkID == -1:
            my_List[i].LinkID = id

    if my_List[int(len(my_List)-1)].LinkID == -1:
        my_List[len(my_List)-1].LinkID = my_List[len(my_List)-2].LinkID

def LogicS(my_list):
    for i in range(len(my_list)):
        if my_list[i].f_strings == -1:
            for j in range(i, len(my_list)):
                if my_list[i].namber == my_list[j].namber:
                    if my_list[i].f_BC == 1 and my_list[j].f_BC == 1:
                        my_list[i].f_strings = 5
                        my_list[j].f_strings = 5
                        #break
                    elif my_list[i].f_RM == 1 and my_list[j].f_RM == 1:
                        my_list[i].f_strings = 3
                        my_list[j].f_strings = 3
                        #break
                    elif my_list[i].f_M == 1 and my_list[j].f_M == 1:
                        my_list[i].f_strings = 2
                        my_list[j].f_strings = 2
                        #break
                    elif my_list[i].f_RM == 1 and my_list[j].f_BC == 1:
                        my_list[i].f_strings = 4
                        my_list[j].f_strings = 4
                        #break
                    elif my_list[i].f_BC == 1 and my_list[j].f_RM == 1:
                        my_list[i].f_strings = 4
                        my_list[j].f_strings = 4
                        #break
                    elif my_list[i].f_BC == 1 and my_list[j].f_M == 1:
                        my_list[i].f_strings = 0
                        my_list[j].f_strings = 0
                        #break
                    elif my_list[i].f_M == 1 and my_list[j].f_BC == 1:
                        my_list[i].f_strings = 0
                        my_list[j].f_strings = 0
                        #break
                    elif my_list[i].f_RM == 1 and my_list[j].f_M == 1:
                        my_list[i].f_strings = 1
                        my_list[j].f_strings = 1
                        #break
                    elif my_list[i].f_M == 1 and my_list[j].f_RM == 1:
                        my_list[i].f_strings = 1
                        my_list[j].f_strings = 1
                        #break

def helpRmListID(my_list):
    for i in range(len(my_list)):
        if my_list[i].f_RM == 1: #and len(my_list[i].posMyList) > 2:
            if len(my_list[i].LinkIdList) == 0:
                for j in range(len(my_list[i].posMyList)):
                    #a = my_list[i].posMyList[j]
                    my_list[i].LinkIdList.append(my_list[my_list[i].posMyList[j]].LinkID)
           # print("my_list[i].LinkIdList= " + str(my_list[i].LinkIdList) + " i= "+str(i))


def LogicLines(my_list):
    for i in range(len(my_list)):
        my_list[i].numelemlist = i
        for j in range(len(my_list)):
            if my_list[i].name == my_list[j].name:
                my_list[j].ListLine.append(my_list[i].namber)
                my_list[j].posMyList.append(i)



    LogicS(my_list)
    linkID(my_list)
    helpRmListID(my_list)

    for i in range(len(my_list_notes)):
        my_list_notes[i].setitemNote(my_list)
        my_list_notes[i].TypeDefinitionNode()
        my_list_notes[i].setSumLgth()
        if my_list_notes[i].TypeNode==1:
            my_list_notes[i].Definition_J()
    for i in range(len(my_list_notes)):
        if my_list_notes[i].TypeNode==2:
            my_list_notes[i].DefinitiFinih(my_list_notes)
    OutData.example(my_list_notes)
    OutDataHTML.getListData(my_list)

"""
    print("________________")
    print(str(len(my_list_notes)))
    print(str(my_list_notes[0].TypeNode) + "  FinihDefinition = " +str(my_list_notes[0].FinihDefinition) +"____"+ str(my_list_notes[0].my_list_Finih))
    print(str(my_list_notes[1].TypeNode) + "  FinihDefinition = " +str(my_list_notes[1].FinihDefinition) +"____"+ str(my_list_notes[1].my_list_Finih))
    print(str(my_list_notes[2].TypeNode) + "  FinihDefinition = " +str(my_list_notes[2].FinihDefinition) +"____"+ str(my_list_notes[2].my_list_Finih))
    print(str(my_list_notes[3].TypeNode) + "  FinihDefinition = " +str(my_list_notes[3].FinihDefinition) +"____"+ str(my_list_notes[3].my_list_Finih))
    print(str(my_list_notes[4].TypeNode) + "  FinihDefinition = " +str(my_list_notes[4].FinihDefinition) +"____"+ str(my_list_notes[4].my_list_Finih))
    print(str(my_list_notes[5].TypeNode) + "  FinihDefinition = " +str(my_list_notes[5].FinihDefinition) +"____"+ str(my_list_notes[5].my_list_Finih))

    print(str(my_list_notes[1].my_list_J))
    print(str(my_list_notes[1].my_list_J_J))
    print("end")
"""
