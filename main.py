
x = int(input())
y = int(input())
c1 = x+y
c2 = x-y
c3 = x*y
c4 = x/y
c5 = x//y
if x>0 and y>0:
    if c1>c3:
        print(c3)
    else:
        print(c1)
elif x==-1 and y==-1:
    print(0)
elif x<0 and y<0:
    if  c4>c2:
        print(c4)
    else:
        print(c2)

elif x<0 and y>0:
    print(c4)
elif x>0 and y<0:
    if c1>c4:
        print(c1)
    else:
        print(c4)
