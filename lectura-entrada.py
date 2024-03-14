#Hola Mundo

import machine
import utime

led_onboard = machine.Pin("LED", machine.Pin.OUT)

while True:
    led_onboard.value(1)
    utime.sleep(10.5)
    led_onboard.value(0)
    utime.sleep(0.5)