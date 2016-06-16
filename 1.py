class python:
    conjugate=1
    denominator=2
    imag=0
    numerator=10
    bit_length=None
    real=None
    _ABC=None
for i in dir(python):
    if not i.startswith('_'):
        print(i)
