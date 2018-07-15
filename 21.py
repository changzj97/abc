i=0
while i < 10:
    a =input('查询能量请输入能量来源!退出程序请输0:')
    print('能量来源如下:')
    print('生活缴费，行走捐，共享单车，线下支付，网络购票')
    if a =='0':
        print('已退出')
        break
    elif a == '生活缴费':
        print('300g')
    elif a == '行走捐':
        print('200g')
    elif a == '共享单车':
        print('350g')
    elif a == '线下支付':
        print('380g')
    elif a == '网络购票':
        print('500g')
    
