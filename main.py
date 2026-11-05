import json
import os
from functions import *
from validations import * 
from orders import *
from storage import *

products = [
    {"id": 1, "name": "Keyboard", "price": 120},
    {"id": 2, "name": "Mouse", "price": 80},
    {"id": 3, "name": "Monitor", "price": 900},
    {"id": 4, "name": "Headphones", "price": 200},
    {"id": 5, "name": "USB Cable", "price": 30}]

order_for_example = {
    "id": 1,
    "items": [{"product_id": 1, "quantity": 2},
              {"product_id": 3, "quantity": 1}],
    "total": 1026.0,
    "status": "OPEN"}

orders=[]
order={"id":1,"items":[],"total":0,"status":"OPEN"}



def main():
    while True:
        print_menu()
        choice = user_choice()
        match choice:
            case "1":
                create_order()
            case "2":
                show_all_orders()
            case "3":
                find_order_by_id()
            case "4":
                close_order()
            case "5":
                pass # show_sales_report 
            case "0":
                break
if __name__ == "__main__":
    main()