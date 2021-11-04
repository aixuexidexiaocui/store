import xlrd
data = xlrd.open_workbook('12.xls')
table=data.sheet_by_index(0)
print(data.sheet_names())
print(data)
rows = table.nrows
cols = table.ncols
for i in range(rows):
    for j in range(cols):
        print(table.cell_value(i,j),end='\t')
    print()