import Class_Point
my_list_Mat = []        #матрица без дуближа
matrixDist=[[]]


# Подготовка матрици расстояний убераем дубляж.
def copiMatrix(my_list):
    #my_list_Mat=my_list.copy()
    temp=0
    for i in range(0, int(len(my_list))):
        if len(my_list_Mat)==0:
            my_list_Mat.append(my_list[i])
        else:
            for j in range(0, int(len(my_list_Mat))):
                if my_list[i].name==my_list_Mat[j].name:
                    temp=temp+1
            if temp ==0:
                my_list_Mat.append(my_list[i])
            else: temp=0

    print("my_list="+str(len(my_list))+ "   my_list_Mat= "+ str(len(my_list_Mat)))
    #my_list_dis = [[-1] * 1 for i in range(int(len(my_list_Mat)))]
    #disMatrix_1(my_list)
    SetPosMatrix(my_list)
#def setValueDis(i,j,list_v,namber)


def SetPosMatrix(my_list):
    a = Class_Point
    #for i in range(len(my_list_Mat)):
    #    my_list_dis=[[-1] * 1 for r in range(len(my_list_Mat))]
    # создаем списак имен
    tempList= []
    for i in range(len(my_list_Mat)):
        tempList.append(my_list_Mat[i].name)
    for i in range(0, len(my_list)):
        my_list[i].set_posMatrix(tempList.index(my_list[i].name))
    tempList.clear()
#def setValueDis(my_list):


        #for j in range(0, len(my_list_Mat)):
         #   if i==j:
          #     # my_list_dis[i][j]=0
           #     a = my_list[j]
            #    a.set_posMatrix(j)
        #    else:
        #        a = my_list[j]
        #        a.set_posMatrix(j)

#                for q in range(j, len(my_list_d)):
 #                   if a.get_namber()==my_list_d[q].get_namber():
 #                       w=int(a.get_lgth())
 #                       my_list_dis[i][j]=w
    print(" ")# + str(my_list_dis[0][0])+" " + str(my_list_dis[0][1])+" " + str(my_list_dis[0][2])+" " + str(my_list_dis[0][3])+" " + str(my_list_dis[0][4]))