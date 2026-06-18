# healthcheck.py
import platform, shutil, json, os

def get_free_memory_mb():
	total, used, free = shutil.disk_usage(".")
	return free // (1024 * 1024)

data = {
	"os": platform.platform(),
	"python_version": platform.python_version(),
	"free_memory_mb": get_free_memory_mb(),
	"file_exists": os.path.exists("../terraform/output.txt")
}

# Сохраняем отчёт в JSON-файл
with open("health.json", "w", encoding="utf-8") as f:
	json.dump(data, f, ensure_ascii=False, indent=2)

# Печать JSON в консоль
print(json.dumps(data, ensure_ascii=False, indent=2))
