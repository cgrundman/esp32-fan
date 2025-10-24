from machine import Pin, SoftI2C, PWM
from bh1750 import BH1750
import time

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=400000)

light_sensor = BH1750(bus=i2c, addr=0x23)

pwm = PWM(Pin(2))
pwm.init(freq=1000, duty=0)

last_toggle = time.ticks_ms()
pwm_on = False

try:
    while True:
        lux = light_sensor.luminance(BH1750.CONT_HIRES_1)
        print("Luminance: {:.2f} lux".format(lux))
        #time.sleep(1)

        current_time = time.ticks_ms()
        if time.ticks_diff(current_time, last_toggle) >= 1000:
            pwm_on = not pwm_on  # Toggle state
            pwm.duty(1023 if pwm_on else 0)
            last_toggle = current_time  # Reset timer

except Exception as e:
    print("An error occurred:", e)