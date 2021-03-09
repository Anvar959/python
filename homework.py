

def ng():
    for i in range(10):
        yield i

print(type(ng()))

n1 = ng()
next(n1)
print(next(n1))
next(n1)
print(next(n1))
next(n1)
print(next(n1))
next(n1)
print(next(n1))
next(n1)
print(next(n1))