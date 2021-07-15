import xlwings as xw
import pandas as pd

wb = xw.Book('300369.xlsx')

sheet1 = wb.sheets[0]
print(sheet1.range('A1:D3').value)

data_frame = sheet1.range('A1:D354').options(pd.DataFrame).value
data_frame.drop(columns = ["股票代码","名称"],inplace = True)
print(data_frame.head())

ax = data_frame.plot()
fig = ax.get_figure()
sheet1.pictures.add(fig, name = '绿盟科技', update = True)
wb.save()
