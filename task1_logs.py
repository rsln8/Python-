# Задание 1: Логи посещения сайта

logs = [
    "192.168.1.1 2023-10-01 10:00:00 200",
    "192.168.1.2 2023-10-01 10:05:00 404",
    "192.168.3.1 2023-10-01 10:10:00 500",
    "10.0.0.1 2023-10-01 10:15:00 200",
    "192.168.1.2 2023-10-01 10:20:00 200"
]

ip_list = []
status_counts = {'200': 0, '404': 0, '500': 0}

for log in logs:
    parts = log.split()
    ip = parts[0]
    status = parts[3]
    
    ip_list.append(ip)
    if status in status_counts:
        status_counts[status] += 1

unique_ips = list(set(ip_list))

print("=" * 50)
print("ЗАДАНИЕ 1: Логи посещения")
print("=" * 50)
print(f"1. Список IP-адресов: {ip_list}")
print(f"2. Уникальные IP-адреса: {unique_ips}")
print(f"3. Статусы ответов: {status_counts}")
