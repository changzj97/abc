def czj():
    czj_str = input('请输入内容:')
    if czj_str.isalnum() and czj_str.islower():
        if czj_str.isalpha()==False:
            print('由小写字母和数字构成')
        else:
            print('不是小写字母和数字构成')
    else:
        print('不是小写字母和数字构成')
czj()
