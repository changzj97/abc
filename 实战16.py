print('请您输入名字:')
name=input()
print('1,水瓶座 1.20~2.18')
print('2,双鱼座 2.19~3.20')
print('3,白羊座 3.21~4.19')
print('4,金牛座 4.20~5.20')
print('5,双子座 5.21~6.21')
print('6,巨蟹座 6.21~7.22')
print('7,狮子座 7.23~8.22')
print('8,处女座 8.23~9.22')
number=int(input('输入数字'))
if number==1:
    print(name)
    print('日期是 1.20~2.18')
    print('性格是 活泼')   
elif number==2:
    print(name)
    print('日期是 2.19~3.20')
    print('性格是 开朗')
elif number==3:
    print(name)
    print('日期是 3.21~4.19')
    print('性格是 阳光:')
elif number==4:
    print(name)
    print('日期是 4.20~5.20')
    print('性格是 随和')
elif number==5:
    print(name)
    print('日期是 5.21~6.21')
    print('性格是 活泼')
elif number==6:
    print(name)
    print('日期是 6.21~7.22')
    print('性格是 开朗')
elif number==7:
    print(name)
    print('日期是 7.23~8.22')
    print('性格是 阳光')
elif number==8:
    print(name)
    print('日期是 8.23~9.22')
    print('性格是 随和')
else:
    print('无法查询')
