import psycopg2
import os
from dotenv import load_dotenv

# Загружаем пароли
load_dotenv()

class Database:
    def __init__(self):
        try:
            # Подключаемся к Postgres
            self.connection = psycopg2.connect(
                dbname=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT")
            )
            self.connection.autocommit = True # Включаем авто-сохранение
            self.cursor = self.connection.cursor()
            self.create_tables()
            print("✅ Успешное подключение к PostgreSQL!")
        except Exception as e:
            print(f"❌ Ошибка подключения: {e}")

    def create_tables(self):
        # Создаем таблицы (обрати внимание на типы данных)
        
        # Таблица Юзеров
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                balance NUMERIC(10, 2),
                email VARCHAR(100)
            );
        """)
            
        # Таблица Товаров
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                price NUMERIC(10, 2),
                stock INTEGER
            );
        """)
        
        print("🛠 Таблицы готовы к работе.")

    def add_user(self, name, balance, email):
        # В Postgres используем %s для безопасности!
        self.cursor.execute(
            "INSERT INTO users (name, balance, email) VALUES (%s, %s, %s)", 
            (name, balance, email)
        )
        print(f"👤 Пользователь {name} добавлен в базу.")

    def get_user(self, name):
        self.cursor.execute("SELECT * FROM users WHERE name = %s", (name,))
        return self.cursor.fetchone()

    def close(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("🔌 Соединение закрыто.")