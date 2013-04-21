#!/usr/bin/python

import RPi.GPIO as GPIO
import time

class LeftMotor:
    __coil_A_1_pin = 23
    __coil_A_2_pin = 24
    __coil_B_1_pin = 9
    __coil_B_2_pin = 10
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.__coil_A_1_pin, GPIO.OUT)
        GPIO.setup(self.__coil_A_2_pin, GPIO.OUT)
        GPIO.setup(self.__coil_B_1_pin, GPIO.OUT)
        GPIO.setup(self.__coil_B_2_pin, GPIO.OUT)
    def __setStep(self, v1, v2, v3, v4):
        GPIO.output(self.__coil_A_1_pin, v1)
        GPIO.output(self.__coil_A_2_pin, v2)
        GPIO.output(self.__coil_B_1_pin, v3)
        GPIO.output(self.__coil_B_2_pin, v4)
        return
    def moveForward(self, delay, steps):
        for i in range(0, int(steps)):
            self.__setStep(1, 0, 0, 1)
            time.sleep(delay)
            self.__setStep(0, 1, 0, 1)
            time.sleep(delay)
            self.__setStep(0, 1, 1, 0)
            time.sleep(delay)
            self.__setStep(1, 0, 1, 0)
            time.sleep(delay)
        self.__setStep(0, 0, 0, 0)
    def moveBackward(self, delay, steps):
        for i in range(0, int(steps)):
            self.__setStep(1, 0, 1, 0)
            time.sleep(delay)
            self.__setStep(0, 1, 1, 0)
            time.sleep(delay)
            self.__setStep(0, 1, 0, 1)
            time.sleep(delay)
            self.__setStep(1, 0, 0, 1)
            time.sleep(delay)
        self.__setStep(0, 0, 0, 0)

class RightMotor:
    __coil_A_1_pin = 4
    __coil_A_2_pin = 17
    __coil_B_1_pin = 8
    __coil_B_2_pin = 7
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.__coil_A_1_pin, GPIO.OUT)
        GPIO.setup(self.__coil_A_2_pin, GPIO.OUT)
        GPIO.setup(self.__coil_B_1_pin, GPIO.OUT)
        GPIO.setup(self.__coil_B_2_pin, GPIO.OUT)
    def __setStep(self, v1, v2, v3, v4):
        GPIO.output(self.__coil_A_1_pin, v1)
        GPIO.output(self.__coil_A_2_pin, v2)
        GPIO.output(self.__coil_B_1_pin, v3)
        GPIO.output(self.__coil_B_2_pin, v4)
        return
    def moveForward(self, delay, steps):
        for i in range(0, int(steps)):
            self.__setStep(1, 0, 1, 0)
            time.sleep(delay)
            self.__setStep(0, 1, 1, 0)
            time.sleep(delay)
            self.__setStep(0, 1, 0, 1)
            time.sleep(delay)
            self.__setStep(1, 0, 0, 1)
            time.sleep(delay)
        self.__setStep(0, 0, 0, 0)
    def moveBackward(self, delay, steps):
        for i in range(0, int(steps)):
            self.__setStep(1, 0, 0, 1)
            time.sleep(delay)
            self.__setStep(0, 1, 0, 1)
            time.sleep(delay)
            self.__setStep(0, 1, 1, 0)
            time.sleep(delay)
            self.__setStep(1, 0, 1, 0)
            time.sleep(delay)
        self.__setStep(0, 0, 0, 0)

