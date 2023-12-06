import utime

import machine
from machine import I2C
from machine import Pin
from time import sleep
import dht
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
 
I2C_ADDR     = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20

sensor = dht.DHT11(Pin(2))
i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)    

while True:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    print("Temperature: {}   Humidity: {:.0f}% ".format(temp, hum))
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr("Temperature: {}°C".format(temp))
    lcd.move_to(0,1)
    lcd.putstr("Humidity: {:.0f}% ".format(hum))


    sleep(2)
