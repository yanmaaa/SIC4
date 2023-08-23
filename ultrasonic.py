import RPi.GPIO as GPIO
import time

# Konfigurasi pin GPIO
TRIGGER_PIN = 20
ECHO_PIN = 21
TRIGGER_PIN2 = 19
ECHO_PIN2 = 26
TRIGGER_PIN3 = 6
ECHO_PIN3 = 13
TRIGGER_PIN4 = 12
ECHO_PIN4 = 16
TRIGGER_PIN5 = 3
ECHO_PIN5 = 4
TRIGGER_PIN6 = 17
ECHO_PIN6 = 27


def init_ultrasonic():
    # GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIGGER_PIN, GPIO.OUT)
    GPIO.setup(ECHO_PIN, GPIO.IN)
    GPIO.setup(TRIGGER_PIN2, GPIO.OUT)
    GPIO.setup(ECHO_PIN2, GPIO.IN)
    GPIO.setup(TRIGGER_PIN3, GPIO.OUT)
    GPIO.setup(ECHO_PIN3, GPIO.IN)
    GPIO.setup(TRIGGER_PIN4, GPIO.OUT)
    GPIO.setup(ECHO_PIN4, GPIO.IN)
    GPIO.setup(TRIGGER_PIN5, GPIO.OUT)
    GPIO.setup(ECHO_PIN5, GPIO.IN)
    GPIO.setup(TRIGGER_PIN6, GPIO.OUT)
    GPIO.setup(ECHO_PIN6, GPIO.IN)

def inven1():
    GPIO.output(TRIGGER_PIN, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(TRIGGER_PIN, GPIO.LOW)
    
    pulse_start = time.time()
    
    while GPIO.input(ECHO_PIN) == GPIO.LOW:
        pulse_start = time.time()
    
    while GPIO.input(ECHO_PIN) == GPIO.HIGH:
        pulse_end = time.time()
    
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # Kecepatan suara adalah 343 meter/detik
    distance = round(distance, 2)
    
    return distance

def inven2():
    GPIO.output(TRIGGER_PIN2, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(TRIGGER_PIN2, GPIO.LOW)
    
    pulse_start = time.time()
    
    while GPIO.input(ECHO_PIN2) == GPIO.LOW:
        pulse_start = time.time()
    
    while GPIO.input(ECHO_PIN2) == GPIO.HIGH:
        pulse_end = time.time()
    
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # Kecepatan suara adalah 343 meter/detik
    distance = round(distance, 2)
    
    return distance

def inven3():
    GPIO.output(TRIGGER_PIN3, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(TRIGGER_PIN3, GPIO.LOW)
    
    pulse_start = time.time()
    
    while GPIO.input(ECHO_PIN3) == GPIO.LOW:
        pulse_start = time.time()
    
    while GPIO.input(ECHO_PIN3) == GPIO.HIGH:
        pulse_end = time.time()
    
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # Kecepatan suara adalah 343 meter/detik
    distance = round(distance, 2)
    
    return distance

def inven4():
    GPIO.output(TRIGGER_PIN4, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(TRIGGER_PIN4, GPIO.LOW)
    
    pulse_start = time.time()
    
    while GPIO.input(ECHO_PIN4) == GPIO.LOW:
        pulse_start = time.time()
    
    while GPIO.input(ECHO_PIN4) == GPIO.HIGH:
        pulse_end = time.time()
    
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # Kecepatan suara adalah 343 meter/detik
    distance = round(distance, 2)
    
    return distance

def inven5():
    GPIO.output(TRIGGER_PIN5, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(TRIGGER_PIN5, GPIO.LOW)
    
    pulse_start = time.time()
    
    while GPIO.input(ECHO_PIN5) == GPIO.LOW:
        pulse_start = time.time()
    
    while GPIO.input(ECHO_PIN5) == GPIO.HIGH:
        pulse_end = time.time()
    
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # Kecepatan suara adalah 343 meter/detik
    distance = round(distance, 2)
    
    return distance

def inven6():
    GPIO.output(TRIGGER_PIN6, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(TRIGGER_PIN6, GPIO.LOW)

    pulse_start = time.time()
    # pulse_end = pulse_start  # Inisialisasi pulse_end di sini

    while GPIO.input(ECHO_PIN6) == GPIO.LOW:
        pulse_start = time.time()

    while GPIO.input(ECHO_PIN6) == GPIO.HIGH:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # Kecepatan suara adalah 343 meter/detik
    distance = round(distance, 2)

    return distance

def calculate_stock(distance):
    if distance >= 24:
        stock = 0
    elif distance >= 21 and distance <24:
        stock = 1
    elif distance >= 18 and distance <21:
        stock = 2
    elif distance >= 15 and distance <18:
        stock = 3
    elif distance >= 12 and distance <15:
        stock = 4
    elif distance >= 9 and distance <12:
        stock = 5
    elif distance >= 6 and distance <9:
        stock = 6
    elif distance >= 3 and distance <6:
        stock = 7
    elif distance >= 0 and distance <3:
        stock = 8
    else :
        print("Program tidak jalan")
    return stock

def ultrasonic_distance():
    rack1 = inven1()
    rack2 = inven2()
    rack3 = inven3()
    rack4 = inven3()
    rack5 = inven5()
    rack6 = inven6()

    return rack1, rack2, rack3, rack4, rack5, rack6