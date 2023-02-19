# This is a sample Python script.
import ReadingData
import OutData
import LogicDist

# Press Shift+F10 to execute it or replace it with your code.
#import openpyxl
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

my_list=[] #Лист объектов
my_list_notes=[] #Лист узлов


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print(str(len(my_list)))
    ReadingData.Read("1.xlsx", my_list) # "new.xlsx"
    #DistanceMatrix.copiMatrix(my_list)
    LogicDist.LogicLines(my_list)


    #DistanceMatrix.disMatrix(DistanceMatrix.copiMatrix(my_list),my_list)
   # print(str(len(my_list)))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
