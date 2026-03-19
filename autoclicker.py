import keyboard
import mouse
from time import sleep

key = "q"
kil = False
time = 0.01

while True:
    if keyboard.is_pressed(key):
        kil = not kil
        sleep(0.3)


    if kil:
        mouse.click()
        sleep(time)



