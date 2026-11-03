class Product:
    def _init_(self, name, price):
        self._price = price
        self._name = name

    @property
    def price(self):
        return self._price
    @price.setter
    def price (self, value):
        if value < 0 :
            raise ValueError("Price cannot be negative")
        self._price = value 

product1 = Product ("Laptop", 3000)
product1.price = 90000
print (product1.discounted_price)
