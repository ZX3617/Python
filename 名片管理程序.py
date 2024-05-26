cards = []
def add_mp():
    name = input('请输入您的名字')
    age = input('请输入您的年龄')
    zw = input('请输入您的职位')
    card = {
        'name':name,
        'age':age,
        'zw':zw
    }
    cards.append(card)
    print('名片已添加成功')
def no_mp():
    if not cards:
        print('没有名片可以添加')
    else:
        for idx, card in enumerate(cards,start=1):
            print(f'名片{idx}:')
            print(f'姓名:{card["name"]}')
            print(f'年龄:{card["age"]}')
            print(f'职位:{card["zw"]}')
            print()
def main():
    while True:
        print('\n名片系统菜单:')
        print("1. 添加名片")
        print("2. 查看所有名片")
        print("3. 退出")
        cz = input('请选择您的操作(1-3):')
        if cz == '1':
            add_mp()
        elif cz == '2':
            no_mp()
        elif cz == '3':
            print('感谢使用名片系统！')
            break
        else:
            print('无效的操作')

main()