vvod=input()
l=list()
z=list(vvod)
u=''
z.append(',')
for i in z:
    if i==',':
        l.append(int(u))
        u=''
    else:
        u=u+i
m=l[0]
n=l[1]
print('',m,'=',1,'*',m)
if n!=0:
    if n<9:
        for a in range(2,n+1):
            if n<9:
                print(m*(a),'=',a,'*',m)
    elif n<99:
        for a in range(2,n+1):
            print(m*(a),'=',a,'*',m)
