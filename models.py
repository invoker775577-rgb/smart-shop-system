# models.py
# Здесь мы храним "Модели" - описание наших данных

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

class User:
    def __init__(self, name, balance, email):
        self.name = name
        self.balance = balance
        self.email = email

class Order:
    def __init__(self, user, product, quantity):
        self.user = user
        self.product = product
        self.quantity = quantity
        self.status = "Создан"
        self.total_price = product.price * quantity