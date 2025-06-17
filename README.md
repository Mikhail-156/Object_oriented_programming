# ***Проект*** 
## _Объектно-ориентированное программирование_
## Описание
Этот проект направлен на реализацию объектно-ориентированного программирования (ООП) на языке Python. Включает классы управления продуктами и категориями, а также юнит-тесты для проверки работоспособности.

### Установка
Клонируйте репозиторий:
- https://github.com/Mikhail-156/Object_oriented_programming.git

## Описание классов
Созданы классы Product и Category и два класса наследников Smartphone и LawnGrass.
- Класс Product имеет атрибуты:
1. name: str
2. description: str
3. __price: float 
4. quantity: int
- Класс Category имеет атрибуты:
1. name: str
2. description: str
3. __products: list[Product]
4. category_count: int
5. product_count: int
- Класс Smartphone имеет атрибуты:
1. self.efficiency = efficiency
2. self.model = model
3. self.memory = memory
4. self.color = color
- Класс LawnGrass имеет атрибуты:
1. self.country = country
2. self.germination_period = germination_period
3. self.color = color

### Тестирование
- Написаны тесты, которые проверяют корректность инициализации объектов класса Category.
- Написаны тесты, которые проверяют корректность инициализации объектов класса Product.
- Написаны тесты, которые проверяют подсчет количества продуктов.
- Написаны тесты, которые проверяют подсчет количества категорий.
- В репозитории есть отчет о покрытии тестами.
