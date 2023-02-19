"""
Делаем список всех база база длина 'DN0002', 'DN0176', 410

"""


def getListData(List_data):
    my_list_BC_DC_L = []
    for i in range(len(List_data)):
        for j in range(len(List_data[i].my_list_Finih)):
            List_data[i].my_list_Finih[j].append(List_data[i].LinkID)
            List_data[i].my_list_Finih[j].append(List_data[i].fiber_note)
            my_list_BC_DC_L.append(List_data[i].my_list_Finih[j])

    """
    Получаем первые имена без дубляжа
        
    """
    temp_my_list=[]
    for i in range(len(my_list_BC_DC_L)):
        if i==0:
            temp_my_list.append(my_list_BC_DC_L[i][0])
        else:
            if temp_my_list.count(my_list_BC_DC_L[i][0])==0:
                temp_my_list.append(my_list_BC_DC_L[i][0])

    """
    Записываем данные в сортерованной форме
     
    """
    temp_my_list_BC_DC_L=[]
    for i in range(len(temp_my_list)):
        for j in range(len(my_list_BC_DC_L)):
            if temp_my_list[i]==my_list_BC_DC_L[j][0]:
                temp_my_list_BC_DC_L.append(my_list_BC_DC_L[j])
    my_list_BC_DC_L.clear()
    my_list_BC_DC_L=temp_my_list_BC_DC_L.copy()
    temp_my_list_BC_DC_L.clear()
    """Создаём и записываем в файл L1"""
    for i in range(len(temp_my_list)):
        f = open("./level1/"+temp_my_list[i]+".html", 'w')
        f.write("<html>" + '\n')
        f.write("<head><title>"+temp_my_list[i]+"</title></head>" + '\n')
        f.write('<link rel="stylesheet" href= "../css/style.css" type="text/css"/>' + '\n')
        f.write('<body>'+ '\n')
        f.write('<table id="table1" >'+ '\n')
        f.write('<thead>'+ '\n')
        f.write('<tr>'+ '\n')
        f.write('<th align="center">'"Ім'я A</th>" + '\n')
        f.write('<th align="center">'"Ім'я B</th>" + '\n')
        f.write('<th align="center">Довжина</th>'+ '\n')
        f.write('<th align="center">Кіл. ОВ</th>'+ '\n')
        f.write('</tr>'+ '\n')
        f.write('</thead>'+ '\n')
        f.write('<tbody>'+ '\n')
        for j in range(len(my_list_BC_DC_L)):
            if temp_my_list[i]==my_list_BC_DC_L[j][0]:
                f.write('<tr>' + '\n')
                f.write('<td align="center">'+my_list_BC_DC_L[j][0]+'</td>'+ '\n')
                f.write('<td align="center">'+my_list_BC_DC_L[j][1]+'</td>'+ '\n')
                f.write('<td align="center"><a href="../level2/'+my_list_BC_DC_L[j][0]+'-'+my_list_BC_DC_L[j][1]+'.html" target="content2">'+str(my_list_BC_DC_L[j][2])+'</a></td>'+ '\n')
                f.write('<td align="center">'+my_list_BC_DC_L[j][4]+'</td>'+ '\n')
                f.write('</tr>'+ '\n')
        f.write('</tbody>'+ '\n')
        f.write('</table>'+ '\n')
        f.write('</body>'+ '\n')
        f.write('</html>'+ '\n')
        f.close()

    """Создаём и записываем в файл L2 """
    for i in range(len(my_list_BC_DC_L)):
        f = open("./level2/"+my_list_BC_DC_L[i][0]+"-"+my_list_BC_DC_L[i][1]+".html", 'w')
        f.write("<html>" + '\n')
        f.write("<head><title>"+my_list_BC_DC_L[i][0]+"-"+my_list_BC_DC_L[i][1]+"</title></head>" + '\n')
        f.write('<link rel="stylesheet" href= "../css/style.css" type="text/css"/>' + '\n')
        f.write('<body>'+ '\n')
        f.write('<table id="table2" >'+ '\n')
        f.write('<thead>'+ '\n')
        f.write('<tr>'+ '\n')
        f.write('<th align="center">'"Ім'я</th>" + '\n')
        f.write('<th align="center">'"Адреса</th>" + '\n')
        f.write('<th align="center">Довжина</th>'+ '\n')
        f.write('</tr>'+ '\n')
        f.write('</thead>'+ '\n')
        f.write('<tbody>'+ '\n')
        for j in range(len(List_data)):
            if List_data[j].LinkID==my_list_BC_DC_L[i][3]:
                tempvar=1
                for m in range(len(List_data[j].my_list_note)):
                    if tempvar % 2 != 0:
                        f.write('<tr>'+ '\n')
                        f.write('<td align="center">' + List_data[j].my_list_note[m].name + '</td>' + '\n')
                        f.write('<td align="center">' + List_data[j].my_list_note[m].adress + '</td>' + '\n')
                        f.write('<td align="center"rowspan="2">' + str(List_data[j].my_list_note[m].lgth) + '</td>' + '\n')
                        f.write('</tr>' + '\n')
                        tempvar+=1
                    else:
                        f.write('<tr>' + '\n')
                        f.write('<td align="center">' + List_data[j].my_list_note[m].name + '</td>' + '\n')
                        f.write('<td align="center">' + List_data[j].my_list_note[m].adress + '</td>' + '\n')
                        f.write('</tr>' + '\n')
                        tempvar += 1
        f.write('</tbody>' + '\n')
        f.write('</table>' + '\n')
        f.write('</body>' + '\n')
        f.write('</html>' + '\n')
        f.close()



    print(temp_my_list)


    print(my_list_BC_DC_L)

    print(len(my_list_BC_DC_L))