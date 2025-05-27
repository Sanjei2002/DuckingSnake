# classes : blue print for crrsting new objects


from abc import ABC, abstractmethod
from collections import namedtuple


class MyPoint:

    # Class Attribute
    GlobalPoint: int

    # properties
    # non Pythonic way
    def __get_x__(self):
        return self.__x

    def __set_x__(self, value: int):
        self.__y = value

    X = property(__get_x__, __set_x__, doc="X")

    # Pythonic Way

    @property
    def Y(self):
        return self.__y

    @Y.setter
    def Y(self, value: int):
        self.__y = value

    # Declraing a constructor is doneusing a magic method called Init

    def __init__(self, x: int, y: int):
        # instance Attribute
        self.__x = x
        self.__y = y

   # cls allows the method to operate on the class it's called on, making it more versatile

    @classmethod
    def create_point(cls):
        return cls(x=10, y=20)

    # magic method Two Underscores called automallicaly by pyhton like cosntrutor and ToString in c#
    def __str__(self) -> str:
        return f"({self.__x},{self.__y})"

    def __eq__(self, value):
        return self.__x == value.__x and self.__y == value.__y

    def __add__(self, value):
        self.__x = self.__x + value.__x
        self.__y = self.__y + value.__y
        return self.create_point()

    def __private_draw(self, x: int, y: int) -> None:
        print(F"Private Draw {x} {y}")

    # gives Indexing accesing for the class
    def __getitem__(self, name):
        if name == "x":
            return self.__x
        else:
            return self.__y

    def __iter__(self):
        return iter([self.X, self.Y])

# by accessing x, y in the Init magic method it beacmes part of MyPoint object

    def draw_a_point(self) -> None:
        self.__private_draw(x=self.__x, y=self.__y)


point = MyPoint(x=5, y=20)
point.draw_a_point()

print(
    f"point property using Property getter setter {point.X}  {point.Y} {point["x"]}")
# print(f"{point.__private_draw}")  # will Throw error

# because objects in python are dynmaic new attribute can be added after the object is created
point.z = 20

# in C# we do tpe checkingusing is , in Python we use isinstance() mehod
print("Type checking :", isinstance(point, MyPoint))

print("Class method :", MyPoint.create_point().draw_a_point())

print(point)

print(f"Overided equals {point == MyPoint.create_point()}")

print(f"adding objects {point + MyPoint.create_point()}")

for cord in point:
    print(f"iterating using __iter magic method {cord}")


# Custom Conatiner like [] list ,{} set ,{"name" : "Sanjei"} Dictionary


# inehritance

# inheriting Absract Base Class so the main Abstract cannot be instanciated
class Stream(ABC):

    # abstractmethod decorator forces child to give implementation to this method
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass


class MemoryStream(Stream):

    # method overiding hides the call to base call inorder to call base classes implementation first use Super
    def read(self):
        super().read()
        pass

    def write(self):
        pass


stream: Stream = MemoryStream()
stream.read()


# Multipe Inhheritance is supported in Python
class FlyAttribute:
    def fly(self):
        print("It can fly")


class SwimAttribute:
    def swim(self):
        print("It can Swim")


class FlyableSwim(FlyAttribute, SwimAttribute):
    pass


flyingFish = FlyableSwim()
flyingFish.fly()
flyingFish.swim()


# class without method : we might need a wrpper in this case NAmed Tupple can be used

SecondPoint = namedtuple("SecondPoint", ["X", "Y"])

tempPoint = SecondPoint(X=10, Y=20)

print(f"namedTupple for temprovary encapsultion {tempPoint.X} {tempPoint.Y}")
