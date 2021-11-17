import random



# 银行的数据库
bank = {     "111222":
                {"leixing":"一类",
                'username': "张三",
               'password':"123456",
               'country': 'cn',
               'province': '河北',
               'street': '桃花街',
               'door': '0011',
               'money': 60000,
               'bank_name': '中国工商银行昌平支行'},
             "222111":
                 {"leixing": "二类",
                  'username': "张三",
                  'password': "123456",
                  'country': 'cn',
                  'province': '河北',
                  'street': '桃花街',
                  'door': '0011',
                  'money': 60000,
                  'bank_name': '中国工商银行昌平支行'}
             }
# 银行名称
bank_name = "中国工商银行昌平支行"

def welcome():
    print("---------------------------------------")
    print("-     中国农业银行账户管理系统V1.0      -")
    print("---------------------------------------")
    print("-  1.开户                             -")
    print("-  2.存钱                             -")
    print("-  3.取钱                             -")
    print("-  4.转账                             -")
    print("-  5.查询                             -")
    print("-  6.Bye!                             -")
    print("--------------------------------------")
# 银行的开户逻辑
def bank_addUser(leixing,account,username,password,country,province,street,door,money):
    if len(bank) > 100:
        return 3

    if account in bank:
        return 2

    # 正常开户
    bank[account] = {
        "leixing":leixing,
        "username":username,
        "password":password,
        "country":country,
        "province":province,
        "street":street,
        "door":door,
        "money":money,
        "bank_name":bank_name
    }
    return 1

# 开户的输入数据
def  addUser():
    leixing = input("请输入账户类型（一类 or 二类）：")
    username = input("请输入姓名：")
    password = input("请输入密码：")
    country = input("请输入国籍：")
    province = input("请输入省份：")
    street = input("请输入街道：")
    door = input("请输入您家门牌号：")
    money = int(input("请输入初始化您的银行卡余额："))
    account = random.randint(10000000,99999999)
    status = bank_addUser(account,leixing,username,password,country,province,street,door,money)

    if status == 3:
        print("对不起，该银行用户已满，请携带证件到其他银行办理！")
    elif status == 2:
        print("您之前已经开过户！禁止重复开户！")
    elif status  == 1:
        print("嘻嘻，开户成功！以下卡户的个人信息：")
        info = '''
            ------------个人信息查询结果-------------
            用户名：%s
            账号：%s
            密码：%s
            地址：
                国籍：%s
                省份：%s
                街道：%s
                门牌号：%s
            余额：%s
            开户行名称：%s
            ---------------------------------------
        '''
        print(info % (username,account,password,country,province,street,door,money,bank_name))
        print(bank)


# 定义取钱逻辑
def out(zhanghao,mima,quchu):
    if zhanghao not in bank:
        return 1
    if mima != bank[zhanghao]["password"]:
        return 2
    if quchu > bank[zhanghao]["money"]:
        return 4
    if bank[zhanghao]["leixing"] == "一类" and quchu <= 50000:
        s = bank[zhanghao]["money"]-quchu
        bank[zhanghao]["money"] = s
        return 3
    elif bank[zhanghao]["leixing"] == "二类" and quchu <= 20000:
        s = bank[zhanghao]["money"] - quchu
        bank[zhanghao]["money"] = s
        return 3
    else:
        print("转账金额过大")

#输入取钱信息
def cash():
    zhanghao = str(input("请输入账号"))
    mima = input("请输入密码")
    quchu = int(input("请输入取出的金额"))
    c=out(zhanghao,mima,quchu)
    if c == 1:
        print("账号不存在")
    elif c == 2:
        print("密码不正确")
    elif c == 4:
        print("账户余额不足")
    elif c == 3:
        print("取钱成功，共取出%s元，剩余%s元"%(quchu,bank[zhanghao]["money"]))
#存钱
def addcash(zhanghao,mima,cunru):
    if zhanghao not in bank:
        return 1
    if mima != bank[zhanghao]["password"]:
        return 2
    s = bank[zhanghao]["money"]+cunru
    bank[zhanghao]["money"] = s
    return 3

#输入存钱信息
def cunqian():
    zhanghao = str(input("请输入账号"))
    mima = input("请输入密码")
    cunru = int(input("请输入存入的金额"))
    c=addcash(zhanghao,mima,cunru)
    if c == 1:
        print("账号不存在")
    elif c == 2:
        print("密码不正确")
    elif c == 3:

        print("账户存钱成功，共存入%s元，剩余%s元" % (cunru, bank[zhanghao]["money"]))

def zhuanzhang():
    zhuanchu=input('请输入转出账号：')
    zhuanru=input("请输入转入账号：")
    password=input("请输入密码：")
    jine=int(input("请输入转账金额："))
    if zhuanru in bank and zhuanchu in bank and password == bank[zhuanchu]["password"]:
        if bank[zhuanchu]["leixing"]=="一类" and jine<50000:
            a = bank[zhuanchu]["money"] - jine
            b = bank[zhuanru]["money"] + jine
            bank[zhuanchu]["money"] = a
            bank[zhuanru]["money"] = b
            print("转账成功，账号%s转出%s元，剩余%s元,账号%s收到转账%s元，剩余%s元" % (zhuanchu, jine, bank[zhuanchu]["money"], zhuanru, jine, bank[zhuanru]["money"]))
        elif bank[zhuanchu]["leixing"]=="二类" and jine<20000:
            a = bank[zhuanchu]["money"]-jine
            b = bank[zhuanru]["money"]+jine
            bank[zhuanchu]["money"]=a
            bank[zhuanru]["money"]=b
            print("转账成功，账号%s转出%s元，剩余%s元,账号%s收到转账%s元，剩余%s元" % (zhuanchu, jine, bank[zhuanchu]["money"], zhuanru, jine, bank[zhuanru]["money"]))
        else:
            print("金额过大")
    if zhuanchu not in bank or zhuanru not in bank:
        print("转出账号或者转入账号不是本银行")
    if password != bank[zhuanchu]["password"]:
        print("密码不正确")



# 银行的查询逻辑
def bank_account(account,password):
    if account not in bank:
        return 3
    else :
        if password != bank[account]["password"]:
            return 2
        else:
            return 1

    # # 正常查询
    # bank[account] = {
    #     "account":account,
    #     "password":password,
    # }
    # return 1


# 查询的输入数据
def query():
    account =  str(input("请输入账号："))
    password = str(input("请输入密码："))
    status = bank_account(account,password)

    if status == 3:
        print("该用户不存在！")
    elif status == 2:
        print("密码错误！")
    elif status  == 1:
        print("查询成功！以下显示卡户的个人信息：")
        print ("个人信息查询结果：%s" % str (bank[account]))
        # print(bank)
#拜拜

while True:
    welcome()
    chose = input("请输入业务编号：")
    if chose == "1":
        addUser()
    elif chose == "2":
        cunqian()
        break
    elif chose == "3":
        cash()
    elif chose == "4":
        zhuanzhang()
    elif chose == "5":
        query()
    elif chose == "6":
        print("baibai")
        break



































































