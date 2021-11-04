import random
a=random.randint(0,150)
#print(a)
i=1
n=5000
m=500
x=3000
print("初始金币",n)
#game()
for i in range(20):
    b = int(input('请输入数字：'))
    if b>a:
        print("输入的大了哦")
        n=n-m
        print("现有金币",n)
    elif b<a:
        print("输这么小干嘛")
        n=n-m
        print("现有金币",n)
    else:
        print("很幸运猜对了")
        n=n+x
        print("现有金币",n)
        break
    if n<0:
        break
