"""
ВСЕ ЗАДАНИЯ В ОДНОМ ФАЙЛЕ
Python - решение 5 задач
"""

import copy
from datetime import datetime

print("\n" + "="*60)
print("РЕШЕНИЕ ВСЕХ ЗАДАНИЙ")
print("="*60)

# ============================================
# ЗАДАНИЕ 1: Логи посещения сайта
# ============================================

print("\n" + "="*60)
print("ЗАДАНИЕ 1: Логи посещения сайта")
print("="*60)

logs = [
    "192.168.1.1 2023-10-01 10:00:00 200",
    "192.168.1.2 2023-10-01 10:05:00 404",
    "192.168.3.1 2023-10-01 10:10:00 500",
    "10.0.0.1 2023-10-01 10:15:00 200",
    "192.168.1.2 2023-10-01 10:20:00 200"
]

# 1. Создаем список IP-адресов
ip_list = []
status_counts = {'200': 0, '404': 0, '500': 0}
times = []

for log in logs:
    parts = log.split()
    ip = parts[0]
    date_str = parts[1]
    time_str = parts[2]
    status = parts[3]
    
    ip_list.append(ip)
    
    if status in status_counts:
        status_counts[status] += 1
    
    dt_str = f"{date_str} {time_str}"
    dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
    times.append(dt)

# 2. Уникальные IP-адреса
unique_ips = list(set(ip_list))

# 4. Время
earliest_time = min(times)
latest_time = max(times)

print(f"1. Список IP-адресов: {ip_list}")
print(f"2. Уникальные IP-адреса: {unique_ips}")
print(f"3. Статусы ответов: {status_counts}")
print(f"4. Самое раннее посещение: {earliest_time}")
print(f"   Самое позднее посещение: {latest_time}")


# ============================================
# ЗАДАНИЕ 2: Заказы пользователей
# ============================================

print("\n" + "="*60)
print("ЗАДАНИЕ 2: Заказы пользователей")
print("="*60)

orders = [
    (101, "Python для начинающих"),
    (101, "Алгоритмы и структуры данных"),
    (102, "Чистый код"),
    (101, "Python для начинающих"),
    (103, "Искусство программирования"),
    (102, "Python для начинающих"),
    (103, "Чистый код"),
    (101, "Грокаем алгоритмы"),
    (102, "Грокаем алгоритмы"),
    (103, "Алгоритмы и структуры данных"),
    (102, "Чистый код"),
    (104, "Python для начинающих")
]

# 1. Создаем словарь user_books
user_books = {}

for user_id, book in orders:
    if user_id not in user_books:
        user_books[user_id] = set()
    user_books[user_id].add(book)

# 2. Находим пользователя с наибольшим количеством книг
top_user = max(user_books.items(), key=lambda x: len(x[1]))

print("1. Словарь user_books:")
for user_id, books in user_books.items():
    print(f"   {user_id}: {books}")

print(f"\n2. Пользователь с наибольшим количеством уникальных книг:")
print(f"   ID: {top_user[0]}, книг: {len(top_user[1])}")
print(f"   Книги: {top_user[1]}")


# ============================================
# ЗАДАНИЕ 3: Работа с деревом файлов
# ============================================

print("\n" + "="*60)
print("ЗАДАНИЕ 3: Работа с деревом файлов")
print("="*60)

tree = {
    'name': '/',
    'meta': {},
    'type': 'directory',
    'children': [
        {
            'name': 'eTc',
            'meta': {},
            'type': 'directory',
            'children': [
                {
                    'name': 'NgiNx',
                    'meta': {'size': 4000},
                    'type': 'directory',
                    'children': [],
                },
                {
                    'name': 'CONSUL',
                    'meta': {},
                    'type': 'directory',
                    'children': [
                        {
                            'name': 'config.json',
                            'type': 'file',
                        },
                    ],
                },
            ],
        },
        {'name': 'hosts', 'type': 'file', 'meta': {}},
    ],
}

def convert_filenames_to_uppercase(node):
    """Рекурсивно приводит имена всех файлов к верхнему регистру"""
    if node.get('type') == 'file':
        node['name'] = node['name'].upper()
    elif node.get('type') == 'directory' and 'children' in node:
        for child in node['children']:
            convert_filenames_to_uppercase(child)

# Создаем копию для тестирования
tree_copy = copy.deepcopy(tree)

print("До преобразования:")
print(f"  config.json: {tree['children'][0]['children'][1]['children'][0]['name']}")
print(f"  hosts: {tree['children'][1]['name']}")

convert_filenames_to_uppercase(tree_copy)

print("\nПосле преобразования:")
print(f"  config.json: {tree_copy['children'][0]['children'][1]['children'][0]['name']}")
print(f"  hosts: {tree_copy['children'][1]['name']}")
print("\nПримечание: имена директорий остались без изменений")


# ============================================
# ЗАДАНИЕ 4: Класс Dog
# ============================================

print("\n" + "="*60)
print("ЗАДАНИЕ 4: Класс Dog")
print("="*60)

class Dog:
    """Класс для представления собаки"""
    
    def __init__(self, name=None, breed=None, age=None):
        self._name = name
        self._breed = breed
        self._age = age
    
    # Геттеры (просмотр)
    def get_name(self):
        return self._name
    
    def get_breed(self):
        return self._breed
    
    def get_age(self):
        return self._age
    
    # Сеттеры (изменение)
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


# Демонстрация
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


# ============================================
# ЗАДАНИЕ 5: Сотрудники компании
# ============================================

print("\n" + "="*60)
print("ЗАДАНИЕ 5: Сотрудники компании")
print("="*60)

employees = [
    {"name": "Анна Смирнова", "department": "IT", "salary": 120000, "age": 28, "experience": 5},
    {"name": "Иван Петров", "department": "Sales", "salary": 95000, "age": 35, "experience": 10},
    {"name": "Мария Иванова", "department": "HR", "salary": 85000, "age": 42, "experience": 15},
    {"name": "Дмитрий Сидоров", "department": "IT", "salary": 150000, "age": 31, "experience": 7},
    {"name": "Елена Козлова", "department": "Sales", "salary": 110000, "age": 29, "experience": 6},
    {"name": "Сергей Михайлов", "department": "IT", "salary": 90000, "age": 24, "experience": 2},
    {"name": "Ольга Новикова", "department": "HR", "salary": 95000, "age": 38, "experience": 12},
    {"name": "Алексей Федоров", "department": "Sales", "salary": 130000, "age": 33, "experience": 8},
    {"name": "Татьяна Морозова", "department": "IT", "salary": 140000, "age": 36, "experience": 9},
    {"name": "Константин Васильев", "department": "Sales", "salary": 88000, "age": 26, "experience": 3},
    {"name": "Наталья Павлова", "department": "HR", "salary": 105000, "age": 45, "experience": 18},
    {"name": "Максим Соколов", "department": "IT", "salary": 160000, "age": 29, "experience": 6}
]

# 1. Сортировка по зарплате (от максимальной к минимальной)
sorted_by_salary = sorted(employees, key=lambda x: x['salary'], reverse=True)

# 2. Сортировка по возрасту (от минимального к максимальному)
sorted_by_age = sorted(employees, key=lambda x: x['age'])

print("\n1. Сотрудники по зарплате (от максимальной к минимальной):")
print("-"*65)
for i, emp in enumerate(sorted_by_salary, 1):
    print(f"{i:2}. {emp['name']:<20} | {emp['department']:8} | {emp['salary']:>7} руб. | Возраст: {emp['age']}")

print("\n2. Сотрудники по возрасту (от минимального к максимальному):")
print("-"*65)
for i, emp in enumerate(sorted_by_age, 1):
    print(f"{i:2}. {emp['name']:<20} | {emp['department']:8} | Возраст: {emp['age']:2} | Зарплата: {emp['salary']} руб.")

print("\n" + "="*60)
print("ВСЕ ЗАДАНИЯ ВЫПОЛНЕНЫ!")
print("="*60)