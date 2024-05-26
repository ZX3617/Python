def wd(name,tiwen,gl):
    #name=input('请输入您的姓名')
    #tiwen=float(input('请输入您的体温'))
    if tiwen<37.5:
        print(f'{name}的体温小于37.5，属于正常体温')
    else:
        #gl=input('请输入您的隔离方式')
        print(f'{name}的体温大于37.5，需要隔离，隔离方式为{gl}')
wd('zx',38,gl='居家隔离')