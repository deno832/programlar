import RPi.GPIO as GPIO
import time

IN1 = 38
IN2 = 40
IN3 = 29       # pin tanımlamaları yapılıyor.
IN4 = 31
ENA = 35
ENB = 33

GPIO.setmode(GPIO.BOARD)

GPIO.setup(IN1, GPIO.OUT, initial= GPIO.LOW)
GPIO.setup(IN2, GPIO.OUT, initial= GPIO.LOW)
GPIO.setup(IN3, GPIO.OUT, initial= GPIO.LOW)
GPIO.setup(IN4, GPIO.OUT, initial= GPIO.LOW)

def dur(hiz=0):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)

def ileri(hiz=0):
    dur()
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN4, GPIO.HIGH)

def geri(hiz=0):
    dur()
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)

def sag(hiz=0):
    dur()
    GPIO.output(IN1, GPIO.HIGH)
    

def sol(hiz=0):
    dur()
    GPIO.output(IN4, GPIO.HIGH)

try:
    sag()
    time.sleep(6)
    sol()
    time.sleep(6)
except:
    GPIO.cleanup()

GPIO.cleanup()
