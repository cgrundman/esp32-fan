from machine import Pin, PWM
pwm = PWM(Pin(0))
pwm.init(freq=1000, duty=1023) # duty = 0...1023