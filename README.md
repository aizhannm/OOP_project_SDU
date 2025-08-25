# 🛍️ OOP Cosmetics Store Project

This project is an **Object-Oriented Programming (OOP) implementation** of an **online cosmetics store management system**, created as part of the SDU University course project.  

It demonstrates core OOP principles such as **abstraction, inheritance, polymorphism, encapsulation, interfaces, static/class methods**, and real-world modeling of an e-commerce system.

---

## 📂 Project Structure
- **StoreItem (Abstract Class)** → Defines base methods for all store items.  
- **Person (Abstract Class)** → Parent class for customers.  
- **Brand** → Represents brand info with encapsulation and class methods.  
- **Category Hierarchy**  
  - `WomensCare`, `MensCare`, `Cosmetics`  
  - `WomensHairCare`, `WomensFaceCare`, `MensHairCare`, `MensFaceCare`  
- **Product (Implements StoreItem)** → Supports discounts, tax calculation, stock management.  
- **Discountable (Interface)** → Defines reusable discount logic.  
- **LoyalCustomer (Extends Person, Implements Discountable)** → Customer with loyalty points.  
- **Delivery** → Delivery info and fee.  
- **Order** → Handles order summary and total calculation.  
- **Payment** → Processes payment based on method.  

---

## 🛠 Technologies Used
- Python 3.x  
- Object-Oriented Programming concepts  
- Exception handling (`ValueError`)  
- Static & class methods  
- Abstraction with `ABC` (Abstract Base Class)  

---

## 🚀 Features
✔️ Add brands with encapsulated data  
✔️ Organize products into multiple categories (Women’s / Men’s Care)  
✔️ Calculate discounts and taxes  
✔️ Create customers with loyalty points  
✔️ Place orders and calculate totals (with delivery fee)  
✔️ Process payments  

---

## 📖 Example Usage
```python
if __name__ == "__main__":
    brand = Brand.from_string("Golden Apple, Kazakhstan, 2015, Popular online beauty store.")
    
    womens_hair_cat = WomensHairCare("Dry")
    womens_shampoo = Product("Volume Shampoo", 3500, brand, womens_hair_cat, "For thick healthy hair", 50)
    
    customer = LoyalCustomer("Aizhan", "aizhan@example.com", 120)
    print(customer.get_customer_info())
    
    delivery = Delivery("Courier", "Almaty, Kazakhstan", 500)
    order = Order(customer, womens_shampoo, 2, delivery)
    
    print(order.get_order_summary())
    payment = Payment(order, "Card")
    payment.process_payment()
