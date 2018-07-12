number='123'
passwd='456'
money=500
number1=input('请输入账号')
passwd1=input('请输入密码')
if number1==number and passwd1==passwd:
    print('输入取款金额')
    money1=int(input())
    if money1>money:
        print('余额不足')
    elif money1<=money:
        print('取款%d,还剩%d'%(money1,money-money1))
else:
    print('非法账户')


