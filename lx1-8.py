lst=[4,56,3,78,40,56,89]
print('原列表:',lst)

# 排序。默认是升序
lst.sort() # 排序是在原列表的基础上进行的，不会产生新的列表对象
print('升序:',lst)

# 排序，降序
lst.sort(reverse=True)
print('降序:',lst)
print("-"*50)
lst2=['banana','apple','Cat','orange']
print('原列表：',lst2)
# 升序排序，先拍大写，在拍小写
lst2.sort()
print('升序：',lst2)

# 降序，先拍小写，后排大写
lst2.sort(reverse=True)
print('降序：',lst2)
print("-"*50)
# 忽略大小写排序
lst2.sort(key=str.lower)
print(lst2)
print("-"*50)
lst2=['banana','apple','Cat','orange']
print('原列表：',lst2)
print("-"*50)
new_lst2=sorted(lst2,key=str.lower)
print('原列表:',lst2)
print('排序后的新列表',new_lst2)