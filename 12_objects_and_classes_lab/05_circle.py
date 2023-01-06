class Circle:
    pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter

    def calculate_circumference(self):
        circumference = self.diameter * Circle.pi
        return circumference

    def calculate_area(self):
        area = ((self.diameter ** 2) / 4) * Circle.pi
        return area

    def calculate_area_of_sector(self, angle):
        #  Sector Area = r² × α / 2.
        area_of_sector = ((self.diameter ** 2) / 4) * Circle.pi * (angle / 360)
        return area_of_sector


circle = Circle(10)

angle = 5
print(circle.pi)
print(Circle.calculate_circumference(circle))
print(circle.calculate_area())
print(circle.calculate_area_of_sector(angle))
