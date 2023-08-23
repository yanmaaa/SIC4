import RPi.GPIO as GPIO
import time

from ultrasonic import init_ultrasonic, calculate_stock, ultrasonic_distance
from ubidots import build_payload, post_request

def setup():
    GPIO.setmode(GPIO.BCM)
    init_ultrasonic()

def loop():
    while True:
        rack1, rack2, rack3, rack4, rack5, rack6 = ultrasonic_distance()
        stock1 = calculate_stock(rack1)
        stock2 = calculate_stock(rack2)
        stock3 = calculate_stock(rack3)
        stock4 = calculate_stock(rack4)
        stock5 = calculate_stock(rack5)
        stock6 = calculate_stock(rack6)
    
        print(f"Ultra 1 - Jarak: {rack1} cm, Stok: {stock1}")
        print(f"Ultra 2 - Jarak: {rack2} cm, Stok: {stock2}")
        print(f"Ultra 3 - Jarak: {rack3} cm, Stok: {stock3}")
        print(f"Ultra 4 - Jarak: {rack4} cm, Stok: {stock4}")
        print(f"Ultra 5 - Jarak: {rack5} cm, Stok: {stock5}")
        print(f"Ultra 6 - Jarak: {rack6} cm, Stok: {stock6}\n")
        time.sleep(3)


        payload = build_payload(rack1, rack2, rack3, rack4, rack5, rack6)
        print("[INFO] Attemping to send data")
        post_request(payload)
        print("[INFO] finished")

setup()
while True:
    loop()