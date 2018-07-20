def money(num):
    dol=6.28
    rmb = num*dol
    return('折合人民币:%.2f'%rmb)
a=money(float((input('输入美元金额:'))))
print(a)
