from validations import * 
from orders import *
from storage import *
from main import * 


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
    choice = input("Enter your choice: ")
    if choice in ["1", "2", "3", "4", "5", "0"]:
        return choice
    else:
        print("Invalid choice. Please try again.")
        return user_choice()




def calculation_of_discount(price_before_discount):
    if price_before_discount < 300:
        return price_before_discount, "no discount"
    elif 300 <= price_before_discount < 700:
        return price_before_discount * 0.95, "5% discount"
    elif 700 <= price_before_discount < 1500:
        return price_before_discount * 0.9, "10% discount"
    else:
        return price_before_discount * 0.85, "15% discount"