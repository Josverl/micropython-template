# use uasyncio to blink the LED
import uasyncio
from machine import Pin


async def blink(led, period_ms):
    while True:
        led.on()
        await uasyncio.sleep_ms(5)
        led.off()
        await uasyncio.sleep_ms(period_ms)


async def main(led1, led2, duration=10_000):
    uasyncio.create_task(blink(led1, 700))
    uasyncio.create_task(blink(led2, 400))
    await uasyncio.sleep_ms(duration)


# Running on a generic board
uasyncio.run_until_complete(main(Pin(1), Pin(2)))
