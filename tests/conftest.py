import pytest

from src.categories import Category
from src.lawngrass import LawnGrass
from src.products import Product
from src.smartphone import Smartphone


@pytest.fixture
def fixture_product() -> Product:
    """Фикстура продукт"""

    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def fixture_product_1() -> Product:
    """Фикстура продукт"""
    return Product("Xiaomi Redmi Note 11", "512GB, Черный цвет, 200MP камера", 31000.0, 5)


@pytest.fixture
def fixture_category() -> Category:
    """Фикстура категории"""
    product_1 = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product_2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product_3 = Product("Xiaomi Redmi Note 11", "256GB, Серый цвет, 200MP камера", 31000.0, 5)
    return Category("Смартфоны", "Смартфоны, как средство связи", [product_1, product_2, product_3])


@pytest.fixture
def fixture_smartphone() -> Smartphone:
    """Фикстура продукт"""
    product_1 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")
    return product_1


@pytest.fixture
def fixture_lawnGrass() -> LawnGrass:
    """Фикстура продукт"""
    product_1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    return product_1

@pytest.fixture
def fixture_product_2():
    product_1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    product_2 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")
    return product_1, product_2
