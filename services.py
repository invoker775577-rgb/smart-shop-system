# services.py
import os
from dotenv import load_dotenv

# Загружаем секреты из файла .env
load_dotenv()

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
        # Читаем секретный ключ из .env (имитация проверки безопасности)
        api_key = os.getenv("BANK_API_KEY")
        
        print(f"🔒 (Bank System connect with Key: {api_key}...)") # Для наглядности
        
        if user.balance >= amount:
            user.balance -= amount
            print(f"💸 ОПЛАТА: Списано {amount}$. У {user.name} осталось {user.balance}$")
            return True
        else:
            print(f"❌ ОПЛАТА: Недостаточно средств!")
            return False

class NotificationService:
    def send_sms(self, user, message):
        # Читаем email отправителя из настроек
        sender = os.getenv("SMS_SENDER_EMAIL")
        print(f"📩 SMS от {sender} для {user.name}: {message}")

print("Hello branch")        

