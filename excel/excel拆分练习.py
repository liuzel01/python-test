import xlwings as xw

work_book = xw.Book('excel拆分练习.xlsx')

sheet1 = work_book.sheets[0]

print(sheet1.book)

last_cell = sheet1.used_range.last_cell
last_row = last_cell.row
last_col = last_cell.column


"""
定义缓存
"""
head_titles = []
rows_content = []
for i in range(last_row - 1):
    rows_content.append([])

"""
读取 excel 内容至缓存
"""
for cell in sheet1.range((1,1),(1, last_col)):
    head_titles.append(cell.value)

col_index = 0
row_index = 0
for cell in sheet1.range((2,1),(last_row, last_col)):
    rows_content[row_index].append(cell.value)
    col_index += 1
    if col_index % last_col == 0:
        row_index += 1
        col_index = 0

"""
将缓存写入 excel
"""

# 遍历 rows_content

for index, row in enumerate(rows_content):
    work_book = xw.Book()
    sheet1 = work_book.sheets[0]
    for col_index, col in enumerate(row):
        sheet1.range((1,col_index + 1)).value = head_titles[col_index]
        sheet1.range((2,col_index + 1)).value = col
    work_book.save(f'{row[0]}.xlsx')
    work_book.close()






