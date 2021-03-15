#!/usr/bin/env python3
from turtle import Turtle
import time


class TurtleFlower(Turtle):
    """ creates an instance of Turtle with a method called drawFlower """
    def __init__(self,*args, **kwargs):
        super(TurtleFlower, self).__init__(*args, **kwargs)
        print("Time for Turtle Flower!")
    
    def drawFlower(self, numOfSquares):
        for i in range(numOfSquares):
            self.begin_fill()
            for j in range(4):
                self.fd(70)
                self.rt(90)
            self.lt(360/numOfSquares)
            self.end_fill()
                




t = TurtleFlower()
t.drawFlower(10)
time.sleep(3)


