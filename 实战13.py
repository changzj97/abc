print('为了您和他人的安全,严禁酒后驾车!')
alcohol=int(input('请输入每100毫升血液的酒精含量:'))
if alcohol>0 and alcohol<20:
    print('你还构不成饮酒行为,可以开车,但是要注意安全')
elif alcohol>=20 and alcohol<80:
           print('已经达到酒后驾驶的标准,请不要开车')
elif alcohol>=80:
    print('已经达到醉酒驾驶的标准,请千万不要开车')

   
