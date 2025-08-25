# OOP Project: GoldApple Cosmetics Store Simulation

## Overview
This Python project simulates a cosmetics and beauty store inspired by **GoldApple**, applying key Object-Oriented Programming (OOP) principles. The system models products, customers, brands, and orders, using abstraction, inheritance, encapsulation, polymorphism, and more to reflect real-world behavior.

---

## Team Members & Responsibilities

### 1. **Team Leader & Class/Inheritance Developer** — *Nussupkulova Aizhan*
- Coordinated the project and ensured timely completion.
- Implemented key class structures like `Product`, `Brand`, `Category`.
- Applied single, multilevel, and multiple inheritance.
- Integrated final code structure.

### 2. **Polymorphism & Encapsulation Developer** — *Adiya Amangeldi*
- Developed overridden methods like `get_details()` and `calculate_price()`.
- Applied encapsulation using private attributes and `@property` decorators.

### 3. **Error Handling & Super Method Specialist** — *Bektaeva Yenglik*
- Implemented `try-except` error handling in constructors and methods.
- Ensured the correct usage of `super()` in inherited constructors.

### 4. **Decoration & Abstraction Expert** — *Berdigaliyeva Zarina*
- Applied decorators: `@property`, `@classmethod`, `@staticmethod`.
- Created abstract base class `StoreItem` using the `abc` module.

### 5. **Documentation & Testing Specialists** — *All Members*
- *Berdigaliyeva Zarina, Adiya Amangeldi, Bektaeva Yenglik, Nussupkulova Aizhan* collaborated on testing and writing documentation.

---

## OOP Principles Implemented

### 1. **Class Implementation**
Classes used: `Product`, `Brand`, `Category`, `HairCare`, `LoyalCustomer`, `StoreItem`.

### 2. **Inheritance**
- `Product` inherits from `StoreItem`
- `HairCare` inherits from `Product`

### 3. **Multiple Inheritance**
- `LoyalCustomer` inherits from both `Customer` and `Discountable`

### 4. **Multilevel Inheritance**
- `HairCare` → `Product` → `StoreItem`

### 5. **Object Creation and Method Calls**
Objects are instantiated and used in method calls throughout the script.

### 6. **Polymorphism**
- Method overriding in `get_details()` and `calculate_price()` across subclasses

### 7. **Encapsulation**
- Private fields like `__price` and `__stock_quantity` with getters/setters

### 8. **Error Handling**
- `try-except` blocks and `raise ValueError` used to validate input

### 9. **Decoration**
- Used `@property`, `@staticmethod`, `@classmethod` decorators

### 10. **Super Method**
- `super()` used in `HairCare` constructor to invoke parent constructor

### 11. **Abstraction**
- `StoreItem` as an abstract base class with abstract methods

---

## Example Output

```python
Product added: Versace Eros
Product added: Herbal Essence Shampoo
Customer created: Alice
Order placed by Alice: 2 items totaling $75.50
```

---

## How to Run

1. Open the file `corrected_project_updated.py`
2. Run it using Python 3.x
3. Outputs will be printed to the console

---

## Files

- `corrected_project_updated.py`: Main Python file
- `README.md`: Project documentation

---

## Final Note

This project is educational and simulates realistic store behavior using Python OOP concepts, based on the structure and spirit of the GoldApple store.