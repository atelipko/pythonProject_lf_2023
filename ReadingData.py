import openpyxl
import Class_Point
def Read(name, my_list):
    book = openpyxl.open(name,data_only=True)
    sheet = book.active
    max_rows = sheet.max_row

    # Собираем структуру Point
    for i in range(6, max_rows+1):

        s = Class_Point.Point(sheet['A' + str(i)].value, sheet['C' + str(i)].value, sheet['D' + str(i)].value,
                              sheet['E' + str(i)].value, sheet['F' + str(i)].value, sheet['G' + str(i)].value,
                              sheet['L' + str(i)].value, sheet['M' + str(i)].value)
        my_list.append(s)
        s.set_flag()
        s = Class_Point.Point(sheet['A' + str(i)].value, sheet['C' + str(i)].value, sheet['H' + str(i)].value,
                              sheet['I' + str(i)].value, sheet['J' + str(i)].value, sheet['K' + str(i)].value,
                              sheet['L' + str(i)].value, sheet['M' + str(i)].value)
        my_list.append(s)
        s.set_flag()
        s.set_flag_end()
    book.close()