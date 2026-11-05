from validations import *
from storage import * 
from orders import * 


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


def print_menu():
    print("========== ORDER MANAGER ==========")
    print("1. Create order")
    print("2. Show all orders")
    print("3. Find order by ID")
    print("4. Close order")
    print("5. Show sales report")
    print("0. Exit")
    print("Choose option: ")


def user_choice():
    pass


def main():
    while True:
        user_choice = user_choice()
        match user_choice:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "0":
                break
main()


def calculation_of_discount(order):
    if order <300:
        return order , "no discount"
    if 700 > order >=300:
        return order * 0.95 , "5% discount"
    if 1500 >order <=700:
        return order * 0.9 , "10 % discount"
    else:
        return order * 0.85 , "15% discount"


