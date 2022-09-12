from machine import Pin as pin
from utime import sleep
b1=pin(2,pin.IN,pin.PULL_UP)
b2=pin(4,pin.IN,pin.PULL_UP)
b3=pin(5,pin.IN,pin.PULL_UP)
b4=pin(25,pin.IN,pin.PULL_UP)
led=pin(14,pin.OUT)

while True:
    a = b1.value()
    b = b2.value()
    c = b3.value()
    d = b4.value()
    
    Z= (a or b) or (c or d) #aqui se ingresa la ecuacion deseada
    led.value(z)
    print (int (z))
    sleep(0.1)
   