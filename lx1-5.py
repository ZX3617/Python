# 直接使用[]
lst=['hello','world',98,100.5]
print(lst)

# 可以使用内在函数list()创建列表
list2=list("helloworld")
list3=list(range(1,10,2)) # 从1开始到10结束，步长为2，不包含10
print(list2)
print(list3)

# 列表是序列中的一种，对序列的操作符、运算符，函数均可使用
print("list+list2+list3") #序列中的相加减
print("list*3") #序列的相乘操作
print(len("list"))
print(max("list"))
print(min("list"))

print(list2.count("o"))
print(list2.index("o"))

# 列表的删除操作
list4=list("10,20,30")
print(list4)
# 删除列表
del list4
print(list4) # name 'list4' is not defined. Did you mean: 'list'?