import xlwt
import xlrd
from statistics import mean


workbook = xlrd.open_workbook('test.xlsx')

sheet = workbook.sheet_by_index(0)
wb = xlwt.Workbook()
ws = wb.add_sheet('result')

for row in range(0, sheet.nrows):
    test = [i.value for i in sheet.row(row)]
    mean_result = 'Срденее'
    result = 'Среднее из среднего'

    if row > 0:
        array1 = [float(i) for i in test[2:]]
        mean_result = mean(array1)

        array1 = [i for i in array1 if i <= mean_result]
        result = mean(array1)

    for i in range(len(test)):
        ws.write(row, i, test[i])
    ws.write(row, sheet.ncols, mean_result)
    ws.write(row, sheet.ncols + 1, result)

wb.save('example.xlsx')


