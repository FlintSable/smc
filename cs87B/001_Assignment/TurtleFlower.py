#!/usr/bin/env python3
from turtle import Turtle

class TurtleFlower(Turtle):
    """ doc string """
    def __init__(self, *args, **kwargs):
        super(TurtleFlower, self).__init__(*args, **kwargs)
        print("Time for Turtle Flower!")
    
    def drawFlower(self, numOfSquares):
        for i in range(4):
            self.fd(100)
            self.rt(90)
        self.end_fill()


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

