from functions import *
from validations import * 
from orders import *
from main import *


def save_orders_to_file():
    if "orders.json" not in os.listdir():
        with open("orders.json", "w") as file:  #
            json.dump(orders, file, indent=2)
    else:
        with open("orders.json", "w") as file:
            json.dump(orders, file, indent=2)

def add_order_to_file(order):
    orders = read_orders_from_file()
    orders.append(order)
    with open("orders.json", "w") as file:
        json.dump(orders, file, indent=2)
        

def read_orders_from_file():
    try:
        with open("orders.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []