import ollama
from pathlib import Path
import json

MODEL = "llama3.2:3b"

messages = [
        {"role": "system", "content": "Ты дружелюбный помощник. Отвечай кратко, на русском."},
]

print("Чат запущен. Напиши \"выход\" для завершения.")

name_file = "chat_history.json"
data_dir = Path("data")
data_dir.mkdir(exist_ok=True)
chat_history_path = data_dir / name_file

if chat_history_path.exists():
    with open(chat_history_path, "r", encoding="utf-8") as f:
        chat_history = json.load(f)
    if chat_history:
        messages = chat_history


def save_chat_history():
    with open(chat_history_path, "w", encoding="utf-8") as f:
        json.dump(messages, f, ensure_ascii=False, indent=2)

while True:
    user_input = input("Ты: ")

    if user_input.lower() in ("выход", "exit", "quit"):
        print("Чат завершен.")
        break

    if user_input.lower() in ("сброс", "reset"):
        messages = messages[:1]
        print("История чата сброшена.")
        if chat_history_path.exists():
            chat_history_path.unlink()
        continue

    messages.append({"role": "user", "content": user_input})
    response = ollama.chat(
        model=MODEL,
        messages=messages
    )
    answer = response["message"]["content"]
    messages.append({"role": "assistant", "content": answer})

    print(f"Бот: {answer}\n")
    save_chat_history()
    