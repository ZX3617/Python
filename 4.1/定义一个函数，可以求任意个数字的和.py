def sum(*nums):
    #定义一个变量，来保存结果
    result = 0
    #遍历元组，并将元组中的数进行累加
    for n in nums:
        result +=n
    print(result)

sum(123,456,789,10,20,30,40)
sum(10,20,30)
sum(12,78,90,67)