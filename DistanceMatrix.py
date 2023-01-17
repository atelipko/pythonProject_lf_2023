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
    SetPosMatrix(my_list)


def SetPosMatrix(my_list):

    # создаем списак имен
    tempList= []
    for i in range(len(my_list_Mat)):
        tempList.append(my_list_Mat[i].name)
    for i in range(0, len(my_list)):
        my_list[i].set_posMatrix(tempList.index(my_list[i].name))

    for i in range(len(tempList)):
        matrixDist=[[0] * len(tempList) for r in range(len(tempList))]

    tempList.clear()

    setValueDis(my_list,matrixDist)

def setValueDis(my_list,matrixDist):

    for i in range(len(my_list)):
        for j in range(i,int(len(my_list))):
            if my_list[i].get_posMatrix()==my_list[j].get_posMatrix():
                matrixDist[my_list[i].posMatrix][my_list[j].posMatrix]=-1
            elif my_list[i].get_namber()==my_list[j].get_namber():
                matrixDist[my_list[i].posMatrix][my_list[j].posMatrix] = my_list[j].lgth
                matrixDist[my_list[j].posMatrix][my_list[i].posMatrix] = my_list[j].lgth


    #print(matrixDist)
    for i in range(len(my_list)):
        if my_list[i].get_posMatrix()!=-1:
            my_list[i].matrixDist=matrixDist[my_list[i].posMatrix]
    #getMatrixDist(matrixDist)