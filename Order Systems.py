# # 1. PRODUCT CLASS
# class Product:

#     def __init__(self, product_id, name, price, stock, category):

#         if name == "":
#             raise ValueError("Name cannot be empty")

#         if category == "":
#             raise ValueError("Category cannot be empty")

#         if price <= 0:
#             raise ValueError("Price must be greater than 0")

#         if stock < 0:
#             raise ValueError("Stock cannot be negative")

#         self.product_id = product_id
#         self.name = name
#         self._price = price
#         self._stock = stock
#         self.category = category

#     @property
#     def price(self):
#         return self._price

#     @price.setter
#     def price(self, value):

#         if value <= 0:
#             raise ValueError("Price must be greater than 0")

#         self._price = value

#     @property
#     def stock(self):
#         return self._stock

#     @stock.setter
#     def stock(self, value):

#         if value < 0:
#             raise ValueError("Stock cannot be negative")

#         self._stock = value

#     def increase_stock(self, quantity):

#         if quantity <= 0:
#             raise ValueError("Quantity must be positive")

#         self._stock += quantity

#     def reduce_stock(self, quantity):

#         if quantity <= 0:
#             raise ValueError("Quantity must be positive")

#         if quantity > self._stock:
#             raise ValueError("Not enough stock")

#         self._stock -= quantity

#     def details(self):

#         return (
#             self.product_id + " | " +
#             self.name + " | ₦" +
#             str(self.price) + " | Stock: " +
#             str(self.stock) + " | " +
#             self.category
#         )

# # 2. CUSTOMER CLASS

# class Customer:

#     def __init__(self, customer_id, name, email, phone):

#         if name == "":
#             raise ValueError("Name cannot be empty")

#         if email == "":
#             raise ValueError("Email cannot be empty")

#         self.customer_id = customer_id
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.orders = []

#     def details(self):

#         return (
#             self.customer_id + " | " +
#             self.name + " | " +
#             self.email + " | " +
#             self.phone
#         )

#     def add_order(self, order):

#         self.orders.append(order)

#     def order_history(self):

#         return self.orders

# # 3. ORDER CLASS

# class Order:

#     def __init__(self, order_id, customer):

#         self.order_id = order_id
#         self.customer = customer
#         self.ordered_products = {}
#         self.status = "Pending"

#     def add_product(self, product, quantity):

#         if self.status == "Completed" or self.status == "Cancelled":
#             raise ValueError("Cannot add to this order")

#         if type(quantity) != int or quantity <= 0:
#             raise ValueError("Quantity must be a positive integer")

#         if quantity > product.stock:
#             raise ValueError("Not enough stock")

#         product.reduce_stock(quantity)

#         if product.product_id in self.ordered_products:

#             self.ordered_products[product.product_id]["quantity"] += quantity

#         else:

#             self.ordered_products[product.product_id] = {
#                 "product": product,
#                 "quantity": quantity
#             }

#     def remove_product(self, product_id):

#         if self.status == "Completed" or self.status == "Cancelled":
#             raise ValueError("Cannot remove from this order")

#         if product_id not in self.ordered_products:
#             raise ValueError("Product is not in the order")

#         item = self.ordered_products[product_id]

#         product = item["product"]
#         quantity = item["quantity"]

#         product.increase_stock(quantity)

#         del self.ordered_products[product_id]

#     def total(self):

#         total = 0

#         for item in self.ordered_products.values():

#             total += item["product"].price * item["quantity"]

#         return total

#     def summary(self):

#         print("\nOrder ID:", self.order_id)
#         print("Customer:", self.customer.name)
#         print("Status:", self.status)

#         for item in self.ordered_products.values():

#             product = item["product"]
#             quantity = item["quantity"]

#             print(
#                 product.name,
#                 "x",
#                 quantity,
#                 "=",
#                 "₦" + str(product.price * quantity)
#             )

#         print("Total: ₦" + str(self.total()))

#     def confirm(self):

#         if self.status != "Pending":
#             raise ValueError("Only pending orders can be confirmed")

#         if len(self.ordered_products) == 0:
#             raise ValueError("Cannot confirm an empty order")

#         self.status = "Confirmed"

#     def complete(self):

#         if self.status != "Confirmed":
#             raise ValueError("Only confirmed orders can be completed")

#         self.status = "Completed"

#     def cancel(self):

#         if self.status == "Completed":
#             raise ValueError("Completed orders cannot be cancelled")

#         if self.status == "Cancelled":
#             raise ValueError("Order is already cancelled")

#         for item in self.ordered_products.values():

#             product = item["product"]
#             quantity = item["quantity"]

#             product.increase_stock(quantity)

#         self.status = "Cancelled"

# # 4. STORE CLASS

# class Store:

#     def __init__(self):

#         self.products = {}
#         self.customers = {}
#         self.orders = {}

#     def add_product(self, product):

#         if product.product_id in self.products:
#             raise ValueError("Product ID already exists")

#         self.products[product.product_id] = product

#     def remove_product(self, product_id):

#         if product_id not in self.products:
#             raise ValueError("Product not found")

#         del self.products[product_id]

#     def find_product(self, product_id):

#         if product_id not in self.products:
#             raise ValueError("Product not found")

#         return self.products[product_id]

#     def register_customer(self, customer):

#         if customer.customer_id in self.customers:
#             raise ValueError("Customer ID already exists")

#         self.customers[customer.customer_id] = customer

#     def find_customer(self, customer_id):

#         if customer_id not in self.customers:
#             raise ValueError("Customer not found")

#         return self.customers[customer_id]

#     def create_order(self, order_id, customer_id):

#         if order_id in self.orders:
#             raise ValueError("Order ID already exists")

#         customer = self.find_customer(customer_id)

#         order = Order(order_id, customer)

#         self.orders[order_id] = order

#         customer.add_order(order)

#         return order

#     def find_order(self, order_id):

#         if order_id not in self.orders:
#             raise ValueError("Order not found")

#         return self.orders[order_id]

#     def list_products(self):

#         for product in self.products.values():

#             print(product.details())

#     def list_customer_orders(self, customer_id):

#         customer = self.find_customer(customer_id)

#         for order in customer.orders:

#             print(
#                 order.order_id,
#                 "-",
#                 order.status,
#                 "- ₦" + str(order.total())
#             )

#     def reports(self, low_stock):

#         print("\nInventory value:")

#         inventory_value = 0

#         for product in self.products.values():

#             inventory_value += product.price * product.stock

#         print("₦" + str(inventory_value))

#         print("\nLow stock products:")

#         for product in self.products.values():

#             if product.stock < low_stock:

#                 print(product.name, "-", product.stock)

#         print("\nMost expensive product:")

#         if len(self.products) > 0:

#             expensive = list(self.products.values())[0]

#             for product in self.products.values():

#                 if product.price > expensive.price:

#                     expensive = product

#             print(expensive.name, "-", expensive.price)

#         print("\nProducts by category:")

#         categories = {}

#         for product in self.products.values():

#             if product.category not in categories:

#                 categories[product.category] = []

#             categories[product.category].append(product.name)

#         for category in categories:

#             print(
#                 category,
#                 ":",
#                 ", ".join(categories[category])
#             )

#         print("\nCompleted sales:")

#         sales = 0

#         for order in self.orders.values():

#             if order.status == "Completed":

#                 sales += order.total()

#         print("₦" + str(sales))

#         print("\nCustomer spending:")

#         for customer in self.customers.values():

#             spending = 0

#             for order in customer.orders:

#                 if order.status == "Completed":

#                     spending += order.total()

#             print(
#                 customer.name,
#                 "- ₦" + str(spending)
#             )

#         print("\nMost frequently ordered products:")

#         product_count = {}

#         for order in self.orders.values():

#             for item in order.ordered_products.values():

#                 product = item["product"]
#                 quantity = item["quantity"]

#                 if product.product_id not in product_count:

#                     product_count[product.product_id] = 0

#                 product_count[product.product_id] += quantity

#         for product_id in product_count:

#             print(
#                 self.products[product_id].name,
#                 "-",
#                 product_count[product_id]
#             )

# # 5. MENU

# store = Store()

# while True:

#     print("\n1. Add product")
#     print("2. View products")
#     print("3. Search product")
#     print("4. Register customer")
#     print("5. Create order")
#     print("6. Add product to order")
#     print("7. Remove product from order")
#     print("8. View order summary")
#     print("9. Confirm order")
#     print("10. Complete order")
#     print("11. Cancel order")
#     print("12. Customer order history")
#     print("13. Store reports")
#     print("14. Exit")

#     choice = input("Choose: ")

#     try:

#         if choice == "1":

#             product_id = input("Product ID: ")
#             name = input("Product name: ")
#             price = float(input("Price: "))
#             stock = int(input("Stock: "))
#             category = input("Category: ")

#             product = Product(
#                 product_id,
#                 name,
#                 price,
#                 stock,
#                 category
#             )

#             store.add_product(product)

#             print("Product added")
#         elif choice == "2":

#             store.list_products()
#         elif choice == "3":

#             search = input("Search: ").lower()

#             found = False

#             for product in store.products.values():

#                 if (
#                     search == product.product_id.lower()
#                     or search in product.name.lower()
#                 ):

#                     print(product.details())

#                     found = True

#             if found == False:

#                 print("Product not found")
#         elif choice == "4":

#             customer_id = input("Customer ID: ")
#             name = input("Name: ")
#             email = input("Email: ")
#             phone = input("Phone: ")

#             customer = Customer(
#                 customer_id,
#                 name,
#                 email,
#                 phone
#             )

#             store.register_customer(customer)

#             print("Customer registered")
#         elif choice == "5":

#             order_id = input("Order ID: ")
#             customer_id = input("Customer ID: ")

#             store.create_order(
#                 order_id,
#                 customer_id
#             )

#             print("Order created")
#         elif choice == "6":

#             order_id = input("Order ID: ")
#             product_id = input("Product ID: ")
#             quantity = int(input("Quantity: "))

#             order = store.find_order(order_id)
#             product = store.find_product(product_id)

#             order.add_product(
#                 product,
#                 quantity
#             )

#             print("Product added to order")
#         elif choice == "7":

#             order_id = input("Order ID: ")
#             product_id = input("Product ID: ")

#             order = store.find_order(order_id)

#             order.remove_product(product_id)

#             print("Product removed")
#         elif choice == "8":

#             order_id = input("Order ID: ")

#             order = store.find_order(order_id)

#             order.summary()
#         elif choice == "9":

#             order_id = input("Order ID: ")

#             order = store.find_order(order_id)

#             order.confirm()

#             print("Order confirmed")
#         elif choice == "10":

#             order_id = input("Order ID: ")

#             order = store.find_order(order_id)

#             order.complete()

#             print("Order completed")
#         elif choice == "11":

#             order_id = input("Order ID: ")

#             order = store.find_order(order_id)

#             order.cancel()

#             print("Order cancelled")
#         elif choice == "12":

#             customer_id = input("Customer ID: ")

#             store.list_customer_orders(
#                 customer_id
#             )
#         elif choice == "13":

#             low_stock = int(
#                 input("Low stock limit: ")
#             )

#             store.reports(low_stock)
#         elif choice == "14":

#             print("Goodbye")

#             break
#         else:

#             print("Invalid choice")

#     except ValueError as error:

#         print("Error:", error)