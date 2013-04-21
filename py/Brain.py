#!/usr/bin/python

from Motor import LeftMotor
from Motor import RightMotor

class Brain:
    leftMotor = LeftMotor()
    rightMotor = RightMotor()
    def moveForward(self):
        print "Move Forward"
    def moveBackward(self):
        print "Move Backward"
    def moveLeft(self, delay):
        self.leftMotor.moveForward(int(delay) / 1000.0, 100)
    def moveRight(self, delay):
        self.rightMotor.moveForward(int(delay) / 1000.0, 100)
