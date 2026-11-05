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





def main():
    while True:
        print_menu()
        choice = user_choice()
        match choice:
            case "1":
                create_order()
            case "2":
                pass # show_all_orders
            case "3":
                pass # find_order_by_id
            case "4":
                pass # close_order
            case "5":
                pass # show_sales_report 
            case "0":
                break
        

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


def print_products():
    print("available products:")
    for product in products:
        print(f"ID: {product['id']}, Name: {product['name']}, Price: {product['price']}")

def create_order():
    order = {"id": len(orders) + 1, "items": [], "total": 0, "status": "OPEN"}
    while True:
        print_products()
        product_id = validate_input("Enter product id or '6' to quite: ", "positive_num")
        validate_that_product_exists(product_id)
        if product_id == 6:
            break
        quantity = validate_input("how much: ", "positive_num")
        order["items"].append({"product_id": product_id, "quantity": quantity})
        product_price = next((product["price"] for product in products if product["id"] == product_id), 0)
        price_before_discount = product_price * quantity
        price_after_discount, discount_message = calculation_of_discount(price_before_discount)
        order["total"] += price_after_discount
    orders.append(order)
    print_order_price(discount_message,price_before_discount,price_after_discount)
    save_orders_to_file()


def calculation_of_discount(price_before_discount):
    if price_before_discount < 300:
        return price_before_discount, "no discount"
    elif 300 <= price_before_discount < 700:
        return price_before_discount * 0.95, "5% discount"
    elif 700 <= price_before_discount < 1500:
        return price_before_discount * 0.9, "10% discount"
    else:
        return price_before_discount * 0.85, "15% discount"


def print_order_price(discount_message, price_before_discount, price_after_discount):
    print(f" the price before discount for order id {order["id"]} is {price_before_discount}")
    print(f"the price after discount is {price_after_discount} you got {discount_message}")



def save_orders_to_file():
    with open("orders.json", "w") as file:
        json.dump(orders, file, indent=2)

def read_orders_from_file():
    try:
        with open("orders.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def validate_that_product_exists(product_id):
    for product in products:
        if product["id"] == product_id:
            return True
    return False




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
main()
print(orders)