import random
import string

def kahao():
    return ''.join(random.choices(string.digits, k=16))

mima={}

for i in range(1000):
    bank_card = kahao()
    mima[bank_card] = '000000'

for i,(bank_card, password) in enumerate(list(mima.items())):
    print(f"模拟银行卡号{i+1}: {bank_card}, 密码: {password}")