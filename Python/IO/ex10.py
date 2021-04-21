a =input()
if a.isalpha():
    for x in a:
        if x != a[len(a)-1]:
            print(x,end='')
            print(',',end='')
    print(a[len(a)-1])
else:
    print('Invalid input pls enter a string')