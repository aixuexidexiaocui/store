import openpyxl
workbook=openpyxl.load_workbook('1a.xlsx')
sheet=workbook.get_sheet_by_name('Sheet1')
row=[item.value for item in list(sheet.rows)[0]]
print(row)