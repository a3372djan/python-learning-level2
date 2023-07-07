import time

from machine import Pin

D6 = 12
D8 = 15
D5 = 14

ledGreen = Pin(D6, Pin.OUT)
ledred = Pin(D5, Pin.OUT)
ledBlue = Pin(D8, Pin.OUT)
time.sleep(2)

for i in range(0,10):
    print("bule")
    ledBlue.on()
    ledred.off()
    ledGreen.off()
    time.sleep(2)

    print("red")
    ledBlue.off()
    ledred.off()
    ledGreen.on()
    time.sleep(2)

    print("green")
    ledBlue.off()
    ledred.on()
    ledGreen.off()
    time.sleep(2)


