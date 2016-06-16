l=[i*i for i in range(10)]
print(l)
maxl=max(l)
for i in l[:]:
    if i==maxl:
        l.remove(i)
print(max(l))
