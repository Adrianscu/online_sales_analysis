from product import Product
from product_manager import ProductManager

pm = ProductManager()
pm.add_product(Product("Laptop", 3000, 5))
pm.add_product(Product("Mouse", 150, 10))
pm.add_product(Product("Keyboard", 400, 7))

pm.display_products()
print(f"Total inventory value: {pm.total_inventory_value()}")