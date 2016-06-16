a='5,3,6,1,1,2,3,4,7,5,5,7,1,1,4,6,3,4,7,4,2'
step=int('4')
l=list()
costs=list(a)
u=''
costs.append(',')
for i in costs:
    if i==',':
        l.append(int(u))
        u=''
    else:
        u=u+i
costs=len(l)-1
weight=0
while costs>=step:
    min=int('1000')
    for i in range(step):
        if min>=l[costs-i]:
            min=l[costs-i]
            num=costs-i
            print(num,min)
    costs=num-1
    weight=weight+min
    
print('Минимальная стоимость пути:',weight)
