def decorator(F):
    def newFunc(a, b):
        print "input ", a, b
        return F(a, b)
    return newFunc

@decorator
def square_sum(a, b):
    return (a ** 2 + b ** 2) ** 0.5

@decorator
def square_diff(a, b):
    return (a ** 2 - b ** 2) ** 0.5

print(square_sum(3, 4))
print(square_diff(5, 3))


