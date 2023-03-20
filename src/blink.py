import time

from machine import Pin

led = Pin(1)
print(led)

for i in range(10):
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)
