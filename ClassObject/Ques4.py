'''Assignment 4: Rectangle Calculator

 A civil engineer wants to calculate the area and perimeter of a rectangular plot.

Create a class Rectangle with the following attributes:

Length

Breadth

Create the following methods:

calculate_area() – Calculate the area.

calculate_perimeter() – Calculate the perimeter.

display_result() – Display length, breadth, area, and perimeter.

Formulas:

Area = Length × Breadth
Perimeter = 2 × (Length + Breadth)

Sample data:

Length: 15
Breadth: 8'''


class Rectangle:
    def set(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        self.area=self.l*self.b
    def perimeter(self):
        self.perimeter=2*(self.l+self.b)
    def result(self):
        print("Length:",self.l)
        print("Bradth:",self.b)
        print("Area:",self.area)
        print("Perimeter:",self.perimeter)

r1=Rectangle()
r1.set(15,8)
r1.area()
r1.perimeter()
r1.result()