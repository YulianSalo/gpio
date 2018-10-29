import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)

state = 0
hightemp = 55
delta = 10

def lowon ():
    GPIO.output(13, False)
    return 1

def highon ():
    GPIO.output(13, True)
    return 2

try:
    state = lowon()
    while True:
        fo = open("/sys/class/thermal/thermal_zone0/temp")
        str = fo.read()
        fo.close()
        temp = int(str)/1000
        if state == 1:
            if temp >= hightemp:
                state = highon()
        if state == 2:
            if temp <= hightemp - delta:
                state = lowon()
        print(temp, state)
        time.sleep(15)

finally:
    GPIO.cleanup()
