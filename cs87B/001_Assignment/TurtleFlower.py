#!/usr/bin/env python3
from turtle import Turtle

class TurtleFlower(Turtle):
    """ doc string """
    def __init__(self, *args, **kwargs):
        super(TurtleFlower, self).__init__(*args, **kwargs)
        print("Time for Turtle Flower!")
    
    def drawFlower(self, numOfSquares):
        self.right(30)
        self.forward(100)
        self.right(90)
        self.forward(100)
        self.forward(100)
        self.forward(100)




t = TurtleFlower()
t.drawFlower(0)
# print(t)
# t.right(30)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)

