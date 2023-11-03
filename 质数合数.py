d=input("六班最帅？：")
if d!='朱道言':
    print("密码错误。")
else :
    print("密码正确。")
    while 1>0:
        a=float(input("请输入正整数a="))
        if a%1!=0:
            print("看不看得懂人话？")
        b=a
        c=a
        if a==1:
            print("有没有点数学头脑？")
        if a==2:
            print("是个质数")
        while 2<b and b<a+1:
            b=a-1
            if c%b==0:
                print("是个合数")
                break
            b=b-1
            if b==1:
                print("是个质数")
            b=b+1
            a=a-1

