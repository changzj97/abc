age =int(input('输入年龄:'))
subject =input('输入专业:')
college =input('输入是否重点大学:')
if age > 25 and subject == '电子信息工程':
    print('您被录取了')
elif subject == '电子信息工程' and college == '是':
    print('您被录取了')
elif age < 28 and subject == '计算机':
    print('您被录取了')
else:
    print('抱歉,您未达到面试要求')
