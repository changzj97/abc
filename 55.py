c_str=input('请输入一个字符串:')
a_dict = {}
for i in c_str.lower():
    if i in a_dict.keys():
        a_dict[i]+=1
    else:
        a_dict[i]=1
print(a_dict)
