import pytest
from services import InventoryService

# Создаем сервис склада
@pytest.fixture
def warehouse():
    return InventoryService()

def test_check_stock_success(warehouse, sample_product):
    # Пытаемся взять 5 штук (на складе 10)
    result = warehouse.check_stock(sample_product, 5)
    assert result is True

def test_check_stock_fail(warehouse, sample_product):
    # Пытаемся взять 20 штук (на складе 10)
    result = warehouse.check_stock(sample_product, 20)
    assert result is False

def test_decrease_stock(warehouse, sample_product):
    # Списываем 3 штуки
    warehouse.decrease_stock(sample_product, 3)
    # Проверяем, что осталось 7
    assert sample_product.stock == 7