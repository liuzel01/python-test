
import xlwings as xw

work_book = xw.Book('测试.xlsx')

sheet1 = work_book.sheets[0]

print(sheet1.book)

last_cell = sheet1.used_range.last_cell 
last_row = last_cell.row
last_col = last_cell.column

c = 0

for cell in sheet1.range((1,1),(last_row, last_col)):
    c += 1
    print(cell.value, end ='\t')
    if c % last_col  == 0:
        print("")
