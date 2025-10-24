from machine import Pin, ADC

adc = ADC(Pin(36))

while True:
    voltage = adc.read_uv()
    print(voltage)