number=eval(input('请输入您6位的中奖号码'))

if number==987456:
    print('恭喜您中奖了')
if number!=987456:
    print('您未中奖')

print('----------以上if判断的表达式，是通过比较运算符计算出来的，结果是布尔值----------')
n=98
if n%2:
     print(n,'是奇数')
if not n%2:
     print(n,'是偶数')

print('-----------判断一个字符串是否是空字符串----------')
x=input('请输入一个字符串：')
if x:
        print('x是一个非空字符串')

if not x:
        print('x是一个空字符串')
print('--------------表达式也可以是一个单纯的布尔型变量----------')
flag=eval(input('请输入一个布尔类型的值：True或False'))
if flag:
         print('flag的值是True')

if not flag:
         print('flag的值是False')
print('-----------------使用if语句时，如果语句块中只有一句代码，可以将语句块直接写在冒号后面----------')
a=10
b=5
if a>b:max=a
print('a和b的最大值为',max)