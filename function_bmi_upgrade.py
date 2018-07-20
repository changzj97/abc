def function_bmi_upgrade(name,height,weight):
    BMI=weight/height**2
    if BMI < 18.5:
        a = '体重过轻'
    elif BMI <24.9 and BMI > 18.5:
        a = '体重正常'
    elif BMI < 29.9 and BMI > 24.9:
        a = '体重过重'
    elif BMI > 29.9:
        a = '体重肥胖'
    print('==========%s=========='%name)
    print('身高:%.2f米\t\t体重:%.2fkg'%(height,weight))
    print('BMI指数为:%f\n您的%s'%(BMI,a))
    print('')
name_list = [{'name1':'绮梦','height1':1.7,'weight1':65},{'name1':'零语','height1':1.78,'weight1':50},{'name1':'黛兰','height1':1.72,'weight1':66},{'name1':'紫轩','height1':1.8,'weight1':75},{'name1':'冷伊一','height1':1.75,'weight1':70}]

name_dict={}
for name_dict in name_list:
 function_bmi_upgrade(name_dict['name1'],name_dict['height1'],name_dict['weight1'])
