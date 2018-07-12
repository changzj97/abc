print('欢迎使用10086自助查询系统')
print('输入1,查询您当前余额')
print('输入2,查询您当前剩余流量')
print('输入3,查询您当前剩余通话分钟数')
number=int(input('请输入:'))
if number==1:
    print('您当前剩余余额为%d元'%(number * 13))
elif number==2:
    print('您当前剩余流量为%dG'%number**2)
elif number==3:
    print('您当前的剩余通话为%d分钟'%number**4)
