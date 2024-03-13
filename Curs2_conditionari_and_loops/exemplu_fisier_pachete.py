def suma_ex(a, b=0, *args):
    initial = a + b
    total = 0
    for elem in args:
        total = total + elem
    return initial + total

var = 10
