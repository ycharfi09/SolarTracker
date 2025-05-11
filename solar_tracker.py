from machine import ADC, Pin, PWM
from time import sleep


ldr1 = ADC(Pin(32))
ldr2 = ADC(Pin(33))
ldr3 = ADC(Pin(34))
ldr4 = ADC(Pin(35))

servo_v = PWM(Pin(13), freq=50)
servo_h = PWM(Pin(14), freq=50)

angle_v = 90
angle_h = 180

def move_servo(servo, angle):
    duty = int((angle / 180) * 102 + 26)
    servo.duty(duty)

move_servo(servo_v, angle_v)
move_servo(servo_h, angle_h)

while True:
    val1 = ldr1.read()
    val2 = ldr2.read()
    val3 = ldr3.read()
    val4 = ldr4.read()

    top_avg = (val1 + val2) / 2
    bottom_avg = (val3 + val4) / 2
    left_avg = (val1 + val3) / 2
    right_avg = (val2 + val4) / 2

    if top_avg - bottom_avg > 300 and angle_h < 180:
        angle_h += 5 #angle_h = angle_h+1
    elif bottom_avg - top_avg > 300 and angle_h > 160:
        angle_h -= 5
    if right_avg - left_avg < 300 and angle_v < 180:
        angle_v += 5
    elif left_avg - right_avg < 300 and angle_v > 0:
        angle_v -= 5

    move_servo(servo_v, angle_v)
    move_servo(servo_h, angle_h)
    print("        ",top_avg,"\n",left_avg,"          ",right_avg,"\n","        ",bottom_avg)
    print("angle_h: ",angle_h)
    sleep(0.1)

