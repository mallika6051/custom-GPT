# # multiple inheritance
#
# class animals:
#     def animal(self):
#         return "The animals are lived in forest"
# class DomesticAnimals:
#     def DomesticAnimal(self):
#         return "Dog", "Cat"
# class wildAnimals(animals, DomesticAnimals):
#     def WildAnimal(self):
#         return "Lion, Tiger"
# Allanimals=wildAnimals()
# print(Allanimals.animal(), Allanimals.WildAnimal())


# multilevel inheritance

# class parent:
#     def fun1(self):
#         print("This is parent class")
# class child(parent):
#     def fun2(self):
#         print("This is child class")
# class grantchild(child):
#     def fun3(self):
#         print("This is grantchild class")
# result=grantchild()
# result.fun1()
# result.fun2()
# result.fun3()
#
# # Hierarchical inheritance
class person:
    def fun1(self):
        print("Mallika")
class Mallika(person):
    def fun2(self):
        print("She is an employee in sightspectrum")
class Malli(person):
    def fun3(self):
        print("She lived in Tambaram")
result1=Mallika()
result2=Malli()
result1.fun1()
result1.fun2()
result2.fun1()
result2.fun3()

#
# # hybrid inheritance
# class parent:
#     def fun1(self):
#         print("This is parent class")
# class child1(parent):
#     def fun2(self):
#         print("This is child class")
# class child2(parent):
#     def fun3(self):
#         print("This is grandchild class")
# class all(child1, child2):
#     def fun4(self):
#         print("This is for all the classes")
# obj=all()
# obj.fun1()
# obj.fun2()
# obj.fun4()
