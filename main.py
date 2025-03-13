from product import Product
from customer import Customer
from cart import Cart
from order import Order

def main():
    products = {
        "Laptop": Product("Laptop", 15000, 5),
        "Telefon": Product("Telefon", 10000, 15),
        "Kulaklık": Product("Kulaklık", 500, 150)
    }
    
    customer = Customer("Ahmet Yılmaz", "ahmet@example.com")
    
    cart = Cart()
    
    
    cart.add_product(products["Laptop"], 2)
    cart.add_product(products["Telefon"], 1)
    
    order = Order(customer, cart)
    order.total_amount = cart.get_amount()
    order.place_order()


main()