
class Dot:
    x = []
    str = ""

    def changepoint(self, p):
        self.str = p
        self.x = p.split(",")

    def strpoint(self):
        return self.str

    def distance(self, point ):
        i=0
        if len(self.x) == len(point.x):
            dl = 0
            while i!=len(point.x):
                if int(self.x[i]) >  int(point.x[i]) >= 0:
                    dl += pow((int(self.x[i]) - int(point.x[i])), 2)

                elif int(self.x[i]) > 0 > int(point.x[i]):
                    dl += pow((int(self.x[i]) + int(point.x[i])), 2)

                elif int(self.x[i]) < 0 < int(point.x[i]):
                    dl += pow((int(point.x[i]) + int(self.x[i])), 2)

                elif 0 <= int(self.x[i]) < int(point.x[i]):
                    dl += pow((int(point.x[i]) - int(self.x[i])), 2)
                i+=1
            dl = pow(dl, 0.5)
            return dl
        else:
            print("Разная размерность")

    def middle(self, point ):
        i = 0
        if len(self.x) == len(point.x):
            a = []
            while i!=len(point.x):
                if int(self.x[i])>=int(point.x[i]) and int(self.x[i])>=0 and int(point.x[i])>=0:
                    a.append((int(self.x[i]) - int(point.x[i])) / 2)
                elif int(self.x[i])>int(point.x[i]) and int(self.x[i]) > 0 > int(point.x[i]):
                    a.append((int(self.x[i]) + int(point.x[i])) / 2)
                elif int(self.x[i]) < int(point.x[i]) and int(self.x[i]) < 0 < int(point.x[i]):
                    a.append((int(point.x[i]) + int(self.x[i])) / 2)
                else:
                    a.append(( int(point.x[i]) - int(self.x[i])) / 2)
                i+=1
            return a
        else:
            print("Разная размерность")


p1 = Dot()
p1.changepoint(input())
p2 = Dot()
p2.changepoint(input())
print("point1:", p1.strpoint(), "point2:", p2.strpoint())
print(p1.distance(p2))
print(p1.middle(p2))
