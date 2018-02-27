import RPi.GPIO as GPIO


class RaspberrySdk:

    def __init__(self):
        GPIO.setmode(GPIO.BCM)

    def input(self, pin):
        GPIO.setup(pin, GPIO.IN)

    def output(self, pin):
        GPIO.setup(pin, GPIO.OUT)

    def high(self, pin):
        GPIO.output(pin, GPIO.HIGH)

    def low(self, pin):
        GPIO.output(pin, GPIO.LOW)

