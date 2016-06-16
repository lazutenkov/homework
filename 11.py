m = input().split(" ")
print("Числа")
print(m)
# ================================
print("Последовательность знаков")
a = []

for i in range(len(m) - 2):
    a.append('-')
    m[i] = int(m[i])

for i in range(pow(2, len(m))):
    print(a)
    # ----------------------------------------
    # вычисления
    s = int(m[0])
    for j in range(len(a)):
        if a[j] == '-':
            s -= int(m[j + 1])
            # print("sum=",s)
        else:
            s += int(m[j + 1])
            # print("sum=",s)
    # print(m[len(m)-1])
    print("результат=", s)
    if int(s) == int(m[len(m) - 1]):
        flag = 1
        break
    else:
        flag = 0
    # перебор знаков
    if len(a) != 1:
        if a[0] == '+':
            a[0] = '-'
            j = 1
            fl = 0
            while j != len(m):
                if a[0 + j] == "+":
                    a[0 + j] = '-'
                    fl = 1
                elif a[0 + j] == '-' and fl == 1:
                    a[0 + j] = "+"
                    fl = 0
                    break
                elif a[0 + j] == '-' and fl == 0:
                    a[0 + j] = "+"
                    break
                j += 1
        else:
            a[0] = "+"
    else:
        if a[0] == '-':
            a[0] = '+'
        else:
            a[0] = "-"
            break

if flag == 1:
    print("YES")
else:
    print("NO")
