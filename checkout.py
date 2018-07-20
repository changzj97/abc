def fun_checkout():
    print('开始计算:-->')
    czj = []
    while True:
        money = float(input('输入商品金额(输入0表示输入完毕)'))
        czj.append(money)
        if money == 0:
            break
    money1 = 0
    money2 = 0
    for i in czj:
        money1 += i
    if money1 >= 500 and money1 <= 1000:
        money2 = money1 * 0.9
    elif money1 >= 1000 and money1 <= 2000:
        money2 = money1 * 0.8
    elif money1 >= 2000 and money1 <= 3000:
        money2 = money1 * 0.7
    elif money1 >= 3000:
        money2 = money1 * 0.6
    print('合计金额:%d应付金额:%d'%(money1,money2))
fun_checkout()
