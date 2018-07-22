print('定制自己的手机套餐:')
a = {1:'0分钟',2:'50分钟',3:'100分钟',4:'300分钟',5:'不限量'}
b = {1:'0M',2:'500M',3:'1G',4:'5G',5:'不限量'}
c = {1:'0条',2:'50条',3:'100条'}
print('A.请设置通话时长:')
for k,v in a.items():
    print(k,v)
a1 = int(input('输入选择的通话时间编号:'))
print('')
print('B.请设置流量:')
for k1,v1 in b.items():
    print(k1,v1)
b1 =int(input('输入选择流量编号:'))
print('')
print('C.请设置短信条数:')
for k2,v2 in c.items():
    print(k2,v2)
c1 =int(input('输入选择的短信条数编号:'))
print('')
print('您的手机套餐定制成功:免费通话时长为%s/月,流量为%s/月,短信条数%s/月'%(a[a1],b[b1],c[c1]))
