#1.有四个数字:1,2,3,4，能组成多少个互不相同且无重复数字的三位数？各是多少？
print('第1题')
n=0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i != k) and (i!=j) and (j!=k):
                print(i,j,k)
                n+=1
print(n)


#2.企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，
# 从键盘输入当月利润I，求应发放奖金总数？
print('第2题')
arr=[1000000,600000,400000,200000,100000,0]
rat=[0.01,0.015,0.03,0.05,0.075,0.1]
while(1):
    i=int(input('请输入当月利润：'))
    if i==0:
        break
    result=0
    for idx in range(0,6):
        if i>arr[idx]:
            result+=(i-arr[idx])*rat[idx]
            i=arr[idx]
    print(result)
    break

#3.输入三个整数x,y,z，请把这三个数由小到大输出
print('第3题')
numlist=[]
for i in range(3):
    x=int(input('依次回车输入：'))
    numlist.append(x)
numlist.sort()

for j in range(0,3):
    print(numlist[j])
    j+=1


#4.将一个列表的数据复制到另一个列表中
print('第4题')
a=['a','s','d']
b=a[:]
print(b)

#5.暂停一秒输出,并格式化当前时间。使用 time 模块的 sleep() 函数。
print('第5题')
import time
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
time.sleep(1)
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
time.sleep(3)
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

#6.打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
print('第6题')
for x in range(1,10):
    for y in range(0,10):
        for z in range(0,10):
            s1=x*100+y*10+z
            s2=pow(x,3)+pow(y,3)+pow(z,3)
            if s1==s2:
                print(s1)

#7.输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
print('第7题')
s=input('input:')
letters=0
space=0
digit=0
others=0
for c in s:
    if c.isalpha():
        letters+=1
    elif c.isspace():
        space+=1
    elif c.isdigit():
        digit+=1
    else:
        others+=1
print('字母：%d 空格：%d  数字：%d  其它：%d'%(letters,space,digit,others))



#8.一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
print('第8题')
h=100
time=10
height=[]
for i in range(2,time+1):
    h/=2
    height.append(h)
print(min(height)/2)
print(sum(height)*2+100)


