import xlrd
import pymysql
wb = xlrd.open_workbook(filename=r"E:\pythonProject\课程\day-9\百度合作单位-人员管理-二期.xls")
st = wb.sheet_by_index(0)
rows = st.nrows
cols = st.ncols
a = 0#手机号
b = 0
c = 0
d = 0#年龄
e = 0#男女
f = 0
g = 0#工资
h = 0
i = 0#公司
k = 0# 疫情地区

for j in range(1,rows):
    data = st.row_values(j)
    if data[5] .startswith('14' or '17'):
        a += 1
    elif data[5].startswith('13'):
        b += 1
    elif data[5].startswith('15'):
        c += 1
    if data[8] == "男":
        d += 1
    elif data[8] =='女' :
        e += 1
    if data[7] > 45 :
        f += 1
    if data[11] > 8000:
        g += 1
    elif data[11] < 3000:
        h += 1
    if data[13] .endswith('传媒有限公司'):
        i += 1
    if data[9] .startswith('黑龙江'or'北京'or'福建'or'四川'):
        k += 1

print("a、表格的总人数为：%s人" %len(rows))
print('b、使用电信：%s人 ,使用移动:%s人 ,使用联通：%s人' %(a,b,c))
print("c、男生人数为：%s人 ,女生人数为:%s人" %(d,e))
print('d、45岁以上的人数为：%s人' %f)
print('e、工资8000以上的人数为：%s人 ,工资3000以下的人数为：%s人' %(g,h))
print('f、去传媒有限公司的人数为:%s人'%i)
print('g、高危地区的人数为：%s人'%k)

con = pymysql.connect(host="localhost",user="root",password="",database="baidu")
cusor = con.cursor()
for a in range(1,rows):
    for b in range(cols):
        date = wb.cell_value(a,b)
        sql = "insert into userinfor value(%s)"
        param = [date]
        cusor.execute(sql, param)
        con.commit()
cusor.close()
con.close()