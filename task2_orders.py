# Задание 2: Заказы пользователей

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

user_books = {}

for user_id, book in orders:
    if user_id not in user_books:
        user_books[user_id] = set()
    user_books[user_id].add(book)

top_user = None
max_books = 0

for user_id, books in user_books.items():
    if len(books) > max_books:
        max_books = len(books)
        top_user = user_id

print("=" * 50)
print("ЗАДАНИЕ 2: Заказы пользователей")
print("=" * 50)
print("1. Словарь user_books:")
for user_id, books in user_books.items():
    print(f"   {user_id}: {books}")

print(f"\n2. Пользователь с наибольшим количеством уникальных книг:")
print(f"   ID: {top_user}, книг: {max_books}")
print(f"   Книги: {user_books[top_user]}")