from machine import Pin as pin
from utime import sleep
b1=pin(22,pin.IN,pin.PULL_UP)
b2=pin(23,pin.IN,pin.PULL_UP)
b3=pin(19,pin.IN,pin.PULL_UP)
b4=pin(5,pin.IN,pin.PULL_UP)
led=pin(14,pin.OUT)

while True:
    a = b1.value()
    b = b2.value()
    c = b3.value()
    d = b4.value()
    
    Z= not((a and b) and (c and d)) #aqui se ingresa la ecuacion deseada
    
    led.value(Z)
    print (int (Z))
    sleep(0.1)
