from product import Product
from product_manager import ProductManager
from cart import Cart

cart = Cart()
product_manager = ProductManager()


product_manager.add_product(Product("Slusalice", 100, 2))
product_manager.add_product(Product("SmartWatch", 150, 3))
product_manager.add_product(Product("Monitor", 200, 1))


product_manager.display_products()
print("Total inventory value:", product_manager.total_inventory_value())

for product in product_manager.products[:3]:  
    cart.add_to_cart(product)

print("Cart contents:")
cart.display_cart()
print("Total cart value:", cart.total_cart_value())