import xlwt
import xlrd
from statistics import mean

file_to_download = 'test.xlsx'
file_to_upload = 'example.xlsx'
name_of_sheet = 'result'


if __name__ == '__main__':

    workbook = xlrd.open_workbook(file_to_download) #Вычитываем файл
    sheet = workbook.sheet_by_index(0) #Получаем первую страницу таблицы
    wb = xlwt.Workbook()#Создаем воркбук для записи таблицы
    ws = wb.add_sheet(name_of_sheet)#создаем страницу для записи результата

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

    wb.save(file_to_upload)
    print(f'File {file_to_upload} was created')

