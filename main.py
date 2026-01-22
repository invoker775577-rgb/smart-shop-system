# main.py

# 1. ИМПОРТЫ (Связываем файлы)
# from <имя_файла> import <имя_класса>
from models import Product, User, Order
from services import InventoryService, PaymentService, NotificationService

# 2. ИНИЦИАЛИЗАЦИЯ
warehouse = InventoryService()
bank = PaymentService()
notifier = NotificationService()

# 3. ДАННЫЕ
iphone = Product("iPhone 15", 1000, 5)
ivan = User("Ivan", 2500, "ivan@gmail.com")

print("--- ЗАПУСК СИСТЕМЫ ---")

# 4. ЛОГИКА
wanted_qty = 2
order = Order(ivan, iphone, wanted_qty)

# Проверяем наличие
if warehouse.check_stock(iphone, wanted_qty):
    # Пробуем оплатить
    if bank.process_payment(ivan, order.total_price):
        # Списываем и уведомляем
        warehouse.decrease_stock(iphone, wanted_qty)
        notifier.send_sms(ivan, "Оплата прошла успешно!")
    else:
        print("Ошибка оплаты")
else:
    print("Товара нет на складе")
