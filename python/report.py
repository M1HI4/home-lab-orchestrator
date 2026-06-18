# report.py
import json

# Читаем данные из JSON, полученного healthcheck.py
with open("health.json", encoding="utf-8") as f:
	data = json.load(f)

# Формируем и печатаем текстовый отчёт
os_info = data.get("os", "N/A")
py_ver = data.get("python_version", "N/A")
free_mem = data.get("free_memory_mb", 0)
file_exists = data.get("file_exists", False)

print(f"ОС: {os_info}")
print(f"Версия Python: {py_ver}")
print(f"Свободная память: {free_mem} MB")
print(f"Файл output.txt существует: {'Да' if file_exists else 'Нет'}")

