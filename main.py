from machine import Pin # type: ignore
import time

led = Pin(35, Pin.OUT)

while True:
    led.value(not led.value())
    time.sleep(0.5)