import machine
import utime
#Pin attatchment in MCU
# AENBL = 4
# BENBL = 16
# APHASE = 25
# BPHASE = 17
# CONFIG = 5
# M1 = 27
# nSLEEP = 2
# nFAULT = 34

AENBL = machine.Pin(4,machine.Pin.OUT)
BENBL = machine.Pin(16,machine.Pin.OUT)
APHASE = machine.Pin(25,machine.Pin.OUT)
BPHASE = machine.Pin(17,machine.Pin.OUT)
CONFIG = machine.Pin(5,machine.Pin.OUT)
M1 = machine.Pin(27,machine.Pin.OUT)
nSLEEP = machine.Pin(2,machine.Pin.OUT)
nFAULT = machine.Pin(34,machine.Pin.IN)
LED = machine.Pin(12,machine.Pin.OUT)
CONFIG.value(0)
nSLEEP.value(1)

# In phase/enable mode, the xPHASE input pins control the direction of current flow through each H-bridge.
#This sets the direction of rotation of a DC motor
# Driving the xENBL input pins active high enables the H-bridge outputs. This can be used as PWM speed control of a DC motor
# In phase/enable mode, the M1 input pin controls the state of the H-bridges when xENBL = 0.
#If M1 is high, the outputs are disabled (high impedance) when xENBL = 0; this corresponds to asynchronous fast decay mode,
#If M1 is low, then the outputs are both driven low; this corresponds to slow decay or brake mode, and is usually used when controlling
# the speed of a DC motor by PWMing the xENBL pin.

#When xENBL is 0, then M1 = 0 makes OUT = 0. Else OUT = z (slow decay or brake mode)

pwmAENBL = machine.PWM(AENBL)
pwmBENBL = machine.PWM(BENBL)
#pwmLED = machine.PWM(LED)

def blink(x):
    LED.value(1)
    utime.sleep_ms(x)
    LED.value(0)
    utime.sleep_ms(x)
    # pwmLED.freq(1000-x)
    # pwmLED.duty(40)

def movA(dir):
    APHASE.value(dir)
    # AENBL.value(1)
    pwmAENBL.freq(10)
    pwmAENBL.duty(100)
    # print("Moving")

def movB(dir):
    BPHASE.value(dir)
    # BENBL.value(1)
    pwmBENBL.freq(10)
    pwmBENBL.duty(100)
def brakeA():
    AENBL.value(0)
    M1.value(0)

def brakeB():
    BENBL.value(0)
    M1.value(0)

def slowA():
    AENBL.value(0)
    M1.value(1)

def slowB():
    BENBL.value(0)
    M1.value(1)

def delay(x):
    for i in range(x):
        utime.sleep_ms(1)

utime.sleep_ms(2000)

while True:
    if (nFAULT == 0):
        print("Fault!!!")
        blink(100)
        break
    #blink(700)
    movA(1)
    movB(0)
    delay(50)
    slowA()
    slowB()
    delay(50)
    movA(0)
    movB(1)
    delay(50)
    slowA()
    slowB()
    delay(50)
    # print("Working")
    # #Run forward
    # movA(1)
    # movB(0)
    # delay(100)
    # blink(700)
    # #Slow now
    # slowA()
    # slowB()
    # delay(500)
    # #Run Backwards
    # movA(0)
    # movB(1)
    # delay(100)
    # blink(700)
    # #brake
    # brakeA()
    # brakeB()
    # delay(100)
    # blink(700)
    # #MOve forward and slow wheel A
    # #Run forward
    # movA(1)
    # movB(0)
    # delay(1000)
    # blink(700)
    # #Slow now
    # slowA()
    # delay(1000)
    # blink(700)
