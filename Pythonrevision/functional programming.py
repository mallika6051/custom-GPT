def add(x):
    return x+10
def twice(func, arg):
    return func(func(arg))
print(twice(add,10))
