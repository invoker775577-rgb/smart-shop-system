# services.py
# Здесь живет бизнес-логика. 

class InventoryService:
    def check_stock(self, product, quantity):
        if product.stock >= quantity:
            return True
        else:
            print(f"❌ СКЛАД: Ошибка! Товара {product.name} не хватает.")
            return False

    def decrease_stock(self, product, quantity):
        product.stock -= quantity
        print(f"📦 СКЛАД: Товар {product.name} выдан. Остаток: {product.stock}")

class PaymentService:
    def process_payment(self, user, amount):
        if user.balance >= amount:
            user.balance -= amount
            print(f"💸 ОПЛАТА: Списано {amount}$. У {user.name} осталось {user.balance}$")
            return True
        else:
            print(f"❌ ОПЛАТА: Недостаточно средств! Нужно {amount}, а есть {user.balance}")
            return False

class NotificationService:
    def send_sms(self, user, message):
        print(f"📩 SMS для {user.name} ({user.email}): {message}")