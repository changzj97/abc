num =int(input('请输入一个数字:'))
while True:
    if num == 0:
        continue
    elif num < 100:
        print('命运给予我们的不是失望之酒，而是机会之杯\n'*num)
        num =int(input('请输入一个数字:'))
        continue
    elif num == 100:
        break
