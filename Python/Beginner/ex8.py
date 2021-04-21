n=int(input())
if n<8 and n>0:
    if n%2==0:
        if n!=2:
            print(30)
        else:
            print(28)
    else:
        print(31)
elif n>=8 and n<=12:
    if n%2==0:
        print(31)
    else:
        print(30)
else:
    print('Error')
