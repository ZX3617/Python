lst=['hello','world','python']
print('原列表:',lst,id(lst))
# 增加元素的操作
lst.append('sql')
print('增加元素之后：',lst,id(lst))
print('-'*40)
lst.insert(1,100)
print(lst)
print('-'*40)
# 列表元素的删除操作
lst.remove('world')
print('删除元素之后的列表',lst,id(lst))
print('-'*40)
# 使用pop(index)根据索引将元素取出，然后再删除
print(lst.pop(1))
print(lst)
print('-'*40)
# 清楚列表中所有的元素clear()
# lst.clear()
# print(lst,id(lst))

# 列表的方向
lst.reverse() # 不会产生新的列表，再原列表的基础上进行的
print(lst)
print('-'*40)
# 根据元素的修改操作
# 根据索引进行修改元素
lst[1]='mysql'
print(lst)