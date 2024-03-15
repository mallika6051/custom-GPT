class MyClass:
    def __init__(self):
        self.public_attribute = "I'm public"
        self._protected_attribute = "I'm protected"
        self.__private_attribute = "I'm private"

    def public_method(self):
        print("This is a public method")

    def _protected_method(self):
        print("This is a protected method")

    def __private_method(self):
        print("This is a private method")

obj=MyClass()


# Accessing public attributes and methods
print(obj.public_attribute)  # Output: I'm public
obj.public_method()          # Output: This is a public method

# Accessing protected attributes and methods
print(obj._protected_attribute)  # Output: I'm protected
obj._protected_method()          # Output: This is a protected method

# Trying to access private attributes and methods (will raise an AttributeError)
# print(obj.__private_attribute)  # This line will raise an AttributeError
# obj.__private_method()          # This line will raise an AttributeError

