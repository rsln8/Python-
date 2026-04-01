# Задание 3: Работа с деревом файлов

import copy

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

tree_copy = copy.deepcopy(tree)

print("=" * 50)
print("ЗАДАНИЕ 3: Дерево файлов")
print("=" * 50)

print("До преобразования:")
print(f"  config.json: {tree['children'][0]['children'][1]['children'][0]['name']}")
print(f"  hosts: {tree['children'][1]['name']}")

convert_filenames_to_uppercase(tree_copy)

print("\nПосле преобразования:")
print(f"  config.json: {tree_copy['children'][0]['children'][1]['children'][0]['name']}")
print(f"  hosts: {tree_copy['children'][1]['name']}")
print("\nПримечание: имена директорий остались без изменений")