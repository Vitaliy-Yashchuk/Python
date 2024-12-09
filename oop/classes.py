class Order:

    # static field
    initial_number = 1000

    # constructor
    def __init__(self, title, price, discount):
        self.name = title
        self.__price = price
        self.discount = discount

        self.number = Order.initial_number
        Order.initial_number += 1

    # destructor - invokes when garbage collected
    def __del__(self):
        # clear unmanaged resources
        print(f"--- Deleting unmanaged resources ({self.number}) ---")

    def show_info(self):
        print(f"Product info: {self.name} - {self.price}$")

    # getter & setter
    def getPrice(self):
        return self.price

    def setPrice(self, value):
        self.price = value

    # properties
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value >= 0:
            self.__price = value

    # override base str conversion
    def __str__(self) -> str:
        return f"#{self.number}: {self.name} - {self.price}$"


order1 = Order("Marshall Major V", 150, 5)
order2 = Order("Xiaomi Redmi 10", 320, 0)
order3 = Order("Apple Vision Pro", 3500, 2)

order2.setPrice(279)
print(f"New price: {order2.getPrice()}")

order2.price = 189
order2.price = -120
print(f"New price: {order2.price}")

order1.show_info()

print(order1)
print(order2)
print(order3)