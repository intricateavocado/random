import keyboard
import time
import datetime
loop = True


hourspast = 0

def work():
    keyboard.write("/work"); keyboard.send("enter"); keyboard.send("enter")

def daily():
    keyboard.write("/daily"); keyboard.send("enter"); keyboard.send("enter")

time.sleep(60 * (60 - datetime.datetime.now().minute))
while loop:
    work()
    time.sleep(60 * 60)
    hourspast += 1
    if hourspast == 24:
        daily()
        hourspast = 0