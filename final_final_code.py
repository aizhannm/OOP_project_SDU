from abc import ABC, abstractmethod

# Abstract Base Class for Store Items
class StoreItem(ABC):
    @abstractmethod
    def get_details(self):
        pass

    @abstractmethod
    def calculate_price(self):
        pass

# Abstract Class for Person-related roles
class Person(ABC):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @abstractmethod
    def get_person_info(self):
        pass

# Brand Class
class Brand:
    def __init__(self, name, country, year_established, history):
        if not name or not country:
            raise ValueError("Brand name and country cannot be empty!")
        self.__name = name
        self.__country = country
        self.year_established = year_established
        self.__history = history

    @property
    def name(self):
        return self.__name

    @property
    def country(self):
        return self.__country

    @property
    def history(self):
        return self.__history

    @classmethod
    def from_string(cls, brand_info):
        name, country, year, history = brand_info.split(", ")
        return cls(name, country, int(year), history)

# Category Hierarchy
class Category:
    def __init__(self, name):
        self.name = name

    def get_category_info(self):
        return f"Category: {self.name}"

class WomensCare(Category):
    def __init__(self):
        super().__init__("Women's Care")

class MensCare(Category):
    def __init__(self):
        super().__init__("Men's Care")

class Cosmetics(Category):
    def __init__(self):
        super().__init__("Cosmetics")

class WomensHairCare(WomensCare):
    def __init__(self, hair_type):
        super().__init__()
        self.name = "Women's Hair Care"
        self.hair_type = hair_type

    def get_category_info(self):
        return f"Category: {self.name}, Hair Type: {self.hair_type}"

class WomensFaceCare(WomensCare):
    def __init__(self, skin_type):
        super().__init__()
        self.name = "Women's Face Care"
        self.skin_type = skin_type

    def get_category_info(self):
        return f"Category: {self.name}, Skin Type: {self.skin_type}"

class MensHairCare(MensCare):
    def __init__(self, scalp_type):
        super().__init__()
        self.name = "Men's Hair Care"
        self.scalp_type = scalp_type

    def get_category_info(self):
        return f"Category: {self.name}, Scalp Type: {self.scalp_type}"

class MensFaceCare(MensCare):
    def __init__(self, beard_friendly):
        super().__init__()
        self.name = "Men's Face Care"
        self.beard_friendly = beard_friendly

    def get_category_info(self):
        return f"Category: {self.name}, Beard Friendly: {self.beard_friendly}"

# Product Class
class Product(StoreItem):
    def __init__(self, name, price, brand, category, description, stock_quantity):
        if price <= 0:
            raise ValueError("Price must be greater than zero!")
        self.name = name
        self.price = price
        self.brand = brand
        self.category = category
        self.description = description
        self.__stock_quantity = stock_quantity

    def get_details(self):
        category_info = self.category.get_category_info()
        return (f"Product: {self.name}, Price: {self.price}, Brand: {self.brand.name}, "
                f"{category_info}, Description: {self.description}")

    def calculate_price(self):
        return self.price

    @staticmethod
    def apply_tax(price, tax_rate=0.1):
        return price * (1 + tax_rate)

    def apply_discount(self, percent):
        if percent <= 0 or percent >= 100:
            raise ValueError("Discount percent must be between 0 and 100.")
        discount = self.price * (percent / 100)
        self.price -= discount
        return self.price

# Discountable Interface
class Discountable:
    def apply_discount(self, percent):
        if percent <= 0 or percent >= 100:
            raise ValueError("Discount percent must be between 0 and 100.")
        discount = self.price * (percent / 100)
        self.price -= discount
        return self.price

# LoyalCustomer
class LoyalCustomer(Person, Discountable):
    def __init__(self, name, email, loyalty_points=0):
        super().__init__(name, email)
        self.loyalty_points = loyalty_points

    def get_person_info(self):
        return f"Name: {self.name}, Email: {self.email}"

    def get_customer_info(self):
        return f"Loyal Customer: {self.name}, Email: {self.email}, Points: {self.loyalty_points}"

# Delivery
class Delivery:
    def __init__(self, method, address, delivery_fee):
        self.method = method
        self.address = address
        self.delivery_fee = delivery_fee

    def get_delivery_info(self):
        return f"Delivery Method: {self.method}, Address: {self.address}, Fee: {self.delivery_fee}"

# Order
class Order:
    def __init__(self, customer, product, quantity, delivery):
        self.customer = customer
        self.product = product
        self.quantity = quantity
        self.delivery = delivery

    def get_order_summary(self):
        total = (self.product.calculate_price() * self.quantity) + self.delivery.delivery_fee
        return f"Order for {self.customer.name}: {self.product.name} x {self.quantity}, Total with delivery: {total}"

# Payment
class Payment:
    def __init__(self, order, method):
        self.order = order
        self.method = method

    def process_payment(self):
        print(f"Processing {self.method} payment for {self.order.customer.name}. Total amount: {(self.order.product.calculate_price() * self.order.quantity) + self.order.delivery.delivery_fee}")

# Example usage
if __name__ == "__main__":
    try:
        brand = Brand.from_string("Golden Apple, Kazakhstan, 2015, Popular online beauty store.")

        womens_hair_cat = WomensHairCare("Dry")
        womens_face_cat = WomensFaceCare("Sensitive")
        mens_hair_cat = MensHairCare("Oily")
        mens_face_cat = MensFaceCare(True)

        womens_shampoo = Product("Volume Shampoo", 3500, brand, womens_hair_cat, "For thick healthy hair", 50)
        womens_cream = Product("Hydrating Cream", 4500, brand, womens_face_cat, "Nourishing face cream", 30)
        mens_shampoo = Product("Menthol Fresh", 3000, brand, mens_hair_cat, "Cool and refreshing shampoo", 40)
        mens_facewash = Product("Beard & Skin Wash", 4000, brand, mens_face_cat, "Cleanses and nourishes", 35)

        # New test products
        extra_womens_shampoo = Product("Keratin Repair Shampoo", 4800, brand, WomensHairCare("Normal"), "Repairs damaged hair", 60)
        mens_facecream = Product("Men's Face Cream", 4200, brand, MensFaceCare(False), "Hydrating cream for men", 25)

        print(womens_shampoo.get_details())
        print(womens_cream.get_details())
        print(mens_shampoo.get_details())
        print(mens_facewash.get_details())
        print(extra_womens_shampoo.get_details())
        print(mens_facecream.get_details())

        customer = LoyalCustomer("Aizhan", "aizhan@example.com", 120)
        print(customer.get_customer_info())

        womens_cream.apply_discount(15)

        delivery = Delivery("Courier", "Almaty, Kazakhstan", 500)
        order = Order(customer, womens_cream, 2, delivery)
        print(order.get_order_summary())
        payment = Payment(order, "Card")
        payment.process_payment()

    except ValueError as e:
        print(f"Invalid input: {e}")
