class Comparator:
    value = 0

    def compare(self, v):
        if hasattr(v, 'value'):
            return  int(self.value) - int(v.value)
        else:
            return 1

class Test:
    pass

C = Comparator()
C.value = 123
T = Test()
T.value = 126
print(C.compare(T))
