import pytest
from models import User, Product, Order

# Эта фикстура создает тестового юзера
# scope="function" значит, что для каждого теста будет создаваться НОВЫЙ юзер
@pytest.fixture(scope="function")
def sample_user():
    return User(name="TestUser", balance=1000.0, email="test@example.com")

# Эта фикстура создает тестовый товар
@pytest.fixture(scope="function")
def sample_product():
    return Product(name="TestPhone", price=500.0, stock=10)

# Эта фикстура создает заказ. Обрати внимание: она запрашивает ДРУГИЕ фикстуры!
@pytest.fixture(scope="function")
def sample_order(sample_user, sample_product):
    return Order(user=sample_user, product=sample_product, quantity=1)