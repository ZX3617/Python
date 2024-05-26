lst=['hello','world','python','php']
# 使用便利循环for编列列表元素
for item in lst:
    print(item)
print('-'*40)
# 使用for循环，range()函数，len()函数，根据索引进行编列
for i in range(0,len(lst)):
    print(i,'--->',lst[i])
print('-'*40)
# 第三种便利方式 enumearte()函数
for index,item in enumerate(lst):
    print(index,item) #index是序号，不是索引
print('-'*40)
#手动修改序列号的起始值
for index,item in enumerate(lst,start=1):
    print(index,item)
print('-'*40)
for index,item in enumerate(lst,1): #   省略start不写，直接写起始值
    print(index, item)