'''
Developer: Ömer Ulutürk
Date: 11.03.2021
Purpose of Software: Reinforcement of learned Python Code and Self-improvement
==========================Triangle and Rectangle========================================0
Create a class named Triangle and Rectangle.
Create a subclass named Square inherited from Rectangle.
Create a subclass named Cube inherited from Square.
Create a subclass named Pyramid multiple inherited both from Triangle and Square.
Two dimensional classes (Triangle, Rectangle and Square) should have:
its dimensions as attributes.(can be inherited from a superclass)
methods which calculate its area and perimeter separately. Three dimensional classes (Cube and Pyramid) should have:
its dimensions as attributes which are inherited from a superclass
its extra dimensions if there is. (hint: maybe for Pyramid)
methods which calculate its volume and surface area separately. (surface area is optional, you may not do this)
'''
class Triangle:
    def __init__(self):
        self.first_edge = int(input("Enter first edge of the triangle:"))
        self.second_edge = int(input("Enter second edge of the triangle:"))
        self.third_edge = int(input("Enter third edge of the triangle:"))
        self.Perimeter()
        self.Area()
        print(f"Perimeter of the triangle is:{self.perimeter}\nArea of the triangle is:{self.area}")

    def Perimeter(self):
        self.perimeter = self.first_edge + self.second_edge + self.third_edge
        return self.perimeter

    def Area(self):
        self.u = self.perimeter / 2
        self.area = 0.5 ** (self.u * (self.u - self.first_edge) * (self.u - self.second_edge) * (self.u - self.third_edge))
        return self.area


class Rectangle:
    def __init__(self):
        self.first_edge = int(input("Enter first edge of the rectangle:"))
        self.second_edge = int(input("Enter second edge of the rectangle:"))
        print(f"Perimeter of the rectangle is:{self.perimeter}\nArea of the rectangle is:{self.area}")

    def Perimeter(self):
        self.perimeter = (self.first_edge + self.second_edge) * 2
        return self.perimeter

    def Area(self):
        self.area = self.first_edge * self.second_edge
        return self.area


class Square(Rectangle):
    def __init__(self):
        self.first_edge = int(input("Enter one edge of the square:"))
        self.second_edge = self.first_edge
        self.Perimeter()
        self.Area()
        print(f"Perimeter of the square is:{self.perimeter}\nArea of the square is:{self.area}")


class Cube(Square):
    def __init__(self):
        self.first_edge = int(input("Enter one edge of the cube:"))
        self.second_edge = self.first_edge
        self.surface_area = self.Area()*6
        self.Volume()
        print(f"Surface area of the cube is:{self.surface_area}\nVolume of the square is:{self.volume}")

    def Volume(self):
        self.volume = self.Area()*self.first_edge
        return self.volume


class Pyramid(Triangle, Rectangle):
    def __init__(self):
        print('''
         1. Tetrahedron (floor is triangle)
         2. Square Pyramid (floor is square)
         ''')
        choise = input("Select your Pyramid: ")
        if choise == "1":
            self.Triangular_Pyramid()
        elif choise == "2":
            self.Square_Pyramid()

    def Triangular_Pyramid(self):
        self.first_edge = int(input("Enter one edge of the base:"))
        self.second_edge = self.first_edge
        self.third_edge = self.first_edge
        self.slant_height = int(input("Enter slant height:"))
        #self.base_area = (3**0.5)*self.first_edge**2/4
        Triangle.Perimeter(self)
        self.surface_area = Triangle.Area(self)+0.5*Triangle.Perimeter(self)*self.slant_height
        self.volume = Triangle.Area(self)*self.slant_height/3
        print(f"Surface area of the pyramid is:{self.surface_area}\n"
              f"Volume of the pyramid is:{self.volume}")
    def Square_Pyramid(self):
        self.first_edge = int(input("Enter one edge of the base:"))
        self.second_edge = self.first_edge
        self.slant_height = int(input("Enter slant height:"))
        self.surface_area = Rectangle.Area(self)+(2*self.first_edge*self.slant_height)
        self.volume = Rectangle.Area(self)*self.slant_height/3
        print(f"Surface area of the pyramid is:{self.surface_area}\n"
              f"Volume of the pyramid is:{self.volume}")

def program():
    while True:
        print('''

        1. Triangle
        2. Rectangle
        3. Square
        4. Cube
        5. Pyramid
        6. Exit
        ''')
        choise = int(input("Select your shape: "))
        if choise == 1:
            Triangle()
        elif choise == 2:
            Rectangle()
        elif choise == 3:
            Square()
        elif choise == 4:
            Cube()
        elif choise == 5:
            Pyramid()
        elif choise == 6:
            print("Thanks... Have a good day!")
            break
        else:
            True
program()