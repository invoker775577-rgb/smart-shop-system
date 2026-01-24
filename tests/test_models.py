import pytest
from models import Order

# 1. Тест с ПАРАМЕТРИЗАЦИЕЙ
# Мы проверяем 3 сценария: скидка 10%, 0% и 50%
@pytest.mark.parametrize(
    "discount_percent, expected_total",
    [
        (10, 450.0),  # Если цена 500 и скидка 10% -> должно быть 450
        (0, 500.0),   # Если скидка 0% -> цена та же
        (50, 250.0),  # Если скидка 50% -> цена пополам
    ]
)
def test_order_discount(sample_order, discount_percent, expected_total):
    # sample_order прилетает из conftest.py (цена там 500)
    
    sample_order.apply_discount(discount_percent)
    
    assert sample_order.total_price == expected_total

# 2. Простой тест на проверку инициализации (использует фикстуру)
def test_product_creation(sample_product):
    assert sample_product.name == "TestPhone"
    assert sample_product.stock == 10