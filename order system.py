class Product:
    def __init__(self, product_id, name, price, stock, category):
        if name.strip() == "":
            raise ValueError("Product name cannot be empty.")

        if category.strip() == "":
            raise ValueError("Category cannot be empty.")

        if price <= 0:
            raise ValueError("Price must be greater than 0.")

        if stock < 0:
            raise ValueError("Stock cannot be negative.")

        self.product_id = product_id
        self.name = name
        self._price = price
        self._stock = stock
        self.category = category

    @property
    def price(self):
        return self._price

    @property
    def stock(self):
        return self._stock

    def increase_stock(self, quantity):
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        self._stock += quantity

    def reduce_stock(self, quantity):
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        if quantity > self._stock:
            raise ValueError("Not enough stock.")

        self._stock -= quantity

    def details(self):
        return (
            f"ID: {self.product_id} | "
            f"{self.name} | "
            f"₦{self.price:.2f} | "
            f"Stock: {self.stock} | "
            f"Category: {self.category}"
        )


class Customer:
    def __init__(self, customer_id, name, email, phone):
        if name.strip() == "":
            raise ValueError("Customer name cannot be empty.")

        if email.strip() == "":
            raise ValueError("Email cannot be empty.")

        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self._orders = []

    @property
    def orders(self):
        return tuple(self._orders)

    def add_order(self, order):
        self._orders.append(order)

    def details(self):
        return (
            f"ID: {self.customer_id} | "
            f"Name: {self.name} | "
            f"Email: {self.email} | "
            f"Phone: {self.phone}"
        )


class Order:
    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        self.ordered_products = {}
        self.status = "Pending"

    def add_product(self, product, quantity):
        if self.status in ["Completed", "Cancelled"]:
            raise ValueError("This order cannot be changed.")

        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        product.reduce_stock(quantity)

        if product in self.ordered_products:
            self.ordered_products[product] += quantity
        else:
            self.ordered_products[product] = quantity

    def remove_product(self, product):
        if self.status in ["Completed", "Cancelled"]:
            raise ValueError("This order cannot be changed.")

        if product not in self.ordered_products:
            raise ValueError("Product is not in this order.")

        quantity = self.ordered_products[product]

        product.increase_stock(quantity)

        del self.ordered_products[product]

    def calculate_total(self):
        total = 0

        for product, quantity in self.ordered_products.items():
            total += product.price * quantity

        return total

    def get_order_summary(self):
        summary = f"\nOrder ID: {self.order_id}\n"
        summary += f"Customer: {self.customer.name}\n"
        summary += f"Status: {self.status}\n"

        if len(self.ordered_products) == 0:
            summary += "No products in order.\n"
        else:
            for product, quantity in self.ordered_products.items():
                subtotal = product.price * quantity

                summary += (
                    f"{product.name} x {quantity} "
                    f"= ₦{subtotal:.2f}\n"
                )

            summary += f"Total: ₦{self.calculate_total():.2f}\n"

        return summary

    def confirm(self):
        if self.status != "Pending":
            raise ValueError("Only pending orders can be confirmed.")

        if len(self.ordered_products) == 0:
            raise ValueError("Cannot confirm an empty order.")

        self.status = "Confirmed"

    def complete(self):
        if self.status != "Confirmed":
            raise ValueError(
                "Only confirmed orders can be completed."
            )

        self.status = "Completed"

    def cancel_order(self):
        if self.status == "Completed":
            raise ValueError(
                "Completed orders cannot be cancelled."
            )

        if self.status == "Cancelled":
            raise ValueError(
                "Order is already cancelled."
            )

        for product, quantity in self.ordered_products.items():
            product.increase_stock(quantity)

        self.status = "Cancelled"


class Store:
    def __init__(self):
        self.products = {}
        self.customers = {}
        self.orders = {}

        self.low_stock_limit = 5

    def add_product(self, product):
        if product.product_id in self.products:
            raise ValueError("Product ID already exists.")

        self.products[product.product_id] = product

    def remove_product(self, product_id):
        if product_id not in self.products:
            raise ValueError("Product not found.")

        product = self.products[product_id]

        for order in self.orders.values():
            if order.status in ["Pending", "Confirmed"]:
                if product in order.ordered_products:
                    raise ValueError(
                        "Product is in an active order."
                    )

        del self.products[product_id]

    def find_product(self, product_id):
        if product_id not in self.products:
            raise ValueError("Product not found.")

        return self.products[product_id]

    def register_customer(self, customer):
        if customer.customer_id in self.customers:
            raise ValueError("Customer ID already exists.")

        self.customers[customer.customer_id] = customer

    def find_customer(self, customer_id):
        if customer_id not in self.customers:
            raise ValueError("Customer not found.")

        return self.customers[customer_id]

    def create_order(self, customer_id):
        customer = self.find_customer(customer_id)

        order_id = "O" + str(len(self.orders) + 1)

        order = Order(order_id, customer)

        self.orders[order_id] = order

        customer.add_order(order)

        return order

    def find_order(self, order_id):
        if order_id not in self.orders:
            raise ValueError("Order not found.")

        return self.orders[order_id]

    def list_products(self):
        if len(self.products) == 0:
            print("No products available.")
        else:
            for product in self.products.values():
                print(product.details())

    def list_customer_orders(self, customer_id):
        customer = self.find_customer(customer_id)

        if len(customer.orders) == 0:
            print("Customer has no orders.")
        else:
            for order in customer.orders:
                print(order.get_order_summary())

    def reports(self):
        print("\n--- STORE REPORTS ---")

        inventory_value = 0

        for product in self.products.values():
            inventory_value += product.price * product.stock

        print(
            f"Total inventory value: "
            f"₦{inventory_value:.2f}"
        )

        print("\nLow stock products:")

        found_low_stock = False

        for product in self.products.values():
            if product.stock < self.low_stock_limit:
                print(product.details())
                found_low_stock = True

        if not found_low_stock:
            print("None")

        print("\nMost expensive product:")

        if len(self.products) > 0:
            expensive = max(
                self.products.values(),
                key=lambda product: product.price
            )

            print(
                f"{expensive.name} - "
                f"₦{expensive.price:.2f}"
            )
        else:
            print("None")

        print("\nProducts by category:")

        categories = {}

        for product in self.products.values():

            if product.category not in categories:
                categories[product.category] = []

            categories[product.category].append(
                product.name
            )

        if len(categories) == 0:
            print("None")
        else:
            for category, products in categories.items():
                print(
                    category + ": " +
                    ", ".join(products)
                )

        completed_sales = 0

        customer_spending = {}

        for order in self.orders.values():

            if order.status == "Completed":

                total = order.calculate_total()

                completed_sales += total

                customer_id = order.customer.customer_id

                if customer_id not in customer_spending:
                    customer_spending[customer_id] = 0

                customer_spending[customer_id] += total

        print(
            f"\nTotal completed sales: "
            f"₦{completed_sales:.2f}"
        )

        print("\nCustomer spending:")

        if len(customer_spending) == 0:
            print("None")
        else:
            for customer_id, amount in customer_spending.items():
                print(
                    f"{customer_id}: "
                    f"₦{amount:.2f}"
                )

        product_frequency = {}

        for order in self.orders.values():

            if order.status != "Cancelled":

                for product, quantity in order.ordered_products.items():

                    if product.name not in product_frequency:
                        product_frequency[product.name] = 0

                    product_frequency[product.name] += quantity

        print("\nMost frequently ordered products:")

        if len(product_frequency) == 0:
            print("None")
        else:
            sorted_products = sorted(
                product_frequency.items(),
                key=lambda item: item[1],
                reverse=True
            )

            for name, quantity in sorted_products:
                print(
                    f"{name}: {quantity}"
                )


store = Store()


while True:

    print("\n===== E-COMMERCE ORDER MANAGEMENT =====")

    print("1. Add product")
    print("2. View all products")
    print("3. Search for product")
    print("4. Register customer")
    print("5. Create order")
    print("6. Add product to order")
    print("7. Remove product from order")
    print("8. View order summary")
    print("9. Confirm order")
    print("10. Complete order")
    print("11. Cancel order")
    print("12. View customer order history")
    print("13. View store reports")
    print("14. Exit")

    choice = input("Enter your choice: ")

    try:

        if choice == "1":

            product_id = input("Enter product ID: ")
            name = input("Enter product name: ")

            price = float(input("Enter price: "))
            stock = int(input("Enter stock: "))

            category = input("Enter category: ")

            product = Product(
                product_id,
                name,
                price,
                stock,
                category
            )

            store.add_product(product)

            print("Product added successfully.")

        elif choice == "2":

            store.list_products()

        elif choice == "3":

            product_id = input("Enter product ID: ")

            product = store.find_product(product_id)

            print(product.details())

        elif choice == "4":

            customer_id = input("Enter customer ID: ")
            name = input("Enter customer name: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")

            customer = Customer(
                customer_id,
                name,
                email,
                phone
            )

            store.register_customer(customer)

            print("Customer registered successfully.")

        elif choice == "5":

            customer_id = input("Enter customer ID: ")

            order = store.create_order(customer_id)

            print(
                f"Order created successfully. "
                f"Order ID: {order.order_id}"
            )

        elif choice == "6":

            order_id = input("Enter order ID: ")
            product_id = input("Enter product ID: ")

            quantity = int(
                input("Enter quantity: ")
            )

            order = store.find_order(order_id)

            product = store.find_product(product_id)

            order.add_product(
                product,
                quantity
            )

            print("Product added to order.")

        elif choice == "7":

            order_id = input("Enter order ID: ")
            product_id = input("Enter product ID: ")

            order = store.find_order(order_id)

            product = store.find_product(product_id)

            order.remove_product(product)

            print("Product removed from order.")

        elif choice == "8":

            order_id = input("Enter order ID: ")

            order = store.find_order(order_id)

            print(order.get_order_summary())

        elif choice == "9":

            order_id = input("Enter order ID: ")

            order = store.find_order(order_id)

            order.confirm()

            print("Order confirmed.")

        elif choice == "10":

            order_id = input("Enter order ID: ")

            order = store.find_order(order_id)

            order.complete()

            print("Order completed.")

        elif choice == "11":

            order_id = input("Enter order ID: ")

            order = store.find_order(order_id)

            order.cancel_order()

            print("Order cancelled. Stock restored.")

        elif choice == "12":

            customer_id = input("Enter customer ID: ")

            store.list_customer_orders(
                customer_id
            )

        elif choice == "13":

            store.reports()

        elif choice == "14":

            print("Goodbye!")
            break

        else:

            print("Invalid choice. Enter 1-14.")

    except ValueError as error:

        print("Error:", error)

    except Exception as error:

        print("Something went wrong:", error)