# main.py
from database import Database
from models import User, Product, Order
from services import InventoryService, PaymentService, NotificationService

def run_app():
    # 1. Инициализация (Подключаем все сервисы)
    print("🚀 Запуск системы Smart Shop...")
    db = Database()
    warehouse = InventoryService()
    bank = PaymentService()
    notifier = NotificationService()

    # 2. ПОДГОТОВКА ДАННЫХ (Seed Data)
    # Давай создадим тестового юзера и товар в БД, если их там нет
    # (В реальном проекте это делается через админку, но нам нужно для теста)
    
    # Добавляем товар (через прямой SQL, т.к. метода add_product у нас пока нет)
    # Проверяем, есть ли товар, чтобы не дублировать
    db.cursor.execute("SELECT * FROM products WHERE name = %s", ("Gaming Laptop",))
    if not db.cursor.fetchone():
        db.cursor.execute("INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)", 
                          ("Gaming Laptop", 1500.00, 10))
        db.connection.commit()
        print("🛠 Тестовый товар создан в БД.")

    # Добавляем юзера (используем наш метод)
    # Проверяем, есть ли юзер
    if not db.get_user("Ivan_CEO"):
        db.add_user("Ivan_CEO", 5000.00, "ivan@ceo.com")

    # 3. ЭМУЛЯЦИЯ ПОКУПКИ (Сценарий)
    print("\n--- НАЧИНАЕМ СЦЕНАРИЙ ПОКУПКИ ---")

    # ШАГ А: Загружаем данные из БАЗЫ в Python-объекты (Mapping)
    # Получаем кортеж из БД: (id, name, price, stock)
    db.cursor.execute("SELECT * FROM products WHERE name = %s", ("Gaming Laptop",))
    prod_data = db.cursor.fetchone()
    # Создаем объект Product из данных БД
    laptop = Product(name=prod_data[1], price=float(prod_data[2]), stock=prod_data[3])

    # Получаем кортеж из БД: (id, name, balance, email)
    user_data = db.get_user("Ivan_CEO")
    # Создаем объект User из данных БД
    ivan = User(name=user_data[1], balance=float(user_data[2]), email=user_data[3])

    print(f"👤 Клиент: {ivan.name} | Баланс: {ivan.balance}")
    print(f"💻 Товар: {laptop.name} | Цена: {laptop.price} | На складе: {laptop.stock}")

    # ШАГ Б: Пытаемся купить
    wanted_qty = 1
    order = Order(ivan, laptop, wanted_qty)

    # Логика Микросервисов
    if warehouse.check_stock(laptop, wanted_qty):
        
        if bank.process_payment(ivan, order.total_price):
            # Если оплата прошла успешно:
            
            # 1. Обновляем объект товара (в памяти)
            warehouse.decrease_stock(laptop, wanted_qty)
            
            # 2. Уведомляем
            notifier.send_sms(ivan, f"Вы купили {laptop.name}!")

            # 3. САМОЕ ВАЖНОЕ: СОХРАНЯЕМ ИЗМЕНЕНИЯ В БД (Persistence)
            print("\n💾 Сохраняем изменения в PostgreSQL...")
            
            # Обновляем баланс юзера
            db.cursor.execute("UPDATE users SET balance = %s WHERE name = %s", 
                              (ivan.balance, ivan.name))
            
            # Обновляем остаток товара
            db.cursor.execute("UPDATE products SET stock = %s WHERE name = %s", 
                              (laptop.stock, laptop.name))
            
            db.connection.commit() # Фиксируем сделку
            print("✅ Данные в базе обновлены успешно!")

        else:
            print("❌ Оплата не прошла.")
    else:
        print("❌ Товара нет на складе.")

    # Закрываем соединение
    db.close()

if __name__ == "__main__":
    run_app()