import asyncio
import websockets
import os
import RPi.GPIO as GPIO
import time

hiz = 0

IN1 = 38
IN2 = 40
IN3 = 29
IN4 = 31
ENA = 35
ENB = 33
GPIO.setmode(GPIO.BOARD)

GPIO.setup(IN1, GPIO.OUT, initial= GPIO.LOW)
GPIO.setup(IN2, GPIO.OUT, initial= GPIO.LOW)
GPIO.setup(IN3, GPIO.OUT, initial= GPIO.LOW)
GPIO.setup(IN4, GPIO.OUT, initial= GPIO.LOW)
GPIO.setup(ENA, GPIO.OUT, initial= GPIO.LOW)
GPIO.setup(ENB, GPIO.OUT, initial= GPIO.LOW)

motor1 = GPIO.PWM(ENA, 1000)
motor2 = GPIO.PWM(ENB, 1000)
motor1.start(50)
motor2.start(50)


def dur():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)

def ileri(hiz):
    dur()
    motor1.ChangeDutyCycle(hiz)
    motor2.ChangeDutyCycle(hiz)

    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN4, GPIO.HIGH)

def geri(hiz):
    dur()
    motor1.ChangeDutyCycle(hiz)
    motor2.ChangeDutyCycle(hiz)

    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)

def sag(hiz):
    dur()
    motor1.ChangeDutyCycle(hiz)
    motor2.ChangeDutyCycle(hiz)

    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    

def sol(hiz):
    dur()
    motor1.ChangeDutyCycle(hiz)
    motor2.ChangeDutyCycle(hiz)

    GPIO.output(IN4, GPIO.HIGH)
    GPIO.output(IN2, GPIO.HIGH)

async def server(websocket, path):
    global hiz
    async for message in websocket:
        listed = message.split(" ")

        if message == "İleri":
            print("İleri gidiyorum...")
            ileri(hiz)
        elif listed[0] == "hiz":
            hiz = int(listed[1])
            print(hiz)
        elif message == "Dur":
            print("Durdum")
            dur()
            
        elif message == "Geri":
            print("Geri gidiyorum...")
            geri(hiz)
            
        elif message == "Sağ":
            print("Sağa gidiyorum...")
            sag(hiz)
            
        elif message == "Sol":
            print("Sola gidiyorum...")
            sol(hiz)

async def main():
    async with websockets.serve(server, "127.0.0.1", 55555):
        await asyncio.Future()  # Sonsuz döngü

asyncio.run(main())
