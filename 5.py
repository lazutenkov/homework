text='abc abc dddf fdr'
a=text.split(' ')
print(a)
count=0
i='---'
for i in a:
    if a.count(i)>count:
        count=a.count(i)
        p=i
    elif (i!=p) and (a.count(i)==count):
        p='---'
print(p)
print('кол-во повторов:',count)
