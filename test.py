import json




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



def main():
    while True:
        user_choice = user_choice()
        match user_choice:
            case "1":
                pass # create_order
            case "2":
                pass # show_all_orders
            case "3":
                pass # find_order_by_id
            case "4":
                pass # close_order
            case "5":
                pass
            case "0":
                break
        



def user_choice():    
    choice = input("Enter your choice: ")
    if choice in ["1", "2", "3", "4", "5", "0"]:
        return choice
    else:
        print("Invalid choice. Please try again.")
        return user_choice()

def validate_input(message, input_type):
    while True:
        user_input = input(message).strip()
        if input_type == "num":
            if user_input.isdigit():
                return int(user_input)
            else:
                print("please enter a num")
        elif input_type == "positive_num":
            if user_input.isdigit() and int(user_input) >= 0:
                return int(user_input)
            else:
                print("please enter positive number")
        elif input_type == "str":
            if user_input.isalpha():
                return user_input
            else:
                print("please enter a string")
        elif input_type == "not_empty":
            if user_input.strip():
                return user_input
            else:
                print("error empty string")

