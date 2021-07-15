import xlwings as xw

work_book = xw.Book('测试.xlsx')

sheet1 = work_book.sheets[0]

print(sheet1.book)

#last_cell = sheet1.used_range.last_cell 
last_row = 4
last_col = 5

## 获取分数的列索引
score_col_index = ""

for cell in sheet1.range((1,1),(1,last_col)):
    if cell.value == '分数':
        score_col_index = cell.column

## 将分数存入列表
score_list = []

for row in range(2,last_row+1):
    cell = sheet1.range((row,score_col_index))
    score_list.append(cell.value)

print(score_list)
sum_score = sum(score_list)
avg_score = sum(score_list) / len(score_list)

## 计算出结果后写入 excel

sheet1.range((last_row + 1,1)).value = "合计"
sheet1.range((last_row + 1,last_col)).value = sum_score


sheet1.range((last_row + 2,1)).value = "平均值"
sheet1.range((last_row + 2,last_col)).value = round(avg_score,2)

work_book.save()
work_book.close()
