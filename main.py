from random import randint
import turtle


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.lowleft.x < self.x < rectangle.upright.x \
                and rectangle.lowleft.y < self.y < rectangle.upright.y:
            return True
        else:
            return False

    def distance_between_two_points(self, point):
        distance = ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
        return distance


class Rectangle:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        """Calculates the area of the rectangle"""
        horizontal_edge = abs(self.point1.x - self.point2.x)
        longitutinal_edge = abs(self.point1.y - self.point2.y)
        return horizontal_edge * longitutinal_edge

    def is_square(self):
        """Is the rectangle square or not"""
        if abs(self.point1.x - self.point2.x) == abs(self.point1.y - self.point2.y):
            return True
        return False

    def fit_circle(self):
        """
        This method calculates the radius of the largest circle that can fit inside the rectangle and
        how many of these circles can fit inside the rectangle.
        """
        horizontal_edge = abs(self.point1.x - self.point2.x)
        longitutinal_edge = abs(self.point1.y - self.point2.y)
        diameter_of_the_largest_circle = min(horizontal_edge, longitutinal_edge)
        number_of_the_largest_circle = abs(horizontal_edge - longitutinal_edge) + 1


class TurtleRectangle(Rectangle):

    def draw_rectangle(self, canvas):
        """This method draws the rectangle by using turtle library"""
        # Go to a certain coordinate. This coordinate will be one of the four edges of the rectangle
        # When we go to that certain point, we dont want the tail to be seen. So we use the penup() method of turtle
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)

        # Now pendown() method will be used in order to illustrate the rectangle
        canvas.pendown()
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)

        turtle.done()


# DRIVER CODE

my_turtle = turtle.Turtle()
my_rectangle = TurtleRectangle(Point(100, 200), Point(50, 150))
#my_rectangle.draw_rectangle(canvas=my_turtle)


