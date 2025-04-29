# Class for product
class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

# Class for customer
class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.cart = {}

    # Add item to the cart
    def add_to_cart(self, product, quantity):
        if product.stock >= quantity:
            if product.product_id in self.cart:
                self.cart[product.product_id]['quantity'] += quantity
            else:
                self.cart[product.product_id] = {'product': product, 'quantity': quantity}
            product.stock -= quantity
            print(f"Added {quantity} of {product.name} to the cart.")
        else:
            print(f"Insufficient stock for {product.name}.")

    # Calculate total cost of items in the cart
    def calculate_total(self):
        total = 0
        for item in self.cart.values():
            total += item['product'].price * item['quantity']
        return total

    # Process the order
    def checkout(self):
        if self.cart:
            total_cost = self.calculate_total()
            print(f"Order processed for {self.name}. Total cost: {total_cost}")
            self.cart.clear()
        else:
            print("Cart is empty!")

# Class for managing inventory
class Inventory:
    def __init__(self):
        self.products = {}

    # Add product to the inventory
    def add_product(self, product):
        self.products[product.product_id] = product
        print(f"Added product {product.name} to inventory.")

    # Display all products
    def display_products(self):
        for product in self.products.values():
            print(f"ID: {product.product_id}, Name: {product.name}, Price: {product.price}, Stock: {product.stock}")

# Sample usage
# Create inventory and add products
inventory = Inventory()
product1 = Product(101, "Laptop", 50000, 10)
product2 = Product(102, "Smartphone", 20000, 20)
inventory.add_product(product1)
inventory.add_product(product2)

# Display available products
inventory.display_products()

# Create customer and shop
customer = Customer(1, "Anurag")
customer.add_to_cart(product1, 2)
customer.add_to_cart(product2, 3)

# Display total and process order
print(f"Total cost: {customer.calculate_total()}")
customer.checkout()

# Display inventory after the transaction
inventory.display_products()