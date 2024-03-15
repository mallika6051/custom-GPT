class person:
    def __init__(self,x):
        self.x = x
    def __add__(self, add):
        return self.x + add.x
object1 = person("Mallika")
object2 = person(" Meena")
print(object1+object2)
object3 = person(21)
object4 = person(22)
print(object3+object4)
