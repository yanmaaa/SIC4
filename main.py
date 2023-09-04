import RPi.GPIO as GPIO
import time
from datetime import datetime

from ultrasonic import init_ultrasonic, calculate_stock, ultrasonic_distance
# from ubidots import build_payload, post_request
from mongo import connect_to_mongodb, insert_data_to_mongodb

def setup():
    GPIO.setmode(GPIO.BCM)
    init_ultrasonic()

def loop(db):
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

        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        data = {
            "rack1_distance": stock1,
            "rack2_distance": stock2,
            "rack3_distance": stock3,
            "rack4_distance": stock4,
            "rack5_distance": stock4,
            "rack6_distance": stock6,
            "datetime": dt_string
            
        }
        insert_data_to_mongodb(db, data)

        time.sleep(3)

        # payload = build_payload(rack1, rack2, rack3, rack4, rack5, rack6)
        # print("[INFO] Attemping to send data")
        # post_request(payload)
        # print("[INFO] finished")

def main():
    db = connect_to_mongodb()
    setup()
    loop(db)

if __name__ == "__main__":
    main()