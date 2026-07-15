# Object-Oriented Programming (OOP) in Python

# OOP helps organize code into reusable, modular, and maintainable structures

class Animal:
    """Base class (Parent)"""
    species = "Animal"                    # Class attribute

    def __init__(self, name, age):
        self.name = name                  # Instance attributes
        self.age = age

    def speak(self):
        return f"{self.name} makes a sound!"

    def __str__(self):
        return f"{self.name} ({self.age} years old)"


class Dog(Animal):
    """Child class inheriting from Animal"""
    species = "Canine"

    def __init__(self, name, age, breed="Unknown"):
        super().__init__(name, age)       # Call parent constructor
        self.breed = breed

    def speak(self):                      # Method overriding (Polymorphism)
        return f"{self.name} says Woof! 🐶"

    def fetch(self):
        return f"{self.name} is fetching the ball!"


class Cat(Animal):
    """Another child class"""
    def speak(self):
        return f"{self.name} says Meow! 🐱"


# 1. Creating Objects
print("=== Creating Objects ===")
dog1 = Dog("Buddy", 5, "Golden Retriever")
cat1 = Cat("Whiskers", 3)

print(dog1)
print(cat1)
print(dog1.speak())
print(cat1.speak())

# 2. Inheritance & Polymorphism
print("\n=== Polymorphism ===")
animals = [dog1, cat1]
for animal in animals:
    print(f"{animal.name} says: {animal.speak()}")


# 3. Encapsulation (using properties)
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance          # Private attribute (name mangling)

    @property
    def balance(self):
        """Getter"""
        return self.__balance

    @balance.setter
    def balance(self, amount):
        """Setter with validation"""
        if amount >= 0:
            self.__balance = amount
        else:
            raise ValueError("Balance cannot be negative!")

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient funds!")
        self.__balance -= amount
        return self.__balance


print("\n=== Encapsulation Example ===")
account = BankAccount("Tester", 1000)
print(f"Initial balance: ${account.balance}")
account.deposit(500)
print(f"After deposit: ${account.balance}")

try:
    account.withdraw(2000)
except ValueError as e:
    print("Error:", e)


# 4. Class Methods & Static Methods
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def info(cls):
        return f"This is class: {cls.__name__}"


print("\n=== Class & Static Methods ===")
print(MathUtils.add(10, 20))
print(MathUtils.info())


# 5. Abstraction (using abstract base classes)
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


rect = Rectangle(10, 5)
print("\n=== Abstraction Example ===")
print(f"Rectangle area: {rect.area()}")
print(f"Rectangle perimeter: {rect.perimeter()}")


# 6. Magic Methods (Dunder Methods)
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


print("\n=== Magic Methods ===")
v1 = Vector(2, 3)
v2 = Vector(5, 7)
print(v1 + v2)


print("\n=== OOP Pillars Summary ===")
print("""
1. Encapsulation → Bundling data + methods + hiding internals
2. Inheritance   → Code reuse (parent → child)
3. Polymorphism  → Same interface, different behavior
4. Abstraction   → Hide complex implementation details
""")

print("=== OOP makes your code more organized, reusable, and scalable! ===")