# Задание 4: Класс Dog

class Dog:
    """Класс для представления собаки"""
    
    def __init__(self, name=None, breed=None, age=None):
        """Инициализация собаки (все атрибуты опциональны)"""
        self._name = name
        self._breed = breed
        self._age = age
    
    # Геттеры (для просмотра значений)
    def get_name(self):
        return self._name
    
    def get_breed(self):
        return self._breed
    
    def get_age(self):
        return self._age
    
    # Сеттеры (для изменения значений)
    def set_name(self, name):
        self._name = name
    
    def set_breed(self, breed):
        self._breed = breed
    
    def set_age(self, age):
        if age is not None and age < 0:
            raise ValueError("Возраст не может быть отрицательным")
        self._age = age
    
    def __str__(self):
        return f"Dog(name={self._name}, breed={self._breed}, age={self._age})"


print("=" * 50)
print("ЗАДАНИЕ 4: Класс Dog")
print("=" * 50)

dog1 = Dog("Шарик", "Дворняга", 5)
print(f"Собака 1: {dog1}")

dog2 = Dog("Мурка")
print(f"Собака 2: {dog2}")

print("\nИзменение атрибутов:")
dog2.set_breed("Лабрадор")
dog2.set_age(3)
print(f"После изменения: {dog2}")

print("\nПросмотр атрибутов:")
print(f"Имя: {dog2.get_name()}")
print(f"Порода: {dog2.get_breed()}")
print(f"Возраст: {dog2.get_age()}")

print("\nПроверка валидации:")
try:
    dog2.set_age(-5)
except ValueError as e:
    print(f"Ошибка: {e}")