class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
x='1,2,7,14,8,8,18,28'
l=list()
z=list(x)
u=''
z.append(',')
for i in z:
    if i==',':
        l.append(u)
        u=''
    else:
        u=u+i

print(l)
a=list()
i=0
while i <int(len(l)):
    a.append(point(l[i],l[i+1]))
    i=i+2
for i in a:
    print(i.x,i.y)

pp=(float(a[0].y)-float(a[1].y))/(float(a[0].x)-float(a[1].x))
pp1=(float(a[2].y)-float(a[3].y))/(float(a[2].x)-float(a[3].x))
if pp==pp1:
    print('yes')
else:
    print('no')
