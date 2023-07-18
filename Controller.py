import pyfirmata

comport = 'COM4' #port number

board = pyfirmata.Arduino(comport)

led_1 = board.get_pin('d:2:o')
led_2 = board.get_pin('d:3:o')
led_3 = board.get_pin('d:4:o')
buzzer_1 = board.get_pin('d:5:o')

def doorlockCondition(value):
    if value == 1:
        led_2.write(1)
        #led_3.write(0)
    if value == 0:
        led_2.write(0)
       # led_3.write(1)
def doorunlockCondition(value):
    if value == 1:
        #led_2.write(1)
        led_3.write(1)
    if value == 0:
       # led_2.write(0)
        led_3.write(0)
def systemCondition(value):
    if value == 1:
        led_1.write(1)
    #led_3.write(1)


def buzzerON(value):
    if value == 1:
        buzzer_1.write(1)
    if value == 0:
        buzzer_1.write(0)
