class Circle:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        """The radius property."""
        print("Get radius")
        return self.__radius

    @radius.setter
    def radius(self, value):
        print("Set radius")
        self.__radius = value

    @radius.deleter
    def radius(self):
        print("Delete radius")
        del self.__radius


circle = Circle(42.0)
print(circle.radius)
circle.radius = 100.0
print(circle.radius)
del circle.radius
# print(circle.radius)
help(circle)