def qwe(w, st):
    f = 0
    g = 0
    q = 0
    f = 0
    while q != len(st):
        if st[q].find(manual[w]) == 0:
            a = st[q]
            a = a.split(" ")
            a.pop(0)
            for it in range(len(a)):
                if f == 0:
                    while g != len(st):
                        print(st[g],"--", a[it])
                        if st[g] == a[it]:
                            #print("+")
                            f = 1
                            #str.remove(str[g])
                            break
                        g += 1
                else:
                    break
        q += 1

    print("func")
    return f

# --------------------------------------

str = ""
s = " "
while s != "":
    s = input()
    str += s + '/br'
str = str.split("/br")
for i in range(str.count("")):
    str.remove("")
print("str=", str)
manual = str[0].split(" ")
print("manual=", manual)
manual.pop(0)
print(str)
flag = 1

for i in range(len(manual)):
    if flag == 1:
        for j in range(len(str)):
            if str[j] == manual[i]:
                flag = 1
                ln = len(str)
                #str.remove(str[j])
                print("+")
                break
            else:
                print(i)
                ln = len(str)
                flag = qwe(i, str)


if flag == 1:
    print("yes")
else:
    print("no")
