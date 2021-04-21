a=input().split()
length=int(a[0])
b=input().split()
for x in range(0,len(a)-1):
  print(a[x],end=' ')
print(a[len(a)-1])
for y in range(0,length-1):
  print(b[y],end=' ')
print(b[length-1])