a =int(input('请输入月份(例如:5):'))
b =int(input('请输入日期(例如:17):'))
if a == 1 and b in range(20,32) or a == 2 and b in range(1,19):
    print('%d月%d日星座为:水瓶座'%(a,b))
elif a == 2 and b in range(19,32) or a == 3 and b in range(1,21):
    print('%d月%d日星座为:双鱼座'%(a,b)) 
elif a == 3 and b in range(21,32) or a == 4 and b in range(1,20):
    print('%d月%d日星座为:白羊座'%(a,b))
elif a == 4 and b in range(20,32) or a == 5 and b in range(1,21):
    print('%d月%d日星座为:金牛座'%(a,b))
elif a == 5 and b in range(21,32) or a == 6 and b in range(1,22):
    print('%d月%d日星座为:双子座'%(a,b))
elif a == 6 and b in range(22,32) or a == 7 and b in range(1,23):
    print('%d月%d日星座为:巨蟹座'%(a,b))
elif a == 7 and b in range(23,32) or a == 8 and b in range(1,23):
    print('%d月%d日星座为:狮子座'%(a,b))
elif a == 8 and b in range(23,32) or a == 9 and b in range(1,23):
    print('%d月%d日星座为:处女座'%(a,b))
elif a == 9 and b in range(23,32) or a == 10 and b in range(1,24):
    print('%d月%d日星座为:天秤座'%(a,b))
elif a == 10 and b in range(24,32) or a== 11 and b in range(1,23):
    print('%d月%d日星座为:天蝎座'%(a,b))
elif a == 11 and b in range(23,32) or a == 12 and b in range(1,22):
    print('%d月%d日星座为:射手座'%(a,b))
elif a == 12 and b in range(22,32) or a == 1 and b in range(1,20):
    print('%d月%d日星座为:摩羯座'%(a,b))
else:
    print('输入有误')
