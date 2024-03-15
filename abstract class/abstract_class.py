from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def Start(self):
       pass
class Car(Vehicle):
    def Start(self):
        print("Start the car")
obj=Car()
# obj1=Vehicle()
# obj1.Start()
obj.Start()
