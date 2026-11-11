import json
from pathlib import Path # Для работы с файловой системой и путями к файлам

data_dir = Path("data") # Папка для хранения файлов
file_path = data_dir / "test.txt"

with open(file_path, "w", encoding="utf-8") as f:
    f.write("Привет, файл!\n")
    f.write("Второй строкой\n")
    
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()
print(content)

print(file_path.read_text(encoding="utf-8"))

user = {
    "name": "Максим",
    "langs": ["Python", "JavaScript"],
    "level": "1"
}

json_path = data_dir / "user.json"

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(user, f, ensure_ascii=False, indent=2)
    
with open(json_path, "r", encoding="utf-8") as f:
    loaded = json.load(f)
print(loaded["name"], loaded["langs"], loaded["level"])
print(type(loaded))
