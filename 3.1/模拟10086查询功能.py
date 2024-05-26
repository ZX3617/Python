def yue():
    print("当前余额为：100")
def liuliang():
    print("当前剩余流量为：10G")
def shijian():
    print("当前剩余通话为：100分钟")
while True:
    num = input("------------10086查询项目-------------------\n1.显示当前余额\n2.显示当前流量\n3.显示剩余通话\n0.退出自助服务")
    if num == "1":
        yue()
    elif num == "2":
        liuliang()
    elif num == "3":
        shijian()
    elif num == "0":
        break
    else:
        print("输入错误，请重新输入！")