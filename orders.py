from functions import *
from validations import * 
from storage import *
from main import * 

def create_order():
    order = {"id": len(read_orders_from_file()) + 1, "items": [], "total": 0, "status": "OPEN"}
    while True:
        print_products()
        product_id = validate_input("Enter product id or '6' to quite: ", "positive_num")
        if not validate_that_product_exists(product_id):
            print("Product does not exist. Please try again.")
            continue
        if product_id == 6:
            break
        quantity = validate_input("how much: ", "positive_num")
        order["items"].append({"product_id": product_id, "quantity": quantity})
        product_price = next((product["price"] for product in products if product["id"] == product_id), 0)
        price_before_discount = product_price * quantity
        price_after_discount, discount_message = calculation_of_discount(price_before_discount)
        order["total"] += price_after_discount
    if order["items"] == []:
        print("No items were added to the order. Order not created.")
        return
    print_order_price(discount_message,price_before_discount,price_after_discount)
    orders.append(order)
    add_order_to_file(order)


def print_order_price(discount_message, price_before_discount, price_after_discount):
    print(f" the price before discount for order id {order["id"]} is {price_before_discount}")
    print(f"the price after discount is {price_after_discount} you got {discount_message}")


def show_all_orders():
    read_orders = read_orders_from_file()
    if not read_orders:
        print("No orders found.")
    else:
        for order in read_orders:
            print(f"ordr ID: {order['id']},total: {order['total']},status: {order['status']}")
            for item in order['items']:
                print(f"  Product ID: {item['product_id']}, quantity: {item['quantity']}")

def find_order_by_id():
    not_found = True
    while not_found:
        order_id = validate_input("please enter id to sherch: ","positive_num")
        read_orders = read_orders_from_file()
        if not read_orders:
            return("No orders found.")
        else:
            for order in read_orders:
                if order["id"] == order_id:
                    print(f"Order ID: {order['id']}, total: {order['total']}, status: {order['status']}")
                    for item in order['items']:
                        print(f"  Product ID: {item['product_id']}, quantity: {item['quantity']}")
                        not_found = False
                    break
            if not_found:
                    print(f"Order ID: {order_id} not found.")
                    not_found= input("want to try again?: ").strip().lower() == 'y'
                    continue

def close_order():
    order_id = validate_input("please enter id to close: ","positive_num")
    read_orders = read_orders_from_file()
    if not read_orders:
        print("No orders found.")
    else:
        for order in read_orders:
            if order["id"] == order_id:
                if order["status"] == "CLOSED":
                    print(f"Order ID: {order_id} is already closed.")
                else:
                    order["status"] = "CLOSED"
                    print(f"Order ID: {order_id} has been closed.")
                with open("orders.json", "w") as file:
                    json.dump(read_orders, file, indent=2)
                return
        print(f"Order ID: {order_id} not found.")

def print_products():
    print("available products:")
    for product in products:
        print(f"ID: {product['id']}, Name: {product['name']}, Price: {product['price']}")