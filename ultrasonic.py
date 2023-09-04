import RPi.GPIO as GPIO
import time

# Konfigurasi pin GPIO
TRIGGER_PIN = 20
ECHO_PIN = 21
TRIGGER_PIN2 = 19
ECHO_PIN2 = 26
TRIGGER_PIN3 = 6
ECHO_PIN3 = 13
TRIGGER_PIN4 = 23
ECHO_PIN4 = 24
TRIGGER_PIN5 = 3
ECHO_PIN5 = 4
TRIGGER_PIN6 = 17
ECHO_PIN6 = 27

# Inisialisasi GPIO
def init_ultrasonic():
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
    GPIO.setwarnings(False)
    
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
    GPIO.setwarnings(False)

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
    GPIO.setwarnings(False)
    
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
    GPIO.setwarnings(False)
    
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
    GPIO.setwarnings(False)
    
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
    GPIO.setwarnings(False)
    
    pulse_start = time.time()
    
    while GPIO.input(ECHO_PIN6) == GPIO.LOW:
        pulse_start = time.time()
    
    while GPIO.input(ECHO_PIN6) == GPIO.HIGH:
        pulse_end = time.time()
    
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # Kecepatan suara adalah 343 meter/detik
    distance = round(distance, 2)
    
    return distance

def calculate_stock(distance):
    if distance >= 16:
        stock = 0
    elif distance >= 13 and distance <16:
        stock = 1
    elif distance >= 10 and distance <13:
        stock = 2
    elif distance >= 7 and distance <10:
        stock = 3
    elif distance >= 4 and distance <7:
        stock = 4
    elif distance >= 0 and distance <4:
        stock = 5
    # elif distance >= 0 and distance <2:
    #     stock = 6
    else :
        print("Program tidak jalan")
    return stock

def ultrasonic_distance():
    rack1 = inven1()
    rack2 = inven2()
    rack3 = inven3()
    rack4 = inven4()
    rack5 = inven5()
    rack6 = inven6()

    return rack1, rack2, rack3, rack4, rack5, rack6