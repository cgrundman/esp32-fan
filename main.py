from machine import Pin # type: ignore
import time

led = Pin(4, Pin.OUT)  # onboard LED
while True:
    led.value(not led.value())
    time.sleep(0.5)