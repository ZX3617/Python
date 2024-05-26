import random
import string

# 假设一个银行卡号由16位数字组成（这只是一个示例，实际银行卡号长度和规则可能不同）
def kahao():
    return ''.join(random.choices(string.digits, k=16))

# 创建一个空字典来存储银行卡号和密码
b = {}

# 生成1000个模拟的银行卡号，并将它们添加到字典中，密码固定为'000000'
for i in range(1000):
    bank_card = kahao()
    b[bank_card] = '000000'

# 打印部分结果或整个结果
# 打印前10个结果作为示例
for i, (bank_card, password) in enumerate(list(b.items())[:10]):
    print(f"模拟银行卡号{i+1}: {bank_card}, 密码: {password}")

# 如果你需要打印所有结果，可以取消上面的切片操作，并直接打印整个字典
#for bank_card, password in b.items():
#    print(f"模拟银行卡号{i+1}: {bank_card}, 密码: {password}")