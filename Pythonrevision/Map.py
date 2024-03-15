def func(x):
    return x+2
List=[10,20,30,40,50]
print(list(map(func, List)))

print(list(map(lambda x: x*2, List)))
