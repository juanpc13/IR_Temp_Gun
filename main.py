import ssd1306
import mlx90614
from machine import I2C, Pin, Timer


i2c = I2C(scl=Pin(2), sda=Pin(0))

sensor = mlx90614.MLX90614(i2c)

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

mode = 0
temperatura = 0

def map(value, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    valueScaled = float(value - leftMin) / float(leftSpan)
    return rightMin + (valueScaled * rightSpan)

def converData(data):
    # Human Mode Calibration
    if mode == 0:
        data = map(data, 24.65, 31.75, 24.0, 32.3)
    data = '{:.2f}'.format(data)
    return data

def show():
    # print('Objeto:' + converData(sensor.read_object_temp()))
    oled.fill(0)
    oled.text('Objeto:' + converData(temperatura), 0, 0)
    oled.show()

def temp():
    global temperatura
    temperatura = temperatura * 4 + sensor.read_object_temp()
    temperatura = temperatura / 5

timDisplay = Timer(-1)
timDisplay.init(period=250, mode=Timer.PERIODIC, callback=lambda t:show())

timTemp = Timer(0)
timTemp.init(period=250, mode=Timer.PERIODIC, callback=lambda t:temp())
# tim.init()