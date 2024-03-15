from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Starting the car!")
    def stop(self):
        print("Stopping the car!")
class Motorcycle(Vehicle):
    def start(self):
        print("Starting the motorcycle!")
    def stop(self):
        print("Stopping the motorcycle!")
car = Car()
motorcycle = Motorcycle()
car.start()
motorcycle.start()
car.stop()
motorcycle.stop()

