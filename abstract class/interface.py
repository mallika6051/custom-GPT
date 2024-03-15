from abc import ABC, abstractmethod

class MyInterface(ABC):
    @abstractmethod
    def interface_method(self):
        pass
    @abstractmethod
    def show(self):
        pass

class MyClass(MyInterface):
    def interface_method(self):
        print("This is the implementation of the interface method.")
class my(MyClass):
    def show(self):
        print("This is mallika")

instance = my()
instance.interface_method()  # Output: "This is the implementation of the interface method."
instance.show()
