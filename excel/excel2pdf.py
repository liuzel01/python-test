import xlwings as xw

wb = xw.Book('300369.xlsx')
sheet1 = wb.sheets[0]
sheet1.to_pdf(path= '300369.pdf')