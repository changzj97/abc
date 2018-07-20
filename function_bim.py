def function_bim(name,height,weight):
    BMI = weight/height**2
    if BMI < 18.5:
        print('%s的身高:%.2f米\t\t体重:%d千克\n%s的BMI指数为:%.2f\n您的体重过轻了'%(name,height,weight,name,BMI))
    elif BMI<24.9 and BMI >18.5:
        print('%s的身高:%.2f米\t\t体重:%d千克\n%s的BMI指数为:%.2f\n正常范围,注意保持'%(name,height,weight,name,BMI))
    elif BMI <29.9 and BMI > 24.9:
        print('%s的身高:%.2f米\t\t体重:%d千克\n%s的BMI指数为:%.2f\n您的体重过重'%(name,height,weight,name,BMI))
    elif BMI >29.9:
        print('%s的身高:%.2f米\t\t体重:%d千克\n%s的BMI指数为:%.2f\n您的体重肥胖'%(name,height,weight,name,BMI))
function_bim('路人甲',1.83,60)
print('') 
function_bim('路人乙',1.6,50)      
    
