for i in range(2,100):
    for a in range(2,i):
        if i%a==0:
            break
        a+=1
    else:
        print(i,end=' ')
    i+=1
print('')
    
