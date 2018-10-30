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

def off ():
    GPIO.output(11, False)
    GPIO.output(13, False)
    return 0

if __name__ == '__main__':
    try:
    state = off()
    

try:
    state = lowon()

    while True:
        fo = open("/sys/class/thermal/thermal_zone0/temp")
        str = fo.read()
        fo.close()
        temp = int(str)/1000

        print(temp)
        
        if state == 0:
            if temp >= midtemp:
                state = lowon()
                
        if state == 1:
            if temp >= hightemp:
                state = highon()
            else:
                if temp <= midtemp - delta:
                    state = off ()
                    
        if state == 2:
            if temp <= hightemp - delta:
                state = lowon()
        print(state)
        
    time.sleep(15)
    #try:
    #while True:
    #char = screen.getch()
    #print chr(char)
    #if char == ord('q'):
        #break
    #elif char == ord('1'):
        #GPIO.output(11, False)
        #GPIO.output(13, False)
    #elif char == ord('2'):
        #GPIO.output(11, True)
        #GPIO.output(13, False)
    #elif char == ord('3'):
        #GPIO.output(11, True)
        #GPIO.output(13, True)
    #time.sleep(.5)

    finally:
        curses.nocbreak(); screen.keypad(0); curses.echo()
        curses.endwin()
        GPIO.cleanup()  

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

