x=eval(input('请输入一个年份'))
if (x%4==0 and x%100!=0) or x%400==0:
    print('今年是闰年')
else:
    print('今年是平年')