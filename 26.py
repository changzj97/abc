num = 100
while num <= 999:
    a = num//100
    b = (num-a*100)//10
    c = num -(a*100+b*10)
    if num == a**3+b**3+c**3:
        print(num)
    num +=1    
