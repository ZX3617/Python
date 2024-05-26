'''
无参数无返回值参数
无参数有返回值参数
有参数无返回值参数
有参数有返回值参数
'''

import random

def cards(c,p) -> int:
    dic=dict(zip(c,p))
    print(dic.keys())
    print(dic.values())
    print(dic.items())
    return 0

card =[''.join(random.choices('0123456789', k=16)) for _ in range(1000)]
password=['000000' for _ in range(1000)]
cards(card,password)
name = input('请输入您的名字:')
print(name)